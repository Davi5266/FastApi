from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models, crud
from schemas import CreateUser, User, CreateProduct, Product

# Criando tabelas definidas em models
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Abrindo e fechando sessões com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def helloworld(db: Session = Depends(get_db)):
    return {
        "users":crud.get_users(db),
        "products":crud.get_products(db)
        }
# users
@app.post("/users/", response_model=User)
def create_user(user_data: CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(db,user_data)

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.put("/users/{user_id}",response_model=User)
def update_user(user_id:int,name:str,dt_nasc:str,email:str,tel:str,db: Session = Depends(get_db)):
    return crud.update_user(db,user_id, name, dt_nasc,email,tel)

@app.delete("/users/{user_id}",response_model=User)
async def delete_user(user_id:int,db: Session = Depends(get_db)):
    return crud.delete_user(db,user_id)

# products
@app.post("/products/", response_model=Product)
def create_product(product_data: CreateProduct, db: Session = Depends(get_db)):
    return crud.create_product(db,product_data)

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db,product_id)

@app.put("/produts/{product_id}", response_model=Product)
def update_product(product_id:int,name:str,type: str,value: int, desc: str, db: Session = Depends(get_db)):
    return crud.update_product(db,product_id,name,type,value,desc)

@app.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db,product_id)