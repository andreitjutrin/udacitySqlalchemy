import os
import sys
from sqlalchemy import Table, Column, Date, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, column_property
from sqlalchemy import create_engine
from sqlalchemy import select, func

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('adopter_id', Integer, ForeignKey('adopter.id')),
    Column('puppy_id', Integer, ForeignKey('puppy.id'))
)

class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    dateOfBirth = Column(Date)
    gender = Column(String(6), nullable=False)
    weight = Column(Float, nullable=False)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    # shelter = relationship(Shelter)
    profile = relationship('Profile', uselist=False, back_populates="puppy")
    adopters = relationship("Adopter", secondary=association_table,
        back_populates="puppies")

class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(20), nullable=False)
    zipCode = Column(String(10), nullable=False)
    website = Column(String, nullable=False)
    maximum_capacity = Column(String)

    current_occupancy = column_property(
        select([func.count(Puppy.id)]).\
        where(Puppy.shelter_id==id).\
        correlate_except(Puppy)
        )


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    photo = Column(String)
    description = Column(String(250))
    specialNeeds = Column(String(250))
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship('Puppy', back_populates='profile')

class Adopter(Base):
    __tablename__ = 'adopter'

    name = Column(String(50), nullable=False)
    id = Column(Integer, primary_key=True)
    puppies = relationship("Puppy", secondary=association_table,
        back_populates="adopters")

engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
