from fastapi import FastAPI
from app.routers import report

app = FastAPI()

app.include_router(report.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}