from sqlalchemy import create_engine
from random import randint
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy, Profile, Adopter, association_table
from random import randint
import datetime
import random
import string


# an Engine, which the Session will use for connection
# resources
engine = create_engine('sqlite:///puppies.db', echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

############### Test occupancy ####################

def queryOne():
	q = session.query(Shelter).all()
	for row in q:
		print row.name, "|", row.city, "|", row.current_occupancy

queryOne()