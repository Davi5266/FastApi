from fastapi import APIRouter

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