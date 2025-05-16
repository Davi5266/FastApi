from pydantic import BaseModel

class CreateClient(BaseModel):
    name: str
    password: str

class Client(BaseModel):
    id: int
    name: str
    password: str

    class Config:
        orm_mode = True