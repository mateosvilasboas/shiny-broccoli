from fastapi import FastAPI

from app.routers.auth import router as Auth
from app.routers.charts import router as Chart
from app.routers.users import router as User

app = FastAPI()

app.include_router(User)
app.include_router(Auth)
app.include_router(Chart)


@app.get('/')
async def root():
    return {'message': 'Hello World'}
