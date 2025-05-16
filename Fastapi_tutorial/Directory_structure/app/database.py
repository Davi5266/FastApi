from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Formato da URL:
# mysql+pymysql://usuario:senha@host:porta/nome_do_banco

DATABASE_URL = "mysql+pymysql://root:123456789@127.0.0.1:3306/vamola"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()