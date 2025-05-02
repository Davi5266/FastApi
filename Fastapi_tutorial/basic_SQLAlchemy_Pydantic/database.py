#Configuração básica de um banco de dados usando o sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados SQLite
DATABASE_URL = "sqlite:///./test.db"

# Criação do engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão de banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos ORM
Base = declarative_base()
