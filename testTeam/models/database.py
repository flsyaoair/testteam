# -*- coding: UTF-8 -*- 

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from testTeam.testteamconfig import DB, DEBUG

engine = create_engine(DB,echo=DEBUG)

BaseModel = declarative_base()

def get_session():
    return Session(bind = engine)

def drop_database():
    BaseModel.metadata.drop_all(bind=engine)

def create_database():
    BaseModel.metadata.create_all(bind=engine)