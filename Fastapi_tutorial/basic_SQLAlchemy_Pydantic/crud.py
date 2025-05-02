from schemas import UserCreate
from sqlalchemy.orm import Session
import models

def create_user(db: Session, user_data: UserCreate):
    user = models.User(name=user_data.name, email=user_data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# def create_user(db: Session, name: str, email: str):
#     user = models.User(name=name, email=email)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# Retorna todos os usuários do DB, com o modelo BaseModel
def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    # return db.query(models.User).all()
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, name: str, email: str):
    user = get_user(db, user_id)
    if user:
        user.name = name
        user.email = email
        db.commit()
        db.refresh(user)
    
    return user

# função que deleta um usuário do DB com base no id
def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user