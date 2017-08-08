# Connect to the database.
import sys
import pymysql
import pymysql.cursors

# connect to db
# pymysql.connect def makeConnection():
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

# void def createUser(**credentials):
def createUser(**credentials):
	name = credentials['name'].strip()
	email = credentials['email'].strip()
	username = credentials['username'].strip()
	password = credentials['password'].strip()

	conn = makeConnection()
	c = conn.cursor(pymysql.cursors.DictCursor)

	# Insert student data.
	sql = "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)"
	data = (name, email, username, password)
	c.execute(sql, data)
	conn.commit()
	conn.close()

def getUser(**loginInfo):
	userName = loginInfo['username'].strip()
	password = loginInfo['password'].strip()

	conn = makeConnection()
	c = conn.cursor(pymysql.cursors.DictCursor)

	sql = "SELECT * FROM users WHERE username = %s"
	data = [userName]
	username = c.execute(sql, data)
	data = c.fetchone()
	password = data['password']

	conn.close()
	return username, password

def saveHasItem(hasItem, user):
	conn = makeConnection()
	c = conn.cursor()

	query = "CALL save_has_items('%s, %s');" %(hasItem) %(user)
	c.execute(query)

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()

def saveWantItem(wantItem, user):
	conn = makeConnection()
	c = conn.cursor()

	query = "CALL save_wants_items('%s, %s');" %(wantItem) %(user)
	c.execute(query)

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()


def getMarket():
	conn = makeConnection()
	c = conn.cursor()

	# Print the contents of the db table.
	c.execute("CALL get_market();")

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()
	return results

def getTrade(trade):
	# trade = 'CALL get_trade(' + input + ');'
	conn = makeConnection()
	c = conn.cursor()

	query = "CALL get_trade ('%s');" % (trade)
	c.execute(query)

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()
	return results

def getItems():
	conn = makeConnection()
	c = conn.cursor()

	# Print the contents of the db table.
	c.execute("CALL get_items();")

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()
	return results
