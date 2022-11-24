#from . import db 

#class Movie(db.Model):
   # id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.Strings(50))
    #rating = db.Column(db.Integer)

from sqlalchemy import Column , String , Integer
from db import Base,engine
from sqlalchemy.schema import ForeignKey

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,autoincrement=True, primary_key=True)
    username = Column(String(70),unique=True)
    password = Column(String(70))
    first_name = Column(String(70))
    last_name = Column(String(70))
    email = Column(String(70))
    phone = Column(String(70))

class Movies(Base):
    __tablename__= 'movies'
    id = Column(Integer,autoincrement=True, primary_key=True)
    movie_title = Column(String(70),unique=True)
    rated = Column(String(70))
    poster_url = Column(String(70))
    

Base.metadata.create_all(engine)
