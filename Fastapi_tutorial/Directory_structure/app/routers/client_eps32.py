from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.client_esp32 import Client, CreateClient
from crud.client_esp32 import create_client, read_all_clients

router = APIRouter(prefix="/clientesp",tags=["clientesp"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Client)
def create_clients(client: CreateClient, db: Session = Depends(get_db)):
    return create_client(db, client)