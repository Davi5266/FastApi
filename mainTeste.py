from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ListOption(str, Enum):
    user = "user"
    department = "department"
    account = "account"

# Rotas alternadas
@app.get("/{list_option}/list")
async def generic_list(list_option: ListOption): # limita as opções de busca em user, department e account
    #Modelo-01 Sem o limitador de buscas
    # if list_option == "user":
    #     data = ["Jim","Pam","Dwight"]
    # elif list_option == "department":
    #     data = ["Sales","Management", "IT"]
    # elif list_option == "account":
    #     data = [234,23423,654654,4326543654]

    # Modelo-02 Com o limitador de buscas
    if list_option == ListOption.user:
        data = ["Jim","Pam","Dwight"]
    elif list_option == ListOption.department:
        data = ["Sales","Management", "IT"]
    elif list_option == ListOption.account:
        data = [234,23423,654654,4326543654]


    return {list_option:data}

# definição de uma rota
@app.get("/teste")
# Função assicrona
async def hello():
    return {"message":"Hello World!"}


@app.get("/user/list")
async def user_list():
    return {"users":["Jim", "pam", "dwight","Stanle"]}

# Rota dinamica
@app.get("/user/{username}")
async def user_profile(username: str):
    return {"data": username}

@app.get("/account/list")
async def account_list():
    return {"acconut":[1234,843432,43278439,413,23421423,2342143]}

@app.get("/account/{number}")
async def accounut_detail(number: int):
    return {"account": number}

@app.get("/import/{filepath:path}")
async def import_file(filepath: str):
    return {"importing": filepath}

# @app.post()   # Create
# @app.get()    # Read
# @app.put()    # Update  
# @app.delete() # Delete