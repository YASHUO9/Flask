#Basic.py
#Create Entries into the tables!
from main import db,Puppy,Owner,Toy

#Creating 2 Puppies
rufus = Puppy('Rufus')
fido  = Puppy('Fido')


#ADD PUPPIES TO DB 
db.session.add_all([rufus,fido])
db.session.commit()

#Check !
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
#CREATE OWNER OBJECT
jose = Owner('Jose',rufus.id)

#Give Rufus same toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

#GRAB RUFUS AFTER THOSE ADDITIONS!
rufus = Puppy.query.filter_by(name = "Rufus").first()
print(rufus)

print(rufus.report_toys())