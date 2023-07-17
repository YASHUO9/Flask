from flask import Flask , render_template
#Without using the template folder it is not working exactly that i want
app = Flask(__name__)

@app.route('/')


def index():
    """Here I have use the template variable"""
    name = "Yash"
    variable  = [i for i in name]
    return render_template("index.html",name = name,variable = variable)


if __name__ =='__main__':
    app.run(debug=True)