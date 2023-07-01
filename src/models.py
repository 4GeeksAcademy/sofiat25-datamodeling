import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ =   "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute. 
    customerID =Column(Integer, primary_key=True)
    UserName = Column(String(250), nullable=False)
    Password =Column(String(250), nullable=False)

class Character (Base):
    __tablename__ = "character"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    charID =Column(Integer, primary_key=True)
    name= Column (Integer,primary_key=True)
    birth_date= Column(String(250), nullable=False)
    height= Column (Integer, primary_key=True)
    hair_color= Column(String(250), nullable=False)
    eye_color= Column(String(250), nullable=False)
    gender= Column(String(250), nullable=False)

class Planets (Base):
    __tablename__ = "planets"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planetID =Column(Integer, primary_key=True)
    name= Column (Integer, primary_key=True)
    population= Column(String(250), nullable=False)
    diameter= Column (Integer, primary_key=True)
    climate= Column(String(250), nullable=False)
    terrain= Column(String(250), nullable=False)

class Ships (Base):
    __tablename__ = "ships"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    shipID = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    max_speed = Column(Integer, primary_key=True)
    passengers = Column(Integer, primary_key=True)
    starship_class = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = "favoritos"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favID= Column(Integer, primary_key= True)
    customerID= Column(Integer,  ForeignKey("user.id"))
    planetID = Column(Integer, ForeignKey("planets.id"))
    charID = Column(Integer, ForeignKey("character.id"))
    shipID = Column(Integer, ForeignKey("ships.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
