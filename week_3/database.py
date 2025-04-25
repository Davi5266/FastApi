from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

slqlite_url = "sqlite:///./usuarios.db"

engine = create_engine(slqlite_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()