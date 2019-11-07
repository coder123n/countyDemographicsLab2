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
    
       
def get_state_fact(counties,state):
    num=0
    for data in counties:
        if data["State"] == state:
            num=data["Miscellaneous"]["Building Permits"]
    fact= srt(state) + " has " + str(num) + " building permits......"
    return fact
    
@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state=get_state_options(counties),fact='')

@app.route("/reply")
def render_reply():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state=get_state_options(counties),fact=get_state_fact(counties,request.args["state"]))
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
