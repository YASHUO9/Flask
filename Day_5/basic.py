from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                     RadioField,SelectField,TextAreaField,TextField,
                     SelectField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    
    breed = StringField("What breed are you ?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered ?")
    mood = RadioField("Please choose your mood:",choices=[('mood_one','Happy'),('mood_two',"chill"),('mood_three',"romantic")])
    food_choice = SelectField(u'Pick your Favorite food:',choices = [('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')
    
    
@app.route('/',methods = ['GET','POST']) #HERE I HAVE USED BOTH BECAUSE I AM DATA SOME DATA TO MY TEMPLATES

def index():
    
    form = InfoForm()
    if form.validate_on_submit():
        """Here i am checking the value has been put or not"""
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
       
        return  redirect(url_for('thankyou'))
        #redirect is having the value and using the 'thankyou' function
        
    return render_template('index.html',form = form)
         

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__=='__main__':
    app.run(debug=True)


















