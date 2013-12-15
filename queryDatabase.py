from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDatabase import *
from populateDatabase import * 

# http://www.blog.pythonlibrary.org/2012/07/01/a-simple-sqlalchemy-0-7-0-8-tutorial/
# http://plone.shenton.org/tech/databases/sqlalchemy-many-to-many-relations

engine = create_engine('sqlite:///darknet.db', echo = True)
 
Session = sessionmaker(bind = engine)
session = Session()
 
"""
res = session.query(User).all()
for user in res:
    print user.firstname + " " + user.lastname
"""

"""
qry = session.query(User, Hacker)
qry = qry.filter(User.id == Hacker.user_id)
"""

"""
user, hacker = qry.filter(Hacker.nickname == "SolomonKane").first()
print user.firstname + " " + user.lastname + " = " + hacker.nickname
"""

"""
for server in new_user.server:
    print server.name + " " + server.ipaddress
"""


print server1.user[0].firstname + " " + server1.user[0].lastname
