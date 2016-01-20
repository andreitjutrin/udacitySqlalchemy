from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy, Profile
from random import randint
import datetime
import random
import string


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

############### Insert into table Profiles ####################

chars = "".join( [random.choice(string.letters) for i in xrange(15)] )

def queryFive():
	q = session.query(Puppy).all()
	
	puppyId = []
	for row in q:
		puppyId.append(row.id)
	return puppyId

for i,x in enumerate(queryFive()):
	new_profile = Profile(description = chars, specialNeeds = chars, puppy_id = x)
	session.add(new_profile)
	session.commit()

############### Test one-to-one association ####################

# puppyId = [5,101,206]

# for i,x in enumerate(puppyId):
# 	new_profile = Profile(description = chars, specialNeeds = chars, puppy_id = x)
# 	session.add(new_profile)
# 	session.commit()

