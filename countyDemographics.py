from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) 

def get_state_options(counties):
    listofstates=[]
    option=""
    for data in counties:
        if data["State"] not in listofstates:
            listofstates.append(data["State"])
    for data in listofstates:
        option=option+Markup("<option value=\"" + data + "\">" + data + "</option>")
    return option
    
       
def get_state_fact(counties):
    request.args[state]
    for data in counties:
        data["Miscellaneous"]["Building Permits"]

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state=get_state_options(counties),fact=get_state_fact(counties))

if __name__=="__main__":
    app.run(debug=False, port=54321)
