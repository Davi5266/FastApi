from product import Product
import json

def generate_products():
    list_products = []

    for i in range(10):
        p = Product(name = f"Product {i + 1}", price= i * 2)
        list_products.append(p)

    return list_products

def generate_products_v2():
    f = open('./data/products.json')
    data = json.loads(f.read())
    f.close()
    return data