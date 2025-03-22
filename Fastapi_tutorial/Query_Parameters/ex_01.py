# Parâmetros de consulta
# Quando você declara outros parâmetros de função que não fazem parte dos parâmetros de caminho, eles são automaticamente interpretados como parâmetros de "consulta".

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

print("https://fastapi.tiangolo.com/tutorial/query-params/")
print("\n")

@app.get("/items/")
#link para testar a rota
# http://127.0.0.1:8000/items/?skip=0&limit=10
async def read_item(skip: int = 0, limit: int = 10): # Esse valor é padrão na rota, ou seja skip = 0 e limit = 10
    print("skip ",skip)
    print("limit ", limit)
    return fake_items_db[skip : skip + limit]

#Parâmetros opcionais
@app.get("/items/{item_id}")
#Da mesma forma, você pode declarar parâmetros de consulta opcionais, definindo o padrão como None:
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#Opção variavel 
from typing import Union

@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Conversão de tipo de parâmetro de consulta
# https://fastapi.tiangolo.com/tutorial/query-params/#query-parameter-type-conversion
@app.get("/items/{item_id}")
#Você também pode declarar bool tipos, e eles serão convertidos:
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Vários parâmetros de caminho e consulta
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Parâmetros de consulta obrigatórios
@app.get("/user_items/{item_id}")
#Como needyé um parâmetro obrigatório, você precisa defini-lo na URL:
# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

#você pode definir alguns parâmetros conforme necessário, alguns como tendo um valor padrão e alguns totalmente opcionais:
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_items(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item