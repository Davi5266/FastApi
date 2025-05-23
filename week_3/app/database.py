from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Formato da URL:
# mysql+pymysql://usuario:senha@host:porta/nome_do_banco

USER = os.getenv("USER_DB")
PASSWORD = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
DB_NAME = os.getenv("DB_NAME")

# print(USER)

# DATABASE_URL = "mysql+pymysql://root:123456789@127.0.0.1:3306/vamola"

DATABASE_URL = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST_DB}:3306/{DB_NAME}'
print(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()