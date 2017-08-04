import sys
import pymysql
from fractions import Fraction

#need code to pull stuff from DB

#need code to analyze the numbers and put out something new
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
    '''
    query = "SELECT * FROM market;"# % (item1)
    #need to get data from DB
    curs.execute(query)
    results = curs.fetchall()
    pricelist = []
    for row in results:
        price_line = row[4]
        trade_item = row[1]
        #print(trade_item)#debug output
        price_line.strip()
        if price_line.find("~b/o", 0, 4) != -1 or price_line.find("~price", 0, 6) != -1:
            split_string = price_line.split()
            if split_string[2] == "chaos":#need to change this to a variable of choice
                pricelist.append(split_string[1])
                print(split_string[1])#debug output
        print(price_line)#debug output
    #return a list of prices
    conn.close()
    return pricelist
    '''
    query = "SELECT seller_item, item_wanted, ammount_item_traded, amount_item_wanted  FROM market;"
    #need to get data from DB
    curs.execute(query)
    results = curs.fetchall()
    price_wanted_list = []
    price_traded_list = []
    item_wanted_list = []
    seller_item_list = []
    for row in results:
        seller_item_list.append(row[0])
        item_wanted_list.append(row[1].strip())
        price_traded_list.append(row[2])
        price_wanted_list.append(row[3])
        #still thinking about how to do this here....
    #return a list of prices
    conn.close()
    return pricelist

def trends():
    #do the math on the trending prices here
    ratio_sum = 0.0
    avg1 = 0.0
    count = 0
    #get the item prices to do calculations with
    price_list = get_data()
    #parse the prices into usable numbers
    for price in price_list:
        if price.find('/') != -1:
            raw_numbers = price.split('/')
            top = int(raw_numbers[0])
            bot = int(raw_numbers[1])
            ratio = top / bot
            ratio_sum = ratio_sum + ratio
        elif float(price) > 1:
            #this will only work if the number is greater than 1, will not work on decimals
            top = 1
            #need to make sure that things like "4.9" are a number and not a ratio
            bot = float(price)
            ratio = top / bot
            ratio_sum = ratio_sum + ratio
        count = count + 1
    #calculate the average price
    avg1 = ratio_sum / count
    avg2 = Fraction(avg1)
    print(avg2)
    #return the average
    return avg2

#get_data()
trends()
