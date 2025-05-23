from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas.client_esp32 import Client, CreateClient, Token, Temperature_s, RegisterTemperature
from crud.client_esp32 import create_client, read_all_clients, c_login_client, register_temperature, read_all_temperature
from security import verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/clientesp",tags=["clientesp"])

@router.post("/", response_model=Client)
def create_clients(client: CreateClient, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.post("/login", response_model=Token)
def r_login_client(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  
    client = c_login_client(db,form_data.username)
    if not client or not verify_password(form_data.password, client.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    access_token = create_access_token(data={"sub":client.name})

    return {"access_token": access_token, "token_type":"bearer"}

@router.post("/private")
def r_read_logged_client(current_client: Client = Depends(get_current_user)):
   
    return {
        "name": current_client.name
    }

@router.get("/readall")
def r_read_all_clients(db: Session = Depends(get_db)):
    return read_all_clients(db)

@router.post("/temperature", response_model=Temperature_s)
def register_temperatures(data: RegisterTemperature, db: Session = Depends(get_db)):
    print("-"*60)
    print(data)
    print("-"*60)
    return register_temperature(db, data)


@router.get("/readtemperature")
def read_temperature(db: Session = Depends(get_db), current_client: Client = Depends(get_current_user)):
    all_temperature = read_all_temperature(db)
    return {"message": all_temperature}