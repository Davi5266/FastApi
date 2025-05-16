from models import Usuario
from mysql_config import SessionLocal

session = SessionLocal()

def create_user(name, email):
     
    new_user = Usuario(nome = name, email = email)
    session.add(new_user)
    session.commit()
    session.close()

def read_users():
    usuarios = session.query(Usuario).all()
    for u in usuarios:
        print(u.nome, u.email)

    session.close()

read_users()




