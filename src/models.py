import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(250))

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    people = relationship("People", backref="favorites")
    planet = relationship("Planet", backref="favorites")
    usuario = relationship("Usuario", backref="favorites")

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(250), nullable=False, unique=True)
    nombre = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
    correo_electronico = Column(String(250), nullable=False, unique=True)
    favorites = relationship("Favorites", backref="usuario")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
