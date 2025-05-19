from sqlalchemy.orm import Session
from models.client_esp32 import Client_Esp32, Temperature
from schemas.client_esp32 import CreateClient, Client, RegisterTemperature, Temperature_s
from security import hash_password, verify_password
from datetime import datetime

actual_date_time = str(datetime.now())

# Client
def create_client(db: Session, client: CreateClient):

    password = hash_password(client.password)

    new_client = Client_Esp32(name=client.name, password=password)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def login_client(db: Session, name: str):
    print("        ")
    print("        ")
    print("        ")
    print("##########################################################################")
    print(db.query(Client_Esp32).filter(Client_Esp32.name == name).first())
    print("##########################################################################")
    print("        ")
    print("        ")
    print("        ")
    return db.query(Client_Esp32).filter(Client_Esp32.name == name).first()

def read_all_clients(db:Session):
    return db.query(Client_Esp32).all()

# Temperature
def register_temperature(db: Session, data: RegisterTemperature):

    print(data.data_hora)
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