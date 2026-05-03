from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import Category, Product, Cart, CartItem, Order, OrderItem, Review
from .serializers import (
    RegisterSerializer, CategorySerializer, ProductSerializer,
    CartSerializer, CartItemSerializer, OrderSerializer, ReviewSerializer
)
from django.contrib.auth.models import User



# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'User created successfully'},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'description']
    filterset_fields = ['category']
    ordering_fields = ['price', 'created_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_add(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'No product found'}, status=404)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    return Response({'message': 'Cart added successfully'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cart_remove(request, pk):
    try:
        cart_item = CartItem.objects.get(id=pk, cart__user=request.user)
        cart_item.delete()
        return Response({'message': 'Item removed from cart'})
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
    if not cart_items.exists():
        return Response({'error': 'cart is empty'}, status=400)
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    order = Order.objects.create(
        user=request.user,
        total_price=total
    )
    
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    
    cart_items.delete()
    
    return Response({'message': 'order placed', 'order_id': order.id})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def review_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'error': 'No product found'}, status=404)
    
    if request.method == 'GET':
        reviews = Review.objects.filter(product=product)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        if Review.objects.filter(product=product, user=request.user).exists():
            return Response({'error': ' ALREADY REVIEWED'}, status=400)
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

