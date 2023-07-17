from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!'

@app.route('/puppy/<name>')

def puppy(name):
    if 'y' in name:
        new_name = name[:len(name)-1] + 'iful'
        
    else:
        new_name = name + 'y'
    return f'<h1>Upper case:{new_name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)





