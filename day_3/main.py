from fastapi import FastAPI

from indb import generate_products, generate_products_v2

from product import Product

import json_db

app = FastAPI()

products = generate_products()

products_v2 = generate_products_v2()

productDB = json_db.jsonDB(path='./data/products.json')

@app.get("/")
async def get_products():
    return {"products": products}

@app.get("/readfiles")
async def read_products():
    return {"products":products_v2}

@app.post("/readfiles")
async def create_products(product: Product):
    # return {"products":products_v2}
    print(product)
    return {"products": product}

@app.get("/productclass")
async def class_product():
    products_class = productDB.read()
    return {"product":products_class} 