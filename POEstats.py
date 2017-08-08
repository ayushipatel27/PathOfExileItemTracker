import sys
import pymysql
from fractions import Fraction

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

#@app.route('/trends', methods=['GET', 'POST'])
def get_data():
    #connect with DB
    conn = makeConnection()
    curs = conn.cursor()
    #query to pull needed data
    query = "SELECT seller_item, item_wanted, amount_item_traded, amount_item_wanted  FROM market;"
    #execute query and store data
    curs.execute(query)
    results = curs.fetchall()
    pricelist = []
    item_wanted_list = []
    #will need to reference this seller_item list to item table in db to get name of item
    seller_item_list = []
    for row in results:
        seller_item_list.append(row[0])
        item_wanted_list.append(row[1].strip())
        #store the two prices into a list as a 1-2 orderd pair....easier than using dict
        pricelist.append(row[3])
        pricelist.append(row[2])
    #return a list of prices
    conn.close()
    return pricelist

def trends():
    #do the math on the trending prices here
    ratio_sum = 0.0
    avg1 = 0.0
    count = 0
    i = 0
    #get the item prices to do calculations with
    price_list = get_data()
    while i < len(price_list):
        ratio_sum = ratio_sum + (price_list[i] / price_list[(i + 1)])
        count = count + 1
        i = i + 2
    #calculate the average price
    avg1 = ratio_sum / count
    avg2 = Fraction(avg1).limit_denominator(100)#may need to make this limit=1000
    print(avg1)#test output
    print(avg2)#test output
    #need to post this and the appropriate names to the db
    #return the average
    return avg2

#get_data()
trends()
