#!/usr/bin/python  

from flask import Flask, render_template, request, Response
import json
import sys
import pymysql
 
app = Flask(__name__)
 
@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route('/market', methods=['GET'])
def market():
	market = getMarket()
	return render_template('market.html', market=market)


def makeConnection():
	file = open(sys.path[0]+"/dbconfig.txt", "r")
	dbStr = file.readline().strip()
	userStr = file.readline().strip()
	passwdStr = file.readline().strip()
	hostStr = file.readline().strip()
	conn = pymysql.connect(
        db=dbStr,
        user=userStr,
        passwd=passwdStr,
        host=hostStr)
	return conn


def getMarket():
	conn = makeConnection()
	c = conn.cursor()

	# Print the contents of the db table.
	c.execute("CALL get_market();")

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()
	return results


# used for debugging in development only!  NOT for production!!!
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)