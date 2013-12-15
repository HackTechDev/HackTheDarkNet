# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Text


# SQLAlchemy Many-to-Many Example: http://xsnippet.org/359350/

engine = create_engine('sqlite:///darknet.db', echo = True)
Base = declarative_base()
 

user_server = Table("user_server", Base.metadata,
                        Column('user_id', Integer, ForeignKey('user.id')),
                        Column('server_id', Integer, ForeignKey('server.id'))
                    )

user_workstation = Table("user_workstation", Base.metadata,
                        Column('user_id', Integer, ForeignKey('user.id')),
                        Column('workstation_id', Integer, ForeignKey('workstation.id'))
                    )


software_security = Table("software_security", Base.metadata,
                        Column('software_id', Integer, ForeignKey('software.id')),
                        Column('security_id', Integer, ForeignKey('security.id'))
                    )

software_vulnerability = Table("software_vulnerability", Base.metadata,
                        Column('software_id', Integer, ForeignKey('software.id')),
                        Column('vulnerability_id', Integer, ForeignKey('vulnerability.id'))
                    )

operatingsystem_security = Table("operatingsystem_security", Base.metadata,
                        Column('operatingsystem_id', Integer, ForeignKey('operatingsystem.id')),
                        Column('security_id', Integer, ForeignKey('security.id'))
                    )

operatingsystem_vulnerability = Table("operatingsystem_vulnerability", Base.metadata,
                        Column('operatingsystem_id', Integer, ForeignKey('operatingsystem.id')),
                        Column('vulnerability_id', Integer, ForeignKey('vulnerability.id'))
                    )
                    

workstation_operatingsystem_software = Table("workstation_operatingsystem_software", Base.metadata,
                        Column('workstation_id', Integer, ForeignKey('workstation.id')),
                        Column('operatingsystem_id', Integer, ForeignKey('operatingsystem.id')),
                        Column('software_id', Integer, ForeignKey('software.id'))
                    )

server_operatingsystem_software = Table("server_operatingsystem_software", Base.metadata,
                        Column('server_id', Integer, ForeignKey('server.id')),
                        Column('operatingsystem_id', Integer, ForeignKey('operatingsystem.id')),
                        Column('software_id', Integer, ForeignKey('software.id'))
                    )

"""
Log
"""

class Userlog(Base):
    __tablename__ = "userlog"
            
    id = Column(Integer, primary_key=True)
    log = Column(String)  

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref=backref("userlog", order_by=id))
                                 
    def __init__(self, log):
        self.log = log

class Workstationlog(Base):
    __tablename__ = "workstationlog"
            
    id = Column(Integer, primary_key=True)
    log = Column(String)  

    workstation_id = Column(Integer, ForeignKey("workstation.id"))
    workstation = relationship("Workstation", backref=backref("workstationlog", order_by=id))
                                 
    def __init__(self, log):
        self.log = log
        
class Serverlog(Base):
    __tablename__ = "serverlog"
            
    id = Column(Integer, primary_key=True)
    log = Column(String)  

    server_id = Column(Integer, ForeignKey("server.id"))
    server = relationship("Server", backref=backref("serverlog", order_by=id))
                                 
    def __init__(self, log):
        self.log = log        
"""
A team has several hackers
"""
class Team(Base):
    __tablename__ = "team"
            
    id = Column(Integer, primary_key=True)
    name = Column(String)  
    nationality = Column(String)

    hacker_id = Column(Integer, ForeignKey("hacker.id"))
    hacker = relationship("Hacker", backref=backref("team", order_by=id))
                                 
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


"""
A user has several hacker
A user has several server
A user has severak workstation
"""
class User(Base):
    __tablename__ = "user"
 
    id = Column(Integer, primary_key=True)
    firstname = Column(String)  
    lastname = Column(String)
    email = Column(String)
    password = Column(String)
    budget = Column(Integer)

    server = relationship('Server', secondary=user_server, backref='user')
    workstation = relationship('Workstation', secondary=user_workstation, backref='workstation')

    def __init__(self, firstname, lastname, email, password, budget):
        self.firstname = firstname    
        self.lastname = lastname 
        self.email = email
        self.password = password
        self.budget = budget

"""
A hacker has one User
A hacker has one Team
"""
class Hacker(Base):
    __tablename__ = "hacker"
 
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    email = Column(String)
    password = Column(String)
 
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref=backref("hacker", order_by=id))
 
    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email= email
        self.password = password



"""
A workstation has one user or one hacker
"""
class Workstation(Base):
    __tablename__ = "workstation"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(String)
    ipaddress = Column(String)
    memory = Column(String) # Code source in memory
    harddisk = Column(String) # Code source in harddisk
    serialnumber = Column(String)
    constraint = Column(String)
        
    operatingsystem_id = Column(Integer, ForeignKey("operatingsystem.id"))

    def __init__(self, name, price, ipaddress, memory, harddisk, serialnumber, constraint):
        self.name = name
        self.price = price    
        self.ipaddress = ipaddress
        self.memory = memory
        self.harddisk = harddisk
        self.serialnumber = serialnumber
        self.constraint = constraint
        
"""
A server can have several user
A server has one operating system
"""
class Server(Base):
    __tablename__ = "server"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(String)
    ipaddress = Column(String)
    memory = Column(String)
    harddisk = Column(String)
    serialnumber = Column(String)
    constraint = Column(String)

    operatingsystem_id = Column(Integer, ForeignKey("operatingsystem.id"))

    def __init__(self, name, price, ipaddress, memory, harddisk, serialnumber, contraint):
        self.name = name
        self.price = price
        self.ipaddress = ipaddress
        self.serialnumber = serialnumber
        self.constraint = contraint

"""
A software has only one type of software
A software has several securities and vulnerabilities
"""
class Software(Base):
    __tablename__ = "software"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    price = Column(Integer)
    description = Column(String)
    sourcecode = Column(String)
    serialnumber = Column(String)
    constraint = Column(String)

    softwarecategory_id = Column(Integer, ForeignKey("softwarecategory.id"))

    def __init__(self, name, version, price, description, sourcecode, serialnumber, contraint):
        self.name = name
        self.version = version
        self.price = price
        self.description = description
        self.sourcecode = sourcecode
        self.serialnumber = serialnumber
        self.constraint = contraint

class Softwarecategory(Base):
    __tablename__ = "softwarecategory"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, name, description):
        self.name = name
        self.description = description

"""
An operating system has several securities and vulnerabilities
"""
class Operatingsystem(Base):
    __tablename__ = "operatingsystem"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    price = Column(String)
    version = Column(String)
    serialnumber = Column(String)
    constraint = Column(String)

    def __init__(self, name, price, version, serialnumber, constraint):
        self.name = name
        self.price = price
        self.version = version
        self.serialnumber = serialnumber
        self.constraint = constraint

"""        
"""     
class Security(Base):
    __tablename__ = "security"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    version = Column(String)
    description = Column(String)
    sourcecode = Column(String)    

    def __init__(self, name, version, description, sourcecode):
        self.name = name
        self.version = version
        self.description = description
        self.sourcecode = sourcecode

"""
"""         
class Vulnerability(Base):
    __tablename__ = "vulnerability"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    version = Column(String)
    description = Column(String)
    sourcecode = Column(String)  
    
    def __init__(self, name, version, description, sourcecode):
        self.name = name
        self.version = version
        self.description = description
        self.sourcecode = sourcecode 

"""
product : 
 software, hardware, server, workstation
"""
class Blackmarket(Base):
    __tablename__ = "blackmarket"

    id = Column(Integer, primary_key=True)
    productid = Column(Integer)
    name = Column(String)  
    version = Column(String)
    product = Column(String)
    availability = Column(Integer)   
    

    def __init__(self, productid, price, product, availability):
        self.productid = productid
        self.price = price
        self.product = product
        self.availability = availability
       

"""
Create database and all tables
"""
Base.metadata.create_all(engine)
