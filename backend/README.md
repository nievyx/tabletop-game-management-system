# Backend

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

## How to run API ( Windows / PowerShell)

Run from project root:
```bash
uvicorn backend.app.main:app --reload
```
or
```
python -m backend.api
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
backend/
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── reset_db.py
│   ├── db.py                 # connection + query helpers
│   ├── app.db                # Ignored by git
│   └── __init__.py 
│
├── api/
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Pydantic request/response schemas
│   ├──  routes.py             # endpoints
│   ├── __init__.py 
│   └── __main__.py        
│
├── README.md
```
## File Structure
```

backend/
├── api/
│   ├── main.py        
│   ├── routes/
│   │   ├── users.py
│   │   ├── profiles.py
│   │   ├── assets.py
│   │   └── quests.py
│   ├── models.py
│   └── schemas.py
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── reset_db.py
│   └── db.py
└── requirements.txt
```