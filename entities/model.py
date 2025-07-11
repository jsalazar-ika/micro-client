from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

class Client(BASE):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    address = Column(String(length=150))
    email = Column(String(length=150))
