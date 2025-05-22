from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
import models, crud
from schemas import CreateUser, User, CreateProduct, Product, Token, LoginData
from security import verify_password, create_access_token, get_current_user

# Criando tabelas definidas em models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Definição de endpoints 

# Rota de teste que retorna todos os usários do banco de dados
@app.get("/")
def helloworld(db: Session = Depends(get_db)):
    return {
        "users":crud.get_users(db),
        "products":crud.get_products(db)
        }

# Registra um usuário ao banco de dados
@app.post("/users/", response_model=User)
async def create_user(user_data: CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(db,user_data)

# Pega um usário com base no seu ID
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

# Modifica um usário com base no seu ID
@app.put("/users/{user_id}",response_model=User)
async def update_user(user_id:int,name:str,dt_nasc:str,email:str,tel:str,db: Session = Depends(get_db)):
    return crud.update_user(db,user_id, name, dt_nasc,email,tel)

# deleta um usuário com base no seu ID
@app.delete("/users/{user_id}",response_model=User)
async def delete_user(user_id:int,db: Session = Depends(get_db)):
    return crud.delete_user(db,user_id)

# Rota de autenticação
@app.post("/login", response_model=Token)
# async def login_user(login_data: LoginData, db: Session = Depends(get_db)):
#     user = crud.get_user_by_email(db, login_data.email)
#     if not user or not verify_password(login_data.password, user.password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Credenciais inválidas"
#         )
#     access_token = create_access_token(data={"sub":user.email})
#     return {"access_token": access_token, "token_type":"bearer"}

# para que o modelo de autenticação funcione é utilizado o OAuth2PasswordRequestForm, ele espera por username(email) e password como formulário. Nesse caso o username é um email
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
async def read_logged_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }

# Rotas de produtos

# products
# registra um produto no sistema
@app.post("/products/", response_model=Product)
async def create_product(product_data: CreateProduct, db: Session = Depends(get_db)):
    return crud.create_product(db,product_data)

# pega um produto com base no seu ID
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db,product_id)

# atualiza um produto com base no seu ID
@app.put("/produts/{product_id}", response_model=Product)
async def update_product(product_id:int,name:str,type: str,value: int, desc: str, db: Session = Depends(get_db)):
    return crud.update_product(db,product_id,name,type,value,desc)
# deleta um produto com base no seu ID
@app.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db,product_id)