from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import Column,Integer,String


engine=create_engine("sqlite:///taskmanager.db",echo=True)

SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import Column,Integer,String


engine=create_engine("sqlite:///taskmanager.db",echo=True)

SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass



