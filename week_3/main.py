from routers import users
from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models, crud
from schemas import CreateUser, User, CreateProduct, Product

# Criando tabelas definidas em models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

def comum():
    print("Executando lágica comum")
    return "valor comum"

@app.get("/teste/")
async def exemplo(dep=Depends(comum)):
    return {"resultado": dep}
