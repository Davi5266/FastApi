from fastapi import APIRouter, Depends
from crud.crud_user import create_user, get_user
from schemas.schemas_user import User, CreateUser
from sqlalchemy.orm import Session
from db.DB_config import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def testUser():
    print("ok")
    return

@router.post("/create", response_model=User)
async def create_data_user(user_data:CreateUser, db: Session = Depends(get_db)):
    return create_user(db, user_data)