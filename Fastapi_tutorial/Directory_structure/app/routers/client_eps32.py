from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas.client_esp32 import Client, CreateClient, Token, Temperature_s, RegisterTemperature
from crud.client_esp32 import create_client, read_all_clients, login_client, register_temperature, read_all_temperature
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

@router.post("/temperature", response_model=Temperature_s)
def register_temperatures(data: RegisterTemperature, db: Session = Depends(get_db)):
    print("-"*60)
    print(data)
    print("-"*60)
    return register_temperature(db, data)

@router.get("/readtemperature")
def read_temperature(db: Session = Depends(get_db)):
    all_temperature = read_all_temperature(db)
    return {"message": all_temperature}