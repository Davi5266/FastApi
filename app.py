from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user: str

@app.post("/")
async def test(user: User):
    print(user.user)
    dados = "megaman"
    print(dados)
    return {"mensage": dados}