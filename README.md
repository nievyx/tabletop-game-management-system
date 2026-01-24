# Databases-Assignment

## File Structure
```
databases-assignment/
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── reset_db.py
│   ├── db.py                 # connection + query helpers
│   └── app.db                # Ignored by git
│
├── demo/
│   └── demo.py               # CLI CRUD demo
│
└── api/
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Pydantic request/response schemas
│   └── routes.py             # endpoints
│
├── README.md
├── pyproject.toml
├── .env.example
└── .gitignore      

```