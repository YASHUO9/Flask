import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 



#giving the my file location
basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)



#Database location
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
#No track to modification 
app.config['SQLALCHEMY_TRACK_MODIFICATION']  =  False



db = SQLAlchemy(app)


Migrate(app,db)
#SQLAlchemy has been setup now
#############################################
class Puppy(db.Model):
    
    #MANUAL TABLE NAME CHOICE!
    __tablename__ = "puppies"
    
    #Unique id that i integer type
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed  = breed
        
    def __rep__(self):
        return f"Puppy {self.name} is {self.age} year/s old "
    











