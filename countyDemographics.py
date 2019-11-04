from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) 

def get_state_options(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    listofstates=[]
    for data in counties:
        if data["State"] not in listofstates:
            listofstates.append(data["State"])
    return listofstates

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',state="get_state_options(counties)")

if __name__=="__main__":
    app.run(debug=False, port=54321)
