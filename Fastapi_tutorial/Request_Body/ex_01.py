#https://fastapi.tiangolo.com/tutorial/body/
from fastapi import FastAPI
from pydantic import BaseModel


#Declarando seu modelo de dados como uma classe que herda do .BaseModel
class Item(BaseModel):
    name: str
    #Esse valor pode ser nulo
    description: str | None = None
    price: float
    #Esse valor pode ser nulo
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

#Versão variante para montar um modelo de dados
from typing import Union

class Item_02(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post("/variantesitems/")
async def create_variante_item(item: Item):
    return item

@app.post("/itemss/")
async def create_items(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


class TestModel(BaseModel):
    name: str
    age: int
    height: Union[int,float]
    


@app.put("/sla/{sla_id}")
async def teste_sla(sla_id: int , test_model: TestModel ,q: str | None = None):
    if q is not None:
        return {
            "querry":q,
            "Model_user":test_model,
            "user_id":sla_id
        }
    
    return {
            "Model_user":test_model,
            "user_id":sla_id
        }