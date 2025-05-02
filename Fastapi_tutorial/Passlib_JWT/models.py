from sqlalchemy import Column, Integer, String
from database import Base
from typing import Union

# Definindo tabela users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dt_nasc = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    tel = Column(String,index=True)
    password = Column(String)

# Definindo tabela product
class Product(Base):
    __tablename__="product"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    value = Column(Integer, index=True)
    desc = Column(String, index=True, insert_default=True)
