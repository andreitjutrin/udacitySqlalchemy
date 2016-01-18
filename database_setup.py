import os
import sys
from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(10), nullable=False)
    zipCode = Column(String(10), nullable=False)
    website = Column(String(40), nullable=False)
    id = Column(Integer, primary_key=True)

class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    dateOfBirth = Column(Date)
    gender = Column(Enum('M', 'F'), nullable=False)
    weight = Column(Float, nullable=False)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship('Shelter')
    profile = relationship('Profile', uselist=False, back_populates="puppy")

class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    photo = Column(String)
    description = Column(String(250))
    specialNeeds = Column(String(250))
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship('Puppy', back_populates='profile')

engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
