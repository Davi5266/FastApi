from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models, crud
from schemas import UserCreate, User

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

@app.post("/users/", response_model=User)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user_data)

@app.get("/users/", response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)
