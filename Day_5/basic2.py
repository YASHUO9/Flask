from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired



app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):
    
    breed = StringField('What breed are you?')
    submit = SubmitField('Click Me.')

@app.route('/', methods=['GET', 'POST'])
def index2():
    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to:{session['breed']}")
        return redirect(url_for('index2'))
    
    
    return render_template('index2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

