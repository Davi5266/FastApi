from fastapi import Depends
from routers import users
from fastapi import FastAPI
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)

def comum():
    print("Executando lágica comum")
    return "valor comum"

@app.get("/teste/")
async def exemplo(dep=Depends(comum)):
    return {"resultado": dep}