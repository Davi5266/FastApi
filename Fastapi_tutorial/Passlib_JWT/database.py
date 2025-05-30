from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CONFIGURAÇÕES DO BANCO DE DADOS SQLite3

# LOCAL DO DB
DATABASE_URL = "sqlite:///./data.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Abrindo e fechando sessões com o banco
# Esta é a função usada como dependência em todos os endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()