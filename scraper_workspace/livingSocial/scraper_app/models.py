from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settings

DeclarativeBase = declarative_base()

def db_connect() :
    """
    Performs database connection on the basis of settings in settings.py
    Returns splachemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine) :
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase) :
    """SqlAlchemy deals model"""

    __tablename__ = "deals"

    id  = Column(Integer, primary_key=True)
    title = Column('title',String)
    link = Column('link', String, nullable=True)
    location = Column("location", String, nullable=True)
    original_price = Column("original_price", Integer, nullable=True)
    price = Column("price",Integer, nullable=True)
    end_date = Column("end_datae", DateTime, nullable=True)
