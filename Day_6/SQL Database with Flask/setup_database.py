from basic import db,Puppy


#Creste All The TABLE Model --->> Db Table
db.create_all()


sam = Puppy('Sammy',3)
frank = Puppy('mono',6)




#None
#None 
print(sam.id,frank.id)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)












