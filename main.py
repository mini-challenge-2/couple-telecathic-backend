from fastapi import FastAPI
from app.schemas import Response

app = FastAPI()


@app.get("/")
async def root():
    return Response(status=200, message="success")