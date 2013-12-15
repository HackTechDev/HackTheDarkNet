import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDatabase import *

engine = create_engine('sqlite:///darknet.db', echo = True)

Session = sessionmaker(bind=engine)
session = Session()

user0 = User("Sam", "Gond", "saml.gond@hackthedark.net", "sgp@55w0rd", 1000)
user1 = User("Bruce", "Wayne", "bruce.wayne@hackthedark.net", "gpp@55w0rd", 1000)
user2 = User("Steve", "Austin", "steve.ausitin@hackthedark.net", "nsp@55w0rd", 1000)

session.add(user0)
session.add(user1)
session.add(user2)


hacker0 = Hacker("LeSanglier", "lesanglier@hackthedark.net", "pass")
hacker1 = Hacker("Nekrofage", "nekrofage@hackthedark.net", "pass")
hacker2 = Hacker("batman", "batman@hackthedark.net", "pass")
hacker3 = Hacker("superman", "superman@hackthedark.net", "pass")
hacker4 = Hacker("madmaw", "madmax@hackthedark.net", "pass")
hacker5 = Hacker("arrow", "arrow@hackthedark.net", "pass")


hacker0.user = user0
hacker1.user = user0

hacker2.user = user1
hacker3.user = user1

hacker4.user = user2
hacker5.user = user2

workstation0 = Workstation("Sun Alpha", 400, "192.168.1.1", "if()", "else()", "equal()", "not equal")
workstation1 = Workstation("SGI Fuel", 400, "192.168.1.2", "if()", "else()", "equal()", "not equal")
workstation2 = Workstation("VaxVMS", 400, "192.168.1.2", "if()", "else()", "equal()", "not equal")


session.add(workstation0)
session.add(workstation1)
session.add(workstation2)

server0 = Server("Opteron", 400, "192.168.2.1", "if()", "else()", "equal()", "not equal")
server1 = Server("Atom", 400, "192.168.3.2", "if()", "else()", "equal()", "not equal")
server2 = Server("Cray", 400, "192.168.4.2", "if()", "else()", "equal()", "not equal")


session.add(server0)
session.add(server1)
session.add(server2)


softwarecategory1 = Softwarecategory("Virus", "")
softwarecategory2 = Softwarecategory("Antivirus", "")
softwarecategory3 = Softwarecategory("Firewall", "")
softwarecategory4 = Softwarecategory("Secure shell", "")
softwarecategory5 = Softwarecategory("No-secure shell", "")
softwarecategory6 = Softwarecategory("Load balancer", "")
softwarecategory7 = Softwarecategory("Mail", "")
softwarecategory8 = Softwarecategory("Password Cracker", "Crack password, method is brute force")
softwarecategory9 = Softwarecategory("Ping", "")
softwarecategory10 = Softwarecategory("Database", "")

session.add(softwarecategory1)
session.add(softwarecategory1)
session.add(softwarecategory2)
session.add(softwarecategory3)
session.add(softwarecategory4)
session.add(softwarecategory5)     
session.add(softwarecategory6)
session.add(softwarecategory7)
session.add(softwarecategory8)
session.add(softwarecategory9)
session.add(softwarecategory10)


software0 = Software("BackOrifice", "0.0.3a", 100, "Troyan", "code", "sn3234KSDFO", "contraint")
software0.softwarecategory_id = 1
software1 = Software("Panda", "6.6.3a", 100, "Troyan", "code", "sn3234KSDFO", "contraint")
software1.softwarecategory_id = 2
software2 = Software("JackTheRipper", "0.0.3a", 100, "Troyan", "code", "sn3234KSDFO", "contraint")
software2.softwarecategory_id = 8
software3 = Software("Zombi", "6.6.3a", 100, "Troyan", "code", "sn3234KSDFO", "contraint")
software3.softwarecategory_id = 1


session.add(software0)
session.add(software1)
session.add(software2)
session.add(software3)



operatingsystem1 = Operatingsystem("Ubuntu", "13.10", 0, "", "")
operatingsystem2 = Operatingsystem("Debian", "7.0", 0, "", "")
operatingsystem3 = Operatingsystem("Windows", "8.0", 0, "", "")
operatingsystem4 = Operatingsystem("MacOs", "Mountain", 0, "", "")

session.add(operatingsystem1)
session.add(operatingsystem2)
session.add(operatingsystem3)
session.add(operatingsystem4)

security1 = Security("Firewall", "0.1", "Firewall", "")
security2 = Security("Strong password", "0.1", "Firewall", "")
security3 = Security("Disable root access", "0.1", "Firewall", "")
security4 = Security("Firewall", "0.1", "Firewall", "")

session.add(security1)
session.add(security2)
session.add(security3)
session.add(security4)


vulnerability1 = Vulnerability( "Backdoor", "0.1", "Backdoor", "")
vulnerability2 = Vulnerability( "Easy password", "0.1", "Backdoor", "")
vulnerability3 = Vulnerability( "No password", "0.1", "Backdoor", "")
vulnerability4 = Vulnerability( "Root access enable", "0.1", "Backdoor", "")

session.add(vulnerability1)
session.add(vulnerability2)
session.add(vulnerability3)
session.add(vulnerability4)

"""
user_server
user_workstation
software_security
software_vulnerability
operatingsystem_security
operatingsystem_vulnerability
workstation_operatingsystem_software
server_operatingsystem_software
"""

session.commit()

