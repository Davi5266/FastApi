from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str

class UsuarioOut(UsuarioCreate):
    id: int

    class Config:
        orm_mode = True
