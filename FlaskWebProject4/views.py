
from flask import render_template,request,redirect,url_for,Flask,jsonify
from FlaskWebProject4 import app
from flask_wtf import FlaskForm 
from wtforms import SelectField 
from flask.json import jsonify 
import pandas as pd
from pandas import DataFrame 
import csv 


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/hello',methods=['POST'])
def hello():
    select3 = request.form.get("year") #in brackets select id goes 
    select4 = request.form.get("hour")
    final = str(select3)+"."+str(select4)
    retlist = list(final.split("."))
    return_lst = []
    for x in retlist:
        if x=="Integrated":
            return_lst.append("Btech Integrated")
        else:
            return_lst.append(x)
    
    df = pd.DataFrame(return_lst)
    df.to_csv('faceapp.csv')

    return "Selected Values Saved"
 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
   

