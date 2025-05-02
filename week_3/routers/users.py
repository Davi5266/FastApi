from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Exemplo básico de rotas em fastapi
@router.get("/")
async def listar_usuarios():
    return[{"id":1,"nome":"João"},{"id":2,"nome":"Maria"}]

@router.post("/")
async def criar_usuario(user:dict):
    return {"msg":"Usuário criado","user":user}

# Rotas com sqlite3
@router.post("/create", response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/create", response_model=list[schemas.UserOut])
async def list_user(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# users
@router.post("/users/", response_model=User)
def create_user(user_data: CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(db,user_data)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@router.put("/users/{user_id}",response_model=User)
def update_user(user_id:int,name:str,dt_nasc:str,email:str,tel:str,db: Session = Depends(get_db)):
    return crud.update_user(db,user_id, name, dt_nasc,email,tel)

@router.delete("/users/{user_id}",response_model=User)
async def delete_user(user_id:int,db: Session = Depends(get_db)):
    return crud.delete_user(db,user_id)
