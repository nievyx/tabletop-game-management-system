from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.config import settings # NOTE: loads env
from backend.app.routes import health, players, characters
import os


app = FastAPI()


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



app.include_router(health.router)
app.include_router(players.router)
app.include_router(characters.router)

@app.get('/db-check')
def health():
    return {"status": "ok"}

# print(demo())