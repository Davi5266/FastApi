from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    # user: str
    temperature: float

class Esp32(BaseModel):
    sla: str

@app.post("/")
async def test(user: User):
    # print(user.user)
    print(user.temperature)
    dados = "megaman"
    print(dados)
    return {"message":"sucesso"}