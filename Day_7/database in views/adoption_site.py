#currently incomplete i do not have made the table yet in the data base;
# The comment are:
#1.set FLASK_APP = file_name.py
#2.flask db init
#3.flask db migrate -m "initial migration"
#4. flask db upgrade




#adoption_site.py
import os
from forms import AddForm ,DelForm,AddOwnerForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = "MYSECRET"


####################################
####### SQL DATABASE SECTION #######
####################################
 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,"dat.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)



##################################
##### MODEL ######################
##################################

class Puppy(db.Model):
    
    __tablename__ = "puppies"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref = 'puppy',uselist = False)
    
    def __init__(self,name):
        self.name = name
    
    def __rep__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name: {self.name} and has no owner yet!"
    
    
class Owner(db.Model):
    
    __tablename__ = "owners"
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))
    
    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
        
    def __repr__(self):
        return f"Owner Name: {self.name}"
    
     
    
    
    
    
    
    
    
##########################################
########### VIEW FUNCTION -- HAVE FORMS ##
##########################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_owner',methods =["GET","POST"] )
def add_owner():
    
    form = AddOwnerForm()
     
    if form.validate_on_submit():
        name = form.name.date
        pup_id = form.pup_id.data
        
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()
    

@app.route("/add",methods=["GET","POST"])
def add_pup():
    
    form = AddForm()
    
    if  form.validate_on_submit():
        name = form.name.data
        
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        
        return redirect(url_for("list_pup"))
    
    return render_template('add.html',form = form)
    
    
@app.route('/list')
def list_pup():
    
    puppies = Puppy.query.all()
    return render_template('list.html', puppies  = puppies)

@app.route("/delete",methods=['GET','POST'])
def del_pup():
    
    form = DelForm()
    
    if form.validate_on_submit():
        
        id  = form.id.data   
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        
        return redirect(url_for('list_pup'))
    return render_template('delete.html',form = form)

if __name__ == "__main__":
    app.run(debug=True)   