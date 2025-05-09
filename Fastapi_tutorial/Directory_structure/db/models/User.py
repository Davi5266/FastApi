from sqlalchemy import Column, Integer, String
# from ..DB_config import Base, engine
from ..engine import engine

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, index=True)
#     password = Column(String, index=True)

from sqlmodel import Field, Session, create_engine, select, SQLModel

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    password: str = Field(index=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

print("ok")