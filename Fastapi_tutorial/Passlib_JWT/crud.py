from schemas import CreateUser, CreateProduct
from sqlalchemy.orm import Session
import models
from typing import Union
from security import hash_password

#CRUD é um acrônimo que representa as quatro operações básicas de persistência em bancos de dados: Create (Criar), Read (Ler), Update (Atualizar) e Delete (Excluir).

# Registra Usuário no banco de dados
def create_user(db: Session, user_data: CreateUser):
    #criptografando senha
    hashed_pw = hash_password(user_data.password)

    user = models.User(name = user_data.name, dt_nasc = user_data.dt_nasc, email = user_data.email, tel = user_data.tel, password = hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#Pega um usuário com base no seu id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Ler todos os usários
def get_users(db: Session):
    return db.query(models.User).all()

# Atualiza usuário no banco de dados
def update_user(db: Session, user_id: int, name: str, dt_nasc: str, email: str, tel:str):
    user = get_user(db, user_id)
    if user:
        user.name = name
        user.dt_nasc = dt_nasc
        user.email = email
        user.tel = tel

    return user

# Deleta usuário do banco de dados
def delete_user(db:Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user

#Pesquisa usuário por email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Registra produto no banco de dados
def create_product(db: Session, user_product: CreateProduct):
    product = models.Product(name = user_product.name, type = user_product.type, value = user_product.value, desc = user_product.desc)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

#Pega um produto com base no seu id
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Pega todos os produtos
def get_products(db: Session):
    return db.query(models.Product).all()

def update_product(db: Session, product_id: int, name: str,type: str, value: int, desc: str | None):
    product = get_product(db, product_id)
    if product:
        product.name = name
        product.type = type
        product.value = value
        product.desc = desc
        db.commit()
        db.refresh(product)
    
    return product

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()

    return product