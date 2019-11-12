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
    
def get_county_options(counties,state):
    listofcounties=[]
    option=""
    for data in counties:
        if data["State"] == state:
            if data["County"] not in listofcounties:
                listofcounties.append(data["County"])
    for data in listofcounties:
        option=option+Markup("<option value=\"" + data + "\">" + data + "</option>")
    return option
    
def get_county_fact(counties,county):
    num=0
    for data in counties:
            if data["County"] == county:
                num=data["Miscellaneous"]["Building Permits"]
                fact= str(county) + " in " + str(data["State"]) + " has " + str(num) + " building permit(s)!!!"
    return fact
    
@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state=get_state_options(counties),county='',fact='')

@app.route("/fun")
def render_fun():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state=get_state_options(counties),county=get_county_options(counties,request.args["State"]),fact='')
    
@app.route("/reply")
def render_reply():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state=get_state_options(counties),county='',fact=get_county_fact(counties,request.args["County"]))
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
