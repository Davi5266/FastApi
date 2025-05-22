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
    # data_hora: str | None | int
    humidade: float | None | int
    temperature_C: float | None | int
    temperature_F: float | None | int

class Temperature_s(BaseModel):
    id: int | None
    data_hora: str | None
    humidade: float | None
    temperature_C: float | None
    temperature_F: float | None