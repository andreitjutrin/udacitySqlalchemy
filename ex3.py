from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Puppy, Shelter, Profile
import datetime
from sqlalchemy.sql import func

# an Engine, which the Session will use for connection
# resources
engine = create_engine('sqlite:///puppies.db', echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# work with sess
# myobject = MyObject('foo', 'bar')
def queryOne():
	q = session.query(Puppy).order_by(Puppy.name.asc())
	for row in q:
		print row.name

today = datetime.date.today()
six_months_ago = today - datetime.timedelta(days = 120)

def queryTwo():
	q = session.query(Puppy).filter(and_(Puppy.dateOfBirth <= today, \
		Puppy.dateOfBirth >= six_months_ago)).order_by(Puppy.dateOfBirth.asc())
	for row in q:
		print row.name, row.dateOfBirth

def queryThree():
	q = session.query(Puppy).order_by(Puppy.weight.asc())
	for row in q:
		print row.name, row.weight

def queryFour():
	q = session.query( \
		Puppy, \
		func.count(Puppy.name).label('TOTAL PUPPYS')). \
		join(Shelter).group_by(Shelter.name).all()
	
	for row in q:
		print row[0].name, row[1]

########### Below are non tasks query, this is for tests only ##########

def queryFive():
	q = session.query(Profile).all()
	
	for row in q:
		print row.id, row.description, row.specialNeeds, row.puppy_id 

# def queryFive():
# 	q = session.query(Puppy, Profile).join(Profile).all()

# 	for row in q:
# 		print row

queryFive()

