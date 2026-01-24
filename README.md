# Databases-Assignment

## File Structure
```py
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
├── api/
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Pydantic request/response schemas
│   └── routes.py             # endpoints
│
├── README.md
├── pyproject.toml
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