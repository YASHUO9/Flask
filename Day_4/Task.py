from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index1():
    first = request.args.get('UserName')
    
    return render_template('index1.html')


@app.route('/passs')
def passs():
    return  render_template('passs.html')


@app.route('/not_pass')
def not_pass():
    return render_template('not_pass.html')
@app.route('/report')
def report():
        
    first = request.args.get('UserName')
    ress = False
    for ele in first:# checking for uppercase character
        if ele.isupper():
            ress = True
            break
    res = any(chr.isdigit() for chr in first)    
    lower_letter = any(c.islower() for c in first)
    if res and ress and lower_letter:
        return  render_template('passs.html')
    else:
        return  render_template('not_pass.html')
    
# if ress and res is True:
#     return render_template('index1.html')




if __name__=="__main__":
    app.run(debug=True)