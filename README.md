# 🛒 E-Commerce REST API

A production-ready **E-Commerce Backend API** built with **Django REST Framework** and **PostgreSQL** — featuring complete shopping functionality with JWT Authentication, Role-based Access Control, Cart Management, Order Processing, and Product Reviews.

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-green?style=flat&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.14-red?style=flat)](https://django-rest-framework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat&logo=postgresql&logoColor=white)](https://postgresql.org)
[![JWT](https://img.shields.io/badge/Auth-JWT-orange?style=flat)](https://jwt.io)
[![Railway](https://img.shields.io/badge/Deployed-Railway-purple?style=flat&logo=railway&logoColor=white)](https://web-production-746fb.up.railway.app)

## 🌐 Live Demo

> **Base URL:** https://web-production-746fb.up.railway.app/api/register

---

## 🚀 Features

- ✅ **JWT Authentication** — Secure Register, Login, Token Refresh
- ✅ **Role-based Access** — Admin vs Customer permissions
- ✅ **Products Management** — Full CRUD with image upload
- ✅ **Categories** — Product categorization system
- ✅ **Cart System** — Add, Remove, Update quantity
- ✅ **Order Processing** — Place orders, track history
- ✅ **Reviews & Ratings** — Product review system
- ✅ **Search & Filter** — By name, category, price range
- ✅ **Pagination** — 10 products per page
- ✅ **PostgreSQL** — Production-grade database

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.11 | Core Language |
| Django 4.2 | Web Framework |
| Django REST Framework | API Development |
| PostgreSQL | Database |
| SimpleJWT | Authentication |
| Pillow | Image Handling |
| django-filter | Search & Filtering |
| python-decouple | Environment Variables |
| Railway | Cloud Deployment |

---

## 📁 Project Structure

```
ecommerce-api/
├── store/
│   ├── models.py        # Product, Cart, Order, Review models
│   ├── serializers.py   # Data serialization
│   ├── views.py         # API business logic
│   ├── urls.py          # URL routing
│   └── admin.py         # Admin panel config
├── core/
│   ├── settings.py      # Project configuration
│   └── urls.py          # Main URL config
├── Procfile             # Railway deployment
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🔗 API Endpoints

### 🔐 Authentication
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/register/` | Register new user | ❌ |
| POST | `/api/login/` | Login — JWT token | ❌ |
| POST | `/api/token/refresh/` | Refresh token | ❌ |

### 📦 Products
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/products/` | All products (search, filter, paginate) | ❌ |
| POST | `/api/products/` | Create product | ✅ Admin |
| GET | `/api/products/{id}/` | Product detail | ❌ |
| PUT | `/api/products/{id}/` | Update product | ✅ Admin |
| DELETE | `/api/products/{id}/` | Delete product | ✅ Admin |

### 🗂️ Categories
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/categories/` | All categories | ❌ |
| POST | `/api/categories/` | Create category | ✅ Admin |

### 🛒 Cart
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/cart/` | View cart + total | ✅ |
| POST | `/api/cart/add/` | Add product to cart | ✅ |
| DELETE | `/api/cart/remove/{id}/` | Remove item | ✅ |

### 📋 Orders
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/orders/place/` | Place order from cart | ✅ |
| GET | `/api/orders/` | Order history | ✅ |

### ⭐ Reviews
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/products/{id}/reviews/` | Get reviews | ✅ |
| POST | `/api/products/{id}/reviews/` | Add review + rating | ✅ |

### 🔍 Search & Filter
```
GET /api/products/?search=phone
GET /api/products/?category=1
GET /api/products/?ordering=price
GET /api/products/?ordering=-price
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.11+
- PostgreSQL
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Mr-SHAAD/ecommerce-api.git
cd ecommerce-api

# 2. Create virtual environment
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
touch .env
```

Add to `.env`:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=ecommerce
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

```bash
# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Start server
python manage.py runserver
```

---

## 🧪 API Testing (Postman)

**Step 1 — Register:**
```json
POST /api/register/
{
    "username": "testuser",
    "email": "test@gmail.com",
    "password": "pass123"
}
```

**Step 2 — Login & get token:**
```json
POST /api/login/
{
    "username": "testuser",
    "password": "pass123"
}
```

**Step 3 — Add to Cart:**
```json
POST /api/cart/add/
Headers: Authorization: Bearer <token>
{
    "product_id": 1,
    "quantity": 2
}
```

**Step 4 — Place Order:**
```
POST /api/orders/place/
Headers: Authorization: Bearer <token>
```

---

## 👨‍💻 Author

**Mohammad Shaad (iamshaadgour)**
- 🐙 GitHub: [@Mr-SHAAD](https://github.com/Mr-SHAAD)
- 💼 LinkedIn: [Mohammad Shaad](https://linkedin.com/in/mohammad-shaad-672334204)
- 📧 Email: knowmore8126@gmail.com

---

⭐ **If you found this helpful, please star this repo!**
