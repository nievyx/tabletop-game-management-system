# Databases-Assignment

Relational database + CRUD demo REST API wrapper

> seed.sql setup with a space themed tabletop game alongside a DRM platform

## Setup database (First run only)

Run from project root:

```bash
python database/reset_db.py
```

## How to run API ( Windows / Powershell)

Run from project root:
```bash
unicorn api.main:app --reload
```
#### Once Running, visit:
Run database health check
- http://127.0.0.1:8000/db-check
- Expected response:
```json
{"ok": 1 }
```
Users table check
- http://127.0.0.1:8000/db-check-users-table
- Expected response:
```json
{ "users_table_exists": true }

```


## Api Endpoints
- http://127.0.0.1:8000/db-check
- http://127.0.0.1:8000/db-check-users-table


## File Structure
```py
databases-assignment/
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── reset_db.py
│   ├── db.py                 # connection + query helpers
│   ├── app.db                # Ignored by git
│   └── __init__.py 
│
├── demo/
│   ├── demo.py               # CLI CRUD demo
│   └── test_db.py
│
├── api/
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Pydantic request/response schemas
│   ├─  routes.py             # endpoints
│   └── __init__.py            
│
├── README.md
├── pyproject.toml
├── requirements.txt # Runtime dependies (pip/venv)
├── .env.example
└── .gitignore      

```
<details>
<summary>Toggle optional Java structure<strong> 
</strong></summary>

### Optional Java Demo
```java
└── java_demo/
    ├── README.md
    ├── pom.xml
    └── src/
        └── main/
            └── java/
                └── Demo.java
```
</details>