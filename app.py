#!/usr/bin/python  

from flask import Flask, render_template, request, Response
import json

 
app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')
 

# used for debugging in development only!  NOT for production!!!
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)