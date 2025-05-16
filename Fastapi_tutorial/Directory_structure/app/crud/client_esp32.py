from sqlalchemy.orm import Session
from models.client_esp32 import Client_Esp32
from schemas.client_esp32 import CreateClient, Client
from security import hash_password, verify_password


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