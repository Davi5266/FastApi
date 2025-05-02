from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models, crud

# Cria as tabelas definidas em models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência que cria uma sessão e fecha após o uso
# garantindo o uso de sessões individuais
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Banco configurado com sucesso!"}

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name, email)

# pega todos os usuários do DB SQLite3
@app.get("/users_1/")
def read_users_1(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Pega o usuário de acordo com o seu id
@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user:
        return user
    return {"error": "Usuário não encontrado"}

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, name, email)
    if user:
        return user
    return {"error": "Usuário não encontrado"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if user:
        return {"message": f"Usuário {user.name} deletado"}
    return {"error": "Usuário não encontrado"}
