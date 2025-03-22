from fastapi import FastAPI
from enum import Enum


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# definindo o valor de item_id como int
@app.get("/items02/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Criar uma Enum classe
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
# Quando se cria uma rota com uma class possuindo esses valores você limita as opções de rotas as pre definidas na class.
# Nesse caso as opções são alexnet, resnet e lenet
async def get_model(model_name: ModelName):
    # Você pode compará-lo com o membro de enumeração em sua enumeração criada ModelName:
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # Você pode obter o valor real (a strneste caso) usando model_name.value, ou em geral, your_enum_member.value:
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # Você pode retornar membros enum da sua operação de caminho , mesmo aninhados em um corpo JSON (por exemplo, a dict).

    return {"model_name": model_name, "message": "Have some residuals"}

#Parâmetros de caminho contendo caminhos
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    try:
        with open(f'{file_path}/file.txt','r') as file:
            content = file.read()
        return {"file_path": file_path, "content":content}
    except:
        return {"file_path": "Arquivo não encontrado", "info":"tente a rota files/data/"}