from sqlalchemy import Column, Integer, String
from mysql_config import Base, engine

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    email = Column(String(100))

Base.metadata.create_all(bind=engine)
