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
# Run Both Frontend and Backend
Terminal 1:
```

uvicorn backend.api.main:app --reload
```

Terminal 2:
```
cd frontend
npm run dev
```

## Backend File Structure
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
```
## Frontend File Structure
```

├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── ProfilesPage.jsx
│   │   │   ├── Assets.jsx
│   │   │   └── Quests.jsx
│   │   ├── components/
│   │   │   └── Profiles.jsx
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

### Developer Note: Password Placeholder

This prototype currently inserts a temporary placeholder value for `password_hash`.

```python
# routes/users.py
 
password_hash = "TEMP_HASH"

cursor = db.execute(
    'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
    (user.username, user.email, "TEMP_HASH")
)
```