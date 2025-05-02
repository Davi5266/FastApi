from pydantic import BaseModel
from typing import Union

# Modelo base para a criação de usuário (POST/PUT)
class CreateUser(BaseModel):
    name: str
    dt_nasc: int
    email: str
    tel: str

# Schema para resposta (GET)
class User(BaseModel):
    id: int
    name: str
    dt_nasc: str
    email: str
    tel: str

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


class Config:
    orm_mode = True