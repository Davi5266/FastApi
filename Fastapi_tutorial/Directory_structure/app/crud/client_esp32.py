from sqlalchemy.orm import Session
from models.client_esp32 import Client_Esp32
from schemas.client_esp32 import CreateClient
from security import hash_password, verify_password


def create_client(db: Session, client: CreateClient):

    password = hash_password(client.password)

    new_client = Client_Esp32(name=client.name, password=password)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def read_all_clients(db:Session):
    return db.query(Client_Esp32).all()