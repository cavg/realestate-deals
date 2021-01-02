from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
import datetime

from property import settings


DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_items_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)



class Items(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "items"

    title = Column('title', String(50))
    link = Column('link', String(255),primary_key=True, nullable=False)
    price = Column('price', Integer, nullable=False)
    address = Column('address', String(50))
    code = Column('code', String(50))
    location = Column('location', String(50))
    operation = Column('operation', String(50))
    _type = Column('type', String(25), nullable=False)
    date = Column('date', String(25))
    thumb = Column('thumb', String(255))
    site = Column('site', String(25), primary_key=True)
    creation_date = Column('creation_date', DateTime, default=datetime.datetime.utcnow)