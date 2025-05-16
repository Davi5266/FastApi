from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.usuario import UsuarioCreate, UsuarioOut
from crud.usuario import criar_usuario, listar_usuarios

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioOut)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

@router.get("/", response_model=list[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    return listar_usuarios(db)
