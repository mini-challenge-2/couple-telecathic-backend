from fastapi import FastAPI
from app.schemas import Response
from app.api.v1 import router

app = FastAPI()

@app.get("/")
async def root():
    return Response(status=200, message="success")

app.include_router(router, prefix='/api/v1')