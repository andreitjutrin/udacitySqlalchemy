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

# def queryFive():
# 	q = session.query(Puppy).all()
	
# 	puppyId = []
# 	for row in q:
# 		puppyId.append(row.id)
# 	return puppyId

# for i,x in enumerate(queryFive()):
# 	chars1 = "".join( [random.choice(string.letters) for i in xrange(15)] )
# 	chars2 = "".join( [random.choice(string.letters) for i in xrange(15)] )
# 	new_profile = Profile(description = chars1, specialNeeds = chars2, puppy_id = x)
# 	session.add(new_profile)
# 	session.commit()

############### Test one-to-one association ####################

puppyId = [5,101,206]

for i,x in enumerate(puppyId):
	chars1 = "".join( [random.choice(string.letters) for i in xrange(15)] )
	chars2 = "".join( [random.choice(string.letters) for i in xrange(15)] )
	new_profile = Profile(description = chars1, specialNeeds = chars2, puppy_id = x)
	session.add(new_profile)
	session.commit()

