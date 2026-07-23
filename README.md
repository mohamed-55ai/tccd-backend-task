# E-Commerce Backend API

A simplified backend API for an e-commerce platform, built with FastAPI and SQLAlchemy.

## Tech Stack
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic

## Project Structure
```
backend-task/
├── main.py            # API endpoints
├── models.py           # Database models (tables)
├── schemas.py           # Request/response validation schemas
├── database.py          # Database connection setup
└── requirements.txt       # Project dependencies
```

## Features
- Full CRUD operations for **Products**
- Full CRUD operations for **Categories**
- Foreign key relationship between Products and Categories
- Automatic request/response validation
- Interactive API documentation (Swagger UI)

## How to Run

1. Clone the repository:
```
git clone <your-repo-url>
cd backend-task
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the server:
```
uvicorn main:app --reload
```

4. Open your browser at:
```
http://127.0.0.1:8000/docs
```
This opens the interactive Swagger UI where you can test all endpoints.

## API Endpoints

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/products | Create a new product |
| GET | /api/products | Get all products |
| GET | /api/products/{id} | Get a specific product |
| PATCH | /api/products/{id} | Update a product |
| DELETE | /api/products/{id} | Delete a product |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/categories | Create a new category |
| GET | /api/categories | Get all categories |
| GET | /api/categories/{id} | Get a specific category |
| PATCH | /api/categories/{id} | Update a category |
| DELETE | /api/categories/{id} | Delete a category |

## Notes
- The database (`shop.db`) is created automatically on first run — no manual setup needed.
- All endpoints can be tested directly from the Swagger UI at `/docs`.
