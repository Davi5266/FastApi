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

#Token config
class Token(BaseModel):
    access_token: str
    token_type: str