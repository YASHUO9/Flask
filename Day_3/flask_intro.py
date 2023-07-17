from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello Puppy!</h1>"
@app.route('/info')
def new():
    return "<h1>Hello  Yash!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    Name = name.upper()
    return f'<h1>Upper case:{Name[100]}</h1>'



if __name__ =='__main__':
    app.run(debug=True)