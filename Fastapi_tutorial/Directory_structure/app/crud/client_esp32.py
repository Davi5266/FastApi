from sqlalchemy.orm import Session
from models.client_esp32 import Client_Esp32, Temperature
from schemas.client_esp32 import CreateClient, Client, RegisterTemperature, Temperature_s
from security import hash_password, verify_password
from datetime import datetime
import tracemalloc
tracemalloc.start()

actual_date_time = str(datetime.now())

# Client
def create_client(db: Session, client: CreateClient):

    password = hash_password(client.password)

    new_client = Client_Esp32(name=client.name, password=password)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def c_update_client(db: Session, client_id:int, name: str):
    client = c_get_all_clients(db, client_id)
    if client:
        client.name = name
        db.commit()
        db.refresh(client)
        
    return client

def c_get_all_clients(db:Session, client_id: int):
    return db.query(Client_Esp32).filter(Client_Esp32.id == client_id).first()

def c_login_client(db: Session, username: str):
    print("c_login_client")
    print(username)
    return db.query(Client_Esp32).filter(Client_Esp32.name == username).first()

def read_all_clients(db:Session):
    return db.query(Client_Esp32).all()

def get_user_by_username(db: Session, username:str):
    return db.query(Client_Esp32).filter(Client_Esp32.name == username).first()

# Temperature
def register_temperature(db: Session, data: RegisterTemperature):

    # print(data.data_hora)
    print(data.humidade)
    print(data.temperature_C)
    print(data.temperature_F)

    new_register = Temperature(data_hora=str(actual_date_time),humidade=data.humidade, temperature_C=data.temperature_C, temperature_F=data.temperature_F)
    db.add(new_register)
    db.commit()
    db.refresh(new_register)

    return new_register

def read_all_temperature(db:Session):
    return db.query(Temperature).all()