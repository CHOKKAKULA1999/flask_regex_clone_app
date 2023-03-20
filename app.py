from flask import Flask, request, render_template ,request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=[ 'POST'])
def match_regex():
    #getting the input from the form 
    string = request.form['string']
    regex = request.form['regex']
    
    
    #find all the matching string 
    
    matches = re.findall(regex , string)
    count = 0 
    for i in matches:
        count = count + 1
    count_total = count
    return render_template('index.html' , string = string   , regex = regex , matches = matches , count_total = count_total )



if __name__ == '__main__':
    app.run(debug=True)
