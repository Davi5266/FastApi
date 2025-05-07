from pydantic import BaseModel
from typing import Union

#MODELOS DE DADOS USADO EM REQUISIÇÕES

# Modelo base para a criação de usuário (POST/PUT)
class CreateUser(BaseModel):
    name: str
    dt_nasc: int
    email: str
    tel: str
    password: str

# Schema para resposta (GET)
class User(BaseModel):
    id: int
    name: str
    dt_nasc: str
    email: str
    tel: str

# MODELO DE PRODUTOS
class CreateProduct(BaseModel):
    name: str
    type: str
    value: Union[int, float]
    desc: Union[str, None] = None

class Product(BaseModel):
    id: int
    name: str
    type: str
    value: Union[int, float]
    desc: Union[str, None] = None

#Token config
class Token(BaseModel):
    access_token: str
    token_type: str

# MODELO DE LOGIN
class LoginData(BaseModel):
    email: str
    password: str

class Config:
    orm_mode = True

class Esp32(BaseModel):
    user: str