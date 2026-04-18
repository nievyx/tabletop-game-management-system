# Databases-Assignment

Relational database + CRUD demo REST API wrapper

> Project intentionally not using an ORM like SQL Alechemy nor Flask, extensive prior use of Flask-based frameworks. See project below for SQL database implementaion via ORM: 
<https://github.com/nievyx/FlaskInventoryApp>

> seed.sql setup with a space themed tabletop game alongside a DRM platform

## Quick start

```bash
python backend/database/reset_db.py
uvicorn backend.api.main:app --reload
```

## Reset Database
```
python backend/database/reset_db.py
```


## File Structure
```
databases-assignment/
├── backend/database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── reset_db.py
│   ├── db.py                 # connection + query helpers
│   ├── app.db                # Ignored by git
│   └── __init__.py 
│
├── backend/demo/
│   ├── demo.py               # CLI CRUD demo
│   └── test_db.py
│
├── backend/api/
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
root/
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
