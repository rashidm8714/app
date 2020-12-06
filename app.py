from flask import Flask, render_template, request
import pandas as pd 
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> hello  </h1>'


@app.route('/ui',methods= [ 'GET','POST'])
def ui():
    return render_template('userinterface.html')


@app.route('/data', methods= [ 'GET','POST'])
def data():
    if request.method == 'POST':
        f= request.form.get('csvFile', 'default value')
        data = []
        with open(f) as file:
            csvFile = csv.reader(file)
            for row in csvFile:
                data.append(row)
            #print (type(data))
            data = pd.DataFrame(data)
        return render_template('data.html', data= data.to_html(header= False, index=False))
if __name__ == '__main__':
    
    app.run(debug= True)