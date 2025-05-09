from sqlalchemy.orm import Session

from db.DB_config import engine
from db.models.User import User
from schemas.schemas_user import CreateUser

# Base.metadata.create_all(bind=engine)
# Base.metadata.create_all(tables=[User], bind= engine)

def create_user(db: Session, user_data: CreateUser):
    user = User(name = user_data.name, email = user_data.email, password = user_data.password)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: id):
    return db.query().filter(User.id == user_id).first()