from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    # Auth
    path('register/', views.register_view),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
    # Cart
    path('cart/', views.cart_view),
    path('cart/add/', views.cart_add),
    path('cart/remove/<int:pk>/', views.cart_remove),
    
    # Orders
    path('orders/', views.order_history),
    path('orders/place/', views.place_order),
    
    # Reviews
    path('products/<int:pk>/reviews/', views.review_view),
    
    # ViewSets
    path('', include(router.urls)),
]