from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas.client_esp32 import Client, CreateClient, Token
from crud.client_esp32 import create_client, read_all_clients, login_client
from security import verify_password

router = APIRouter(prefix="/clientesp",tags=["clientesp"])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.post("/", response_model=Client)
def create_clients(client: CreateClient, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.post("/login", response_model=Token)
def login_client(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    client = login_client(db,form_data.username)
    if not user or not verify_password(form_data.password, client.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    


    return