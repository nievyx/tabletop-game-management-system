from fastapi import FastAPI
from api.routes import router
from demo.demo import demo

app = FastAPI()
app.include_router(router)

print(demo())