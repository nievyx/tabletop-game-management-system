## Backend

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