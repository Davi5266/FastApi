from sqlalchemy import Column, Integer, String, Float
from database import Base

class Client_Esp32(Base):
    __tablename__="esp32_client"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    password = Column(String(255), index=True)
    

class Temperature(Base):
    __tablename__="temperature"
    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(String(55), index=True)
    humidade = Column(Float, index=True)
    temperature_C = Column(Float, index=True)
    temperature_F = Column(Float, index=True)
    
    