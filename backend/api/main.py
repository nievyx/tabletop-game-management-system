from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from backend.api.routes import health, users, profiles, characters
import os

load_dotenv()

app = FastAPI()

app.include_router(health.router)
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(characters.router)

origins = os.getenv(
    'frontend_origins',
    'http://localhost:5173',
).split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/db-check')
def health():
    return {"status": "ok"}

# print(demo())