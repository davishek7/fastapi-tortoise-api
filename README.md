# FastAPI Orders API

A modular API built using **FastAPI**, **Tortoise ORM**, and **Aerich**, designed to manage customers and orders.  
The project uses `uv` for virtual environment and dependency management, and follows a Django-style folder structure.

---

## Features

- FastAPI for async REST APIs  
- Tortoise ORM for database modeling and queries  
- Aerich for migrations  
- SQLite as local database  
- Environment isolation with `uv`  
- Modular, maintainable structure with separate apps for customers and orders

---

## Folder Structure

```
app/
├── configs/
│   ├── db.py              # Tortoise ORM configuration
│   └── settings.py        # Application settings
│
├── customer/
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── order/
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── enum.py
│   └── serializer.py
│
└── main.py                # FastAPI entry point

migrations/
└── models/               # Aerich migration files
```

---

## Installation and Setup

### 1. Create Virtual Environment and Install Dependencies

```bash
uv venv
uv sync
```

If using a `requirements.txt` file:

```bash
uv pip install -r requirements.txt
```

---

### 2. Initialize Database and Run Migrations

Initialize Aerich (first-time setup):

```bash
uv run aerich init -t app.configs.db.TORTOISE_ORM
```

Generate schema:

```bash
uv run aerich init-db
```

When you change models, create and apply migrations:

```bash
uv run aerich migrate
uv run aerich upgrade
```

---

### 3. Run the Application

Start FastAPI with:

```bash
uv run fastapi dev app/main.py
```

Access your API at:  
**http://127.0.0.1:8000**

Documentation:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

---

## Database Configuration

Defined in `app/configs/db.py`:

```python
TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3"
    },
    "apps": {
        "models": {
            "models": [
                "app.customer.models",
                "app.order.models",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}
```

> Note: Do not use `generate_schemas=True` in `register_tortoise()` if you’re using Aerich.

---

## Postman Collection

You can test all API endpoints using the included Postman collection file:  
`postman_collection.json`

### Import Instructions
1. Open Postman → click **Import** → select the `.json` file.
2. Set environment variable:
   ```
   base_url = http://127.0.0.1:8000
   ```
3. Use the following endpoints:

| Action | Method | URL |
|--------|---------|-----|
| List all customers | GET | `{{base_url}}/api/customers/` |
| Get customer by ID | GET | `{{base_url}}/api/customers/{customer_id}` |
| Create new customer | POST | `{{base_url}}/api/customers/` |
| Create order | POST | `{{base_url}}/api/orders/` |
| Get order by ID | GET | `{{base_url}}/api/orders/{order_id}` |
| Get customer’s total spend | GET | `{{base_url}}/api/orders/customer/{customer_id}/total_spend` |
| Update order status | PUT | `{{base_url}}/api/orders/{order_id}/status?new_status=Confirmed` |

---

## Example: Create Order Request

```json
{
  "customer_id": "string",
  "status": "Draft",
  "order_items": [
    {
      "product_name": "string",
      "quantity": 1,
      "price": 99.99
    }
  ]
}
```

---

## Notes

- Primary keys use UUID.
- SQLite journal files (`db.sqlite3-shm`, `db.sqlite3-wal`) are normal.
- Aerich handles all schema migrations — manual schema generation is not needed.
- Project follows separation of concerns for cleaner maintainability.

---

## License

This project is for educational and demonstration purposes.