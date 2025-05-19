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

# Temperature
class RegisterTemperature(BaseModel):
    data_hora: str
    humidade: float
    temperature_C: float
    temperature_F: float

class Temperature_s(BaseModel):
    id: int
    data_hora: str
    humidade: float
    temperature_C: float
    temperature_F: float