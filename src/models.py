import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique= True)
    password = Column(String(100), nullable=False)
    apellido = Column(String(250), nullable= False)
    email = Column(String (100), nullable=False, unique = True)
    fecha_de_subscripción = Column(Integer,nullable=False)
    favorites = relationship('Favoritos')

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable= False, primary_key=True)
    id_favoritos = Column(Integer, ForeignKey('personajes.id'), ForeignKey('planetas.id'))
    fav_name = Column(String(250), ForeignKey('personajes.name'), ForeignKey('planetas.name'))
    fav_tema = Column(String(250), ForeignKey('personajes.__tablename__'), ForeignKey('planetas.__tablename__'))


class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
 


class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    terrain = Column(String(250))
    climate = Column(String(250))
  




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')