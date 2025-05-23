from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate

def criar_usuario(db: Session, usuario: UsuarioCreate):
    novo = Usuario(nome=usuario.nome, email=usuario.email)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_usuarios(db: Session):
    return db.query(Usuario).all()
