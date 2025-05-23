# from fastapi import FastAPI
from routers import usuario,client_eps32
from database import Base, engine
from app import app

Base.metadata.create_all(bind=engine)

# app = FastAPI()
app.include_router(usuario.router)
app.include_router(client_eps32.router)