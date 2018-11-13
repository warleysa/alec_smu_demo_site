from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def init_db():
    db.create_all()


