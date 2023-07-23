#currently in complete



import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = "1"

#These os import help to run the program locally
##################################################################################################
from flask import Flask ,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint,google

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"

blueprint = make_google_blueprint(client_id="848622301932-gop1egoi9ucaf5kqq4mba21782muhts9.apps.googleusercontent.com", client_secret= "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",offline=True,scope=['profile','email'])

app.register_blueprint(blueprint,url_prefix = "/login")


#Home page
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/welcome')
def welcome():
    #RETURN ERROR INTERNAL SEVER ERROR IF NOT LOGGED IN !!
    resp = google.get('/oauth2/v1/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    
    return render_template('welcome.html',email = email)


# if __name__ == "__main__":
#      app.run(debug=True ,use_reloader=False) 
@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))

    resp = google.get('/oath2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    
    return render_template('welcome.html',email = email)

if __name__ == "__main__":
    app.run()
    
    




    
    
    
    
    
    
    
    
    
    
    
    