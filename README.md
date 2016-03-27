# Main issue
1. One-to-one association does not work
2. There supposed to be a dependancy between puppy and profile table, for example, if I insert into puppy tables data for puppies that DO NOT exist in puppy table then I expect to have some error, eg: puppy not found. However in this setup I am able to insert any puppy, even if it does not exist in puppy table
3. Do not understand how to insert into association_table. Internet research suggests I should be able to use append feature but I wasn't able to make it work.
4. Current_occupancy feature works but I cannot get a good order in database_setup.py file. I have to ommit relationship line from Puppy in order to make it work.
5. Should maximum_capacity be just a INT?

# How to setup
1. Put all files in the same folder
2. Run database_setup.py => this will create a sqlite DB
3. Run puppypopulator.py => This will populate DB with dummy data
4. Run one_one_insert.py => This will populate additional tables with dummy data

# one_one_insert.py
1. The file contains both: 
    a) populate DB with dummy data
    b) test primary / foreign key dependancy between puppy and profile table
2. You need to manually comment / uncomment whichever option you require
