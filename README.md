🛒 E-Commerce API — Django REST Framework
Deploy on Railway
 
Python
 
Django
 
DRF
 


🚀 A production-ready E-Commerce REST API built from scratch as a fresher project — featuring complete user authentication, product management, cart system, order placement, and product reviews. Live deployed on Railway with GitHub CI/CD.

🌐 Live project link:
Base URL: https://blog-api-production-b09d.up.railway.app/api/register/

✅ API is live and fully functional. Test it using Postman or any REST client.

🧰 Tech Stack — Full Breakdown
Layer	Technology	Purpose
Language	Python 3.11	Core programming language
Framework	Django 4.x	Web framework
API Layer	Django REST Framework (DRF)	Building RESTful APIs
Authentication	Token Auth (DRF)	Secure user sessions
Image Handling	Pillow	Product image upload & processing
Filtering	django-filter	Query-based product filtering
Database	SQLite (Dev) / PostgreSQL (Prod)	Data storage
Deployment	Railway	Cloud hosting platform
Version Control	GitHub	Source code & CI/CD pipeline
API Testing	Postman	Endpoint testing & documentation
✨ Core Features
🔐 Token-Based Authentication — Secure Register & Login system
👤 Role-Based Access — Admin vs Regular User permissions
📦 Product Management — Full CRUD with image upload via Pillow
📂 Category System — Organize products under categories
🔍 Product Filtering — Filter by category, price, name using django-filter
🛒 Cart System — Add/remove items, view cart total
🧾 Order Management — Place orders, view order history
⭐ Reviews System — Users can post reviews on products
📄 Paginated Responses — Scalable list endpoints
📁 Project Structure
ecommerce-api/
│
├── users/
│   ├── models.py          # Custom User Model
│   ├── serializers.py     # User Serializers
│   └── views.py           # Register, Login Views
│
├── products/
│   ├── models.py          # Product, Category Models
│   ├── serializers.py     # Product Serializers
│   ├── filters.py         # django-filter integration
│   └── views.py           # Product CRUD Views
│
├── cart/
│   ├── models.py          # Cart & CartItem Models
│   └── views.py           # Cart Logic
│
├── orders/
│   ├── models.py          # Order & OrderItem Models
│   └── views.py           # Order Placement Views
│
├── reviews/
│   ├── models.py          # Review Model
│   └── views.py           # Review CRUD
│
├── manage.py
├── requirements.txt
└── README.md
🚀 API Endpoints — Complete Reference
🔐 Authentication
Method	Endpoint	Auth Required	Description
POST	/api/register/	❌ No	Register new user
POST	/api/login/	❌ No	Login & receive token
json


// POST /api/register/ — Request Body
{
  "username": "shaadali",
  "email": "shaad@gmail.com",
  "password": "pass123"
}

// Response 201 Created
{
  "message": "User created successfully"
}
json


// POST /api/login/ — Request Body
{
  "username": "shaadali",
  "password": "pass123"
}

// Response 200 OK
{
  "token": "abc123xyz..."
}
📂 Categories
Method	Endpoint	Auth Required	Description
GET	/api/categories/	❌ No	List all categories
POST	/api/categories/	✅ Admin	Create new category
json


// POST /api/categories/ — Request Body
{
  "name": "Electronics"
}

// Response 201 Created
{
  "id": 1,
  "name": "Electronics"
}
📦 Products
Method	Endpoint	Auth Required	Description
GET	/api/products/	❌ No	List all products (paginated)
POST	/api/products/	✅ Admin	Create new product
GET	/api/products/{id}/	❌ No	Get single product detail
PUT	/api/products/{id}/	✅ Admin	Update product
DELETE	/api/products/{id}/	✅ Admin	Delete product
json


// POST /api/products/ — Request Body
{
  "name": "iPhone 15",
  "description": "Latest Apple smartphone",
  "price": "99999",
  "stock": 10,
  "category": 1,
  "image": "<file_upload>"
}

// GET /api/products/ — Response 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "iPhone 15",
      "price": "99999.00",
      "stock": 10,
      "category": "Electronics",
      "image": "/media/products/iphone15.jpg",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
🔍 Filtering Supported: /api/products/?category=1&price_min=500&price_max=5000

🛒 Cart
Method	Endpoint	Auth Required	Description
GET	/api/cart/	✅ Yes	View user's cart
POST	/api/cart/add/	✅ Yes	Add item to cart
DELETE	/api/cart/remove/{id}/	✅ Yes	Remove item from cart
json


// POST /api/cart/add/ — Request Body
{
  "product_id": 1,
  "quantity": 2
}

// GET /api/cart/ — Response
{
  "id": 1,
  "user": "shaadali",
  "items": [
    {
      "product": "iPhone 15",
      "quantity": 2,
      "price": "99999.00",
      "subtotal": "199998.00"
    }
  ],
  "total": "199998.00"
}
🧾 Orders
Method	Endpoint	Auth Required	Description
POST	/api/orders/place/	✅ Yes	Place order from cart
GET	/api/orders/	✅ Yes	View all user orders
GET	/api/orders/{id}/	✅ Yes	View single order detail
json


// POST /api/orders/place/ — Response 201 Created
{
  "message": "Order placed successfully",
  "order_id": 1,
  "total": "199998.00",
  "status": "pending"
}

// Error if cart empty — 400 Bad Request
{
  "error": "Cart is empty"
}
⭐ Reviews
Method	Endpoint	Auth Required	Description
GET	/api/reviews/	❌ No	List all reviews
POST	/api/reviews/	✅ Yes	Post a product review
DELETE	/api/reviews/{id}/	✅ Yes	Delete own review
json


// POST /api/reviews/ — Request Body
{
  "product": 1,
  "rating": 5,
  "comment": "Excellent product! Highly recommended."
}

// Response 201 Created
{
  "id": 1,
  "user": "shaadali",
  "product": "iPhone 15",
  "rating": 5,
  "comment": "Excellent product! Highly recommended.",
  "created_at": "2024-01-01T00:00:00Z"
}
🔑 Authentication Guide
Sab protected routes ke liye Bearer Token header mein bhejo:

Authorization: Token abc123xyz...
Postman mein: Authorization Tab → Bearer Token → Paste your token

⚙️ Local Setup
bash


# 1. Clone the repo
git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (Admin)
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
📦 Requirements
django
djangorestframework
django-filter
Pillow
gunicorn
python-decouple
📌 Why This Project? — For Recruiters & HR
This project was built entirely from scratch as a fresher to demonstrate real-world backend development skills:

✅ Designed and implemented a complete REST API with 15+ endpoints
✅ Built Token-based authentication system from ground up
✅ Implemented role-based permissions (Admin vs User)
✅ Used Pillow for real product image handling
✅ Integrated django-filter for advanced product search & filtering
✅ Handled error cases with proper HTTP status codes
✅ Deployed to production on Railway with GitHub CI/CD
✅ Followed REST best practices throughout the project
✅ Built 5 independent modules — Auth, Products, Cart, Orders, Reviews

👨‍💻 About the Developer

Mohammad Shaad — Fresher Backend Developer

🔗 GitHub: @Mr-SHAAD
📧 Email: knowmore8126@gmail.com
🌐 Live Project: blog-api-production-b09d.up.railway.app/api/register/
