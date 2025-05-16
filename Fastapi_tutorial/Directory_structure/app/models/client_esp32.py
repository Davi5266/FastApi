from sqlalchemy import Column, Integer, String
from database import Base

class Client_Esp32(Base):
    __tablename__="esp32_client"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    password = Column(String(255), index=True)