# Authors: Bryan Arretteig, Craig Brewton, Ayushi Patel

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
		host=hostStr,
		charset='utf8')
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

def getTrade(has, want):
	# trade = 'CALL get_trade(' + input + ');'
	conn = makeConnection()
	c = conn.cursor()

	query = "CALL get_trade ('%s', '%s');" % (has, want)
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

# Inserts item into database.
def insertItem(**tracked_item):
	item_id = tracked_item['item_id'].strip()
	frame_type = tracked_item['frame_type']
	# Attempt at getting rid of apostrophes from type_line (type_line is the item name).
	type_line = tracked_item['type_line'].strip().translate(str.maketrans({"'":None}))
	# icon appears to be going into the database as "None" it is suppose to be a link to a cdn of items.
	icon = tracked_item['icon'].strip()
	item_wanted = tracked_item['item_wanted'].strip()
	seller_paying_amount = tracked_item['seller_paying_amount']
	seller_wanting_amount = tracked_item['seller_wanting_amount']
	seller_account_id = tracked_item['seller_account_id'].strip()
	seller_character_name = tracked_item['seller_character_name'].strip()
	league = tracked_item['league'].strip()
	quantity = tracked_item['quantity']
	conn = makeConnection()
	c = conn.cursor()
	query = "CALL post_item ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (item_id, icon, item_wanted, seller_paying_amount, seller_wanting_amount, seller_account_id, seller_character_name, league, quantity, type_line, frame_type)
	c.execute(query)
	conn.commit()
	conn.close()


def updateJsonId(last_id, next_id):
	try:
		conn = makeConnection()
		c = conn.cursor()
		query = "CALL update_json_id('%s', '%s');" % (last_id, next_id)
		c.execute(query)
		conn.commit()
		conn.close()
	except:
		print('Error Updating POE JSON IDs')

def getNextJsonId():
	try:
		conn = makeConnection()
		c = conn.cursor()
		query = "CALL get_next_id();"
		c.execute(query)
		results = c.fetchall()
		conn.close()
		return results
	except:
		print('Error getting POE JSON ID')

def getApiInfo():
	try:
		conn = makeConnection()
		c = conn.cursor()
		query = "CALL get_stashwatch_api_ids();"
		c.execute(query)
		results = c.fetchall()
		conn.close()
		return results
	except:
		print('Error getting STASHWATCH API JSON')