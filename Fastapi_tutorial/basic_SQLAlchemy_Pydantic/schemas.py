from pydantic import BaseModel

# Schema para entrada de dados (POST/PUT)
class UserCreate(BaseModel):
    name: str
    email: str

# Schema para resposta (GET)
class User(BaseModel):
    id: int
    name: str
    email: str

class Config:
    orm_mode = True # Permite conversão de SQLAlchemy para Pydantic

    