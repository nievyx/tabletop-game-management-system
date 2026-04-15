# Databases-Assignment

Relational database + CRUD demo REST API wrapper

> Project intentionally not using an ORM like SQL Alechemy nor Flask, extensive prior use of Flask-based frameworks. See project below for SQL database implementaion via ORM: 
<https://github.com/nievyx/FlaskInventoryApp>

> seed.sql setup with a space themed tabletop game alongside a DRM platform



## Setup database (First run only)
<details>
<summary>Setup Virtual environment</summary>

```bash
python -m venv .venv
./venv\Scripts\activate
pip install -r requirements.txt
```
</details>

---
Run from project root:

```bash
python backend/database/reset_db.py
```

## How to run API ( Windows / Powershell)

Run from project root:
```bash
uvicorn backend.api.main:app --reload
```
or
```
python -m api
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
```
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
│   ├──  routes.py             # endpoints
│   ├── __init__.py 
│   └── __main__.py        
│
├── README.md
├── pyproject.toml
├── requirements.txt # Runtime dependies (pip/venv)
├── .env.example
└── .gitignore      

```

## Desired File Structure
```
database-assignment/
├── backend/
│   ├── api/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── users.py
│   │   │   ├── profiles.py
│   │   │   ├── assets.py
│   │   │   └── quests.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── database/
│   │   ├── schema.sql
│   │   ├── seed.sql
│   │   ├── reset_db.py
│   │   └── db.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Profiles.jsx
│   │   │   ├── Assets.jsx
│   │   │   └── Quests.jsx
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── docs/
│   ├── erd.png
│   ├── data-dictionary.docx
│   └── notes.md
├── README.md
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
