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
    conn.close()
    return results

def get_item_name():
    transactions = get.data()
    conn = makeConnection()
    curs = conn.cursor()
    for row in transactions:
        query = "SELECT type_line FROM item WHERE id='%d';" % (row[0])
        curs.execute(query)
        name = curs.fetchone()
        row[0] = name
    conn.close()
    return transactions

def trends():
    names_list = ['Splinter of Tul', 'Splinter of Chayula', 'Chaos Orb', 'Orb of Annulment', 'Screaming Essence of Greed', 'Engineers Orb', 'Ancient Orb', 'Orb of Horizons', 'Harbingers Orb',
	                'Essence of Insanity', 'Vaal Orb', 'Orb of Scouring', 'Blessed Orb', 'Glassblowers Bauble', 'Orb of Binding', 'Exalted Shard', 'Screaming Essence of Scorn', 'Exalted Orb',
					'Screaming Essence of Torment', 'Shrieking Essence of Woe', 'Remnant of Corruption', 'Orb of Chance', 'Orb of Alteration', 'Screaming Essence of Envy',  'Screaming Essence of Misery',
					'Screaming Essence of Anguish', 'Screaming Essence of Wrath', 'Screaming Essence of Dread', 'Screaming Essence of Suffering', 'Screaming Essence of Zeal',
					'Screaming Essence of Fear', 'Wailing Essence of Loathing', 'Screaming Essence of Anger', 'Screaming Essence of Hatred', 'Gemcutters Prism', 'Deafening Essence of Hatred',
					'Divine Orb', 'Jewellers Orb', 'Splinter of Uul-Netol', 'Splinter of Esh', 'Screaming Essence of Spite', 'Silver Coin', 'Armourers Scrap', 'Orb of Transmutation',
					'Apprentice Cartographers Sextant', 'Cartographers Chisel', 'Orb of Augmentation', 'Orb of Regret', 'Orb of Fusing', 'Blacksmiths Whetstone', 'Screaming Essence of Sorrow',
					'Splinter of Xoph', 'Regal Orb', 'Essence of Hysteria', 'Journeyman Cartographers Sextant']
    sum_dict = {'Splinter of Tul': [], 'Splinter of Chayula': [], 'Chaos Orb': [], 'Orb of Annulment': [], 'Screaming Essence of Greed': [], 'Engineers Orb': [], 'Ancient Orb': [], 'Orb of Horizons': [], 'Harbingers Orb': [],
	                'Essence of Insanity': [], 'Vaal Orb': [], 'Orb of Scouring': [], 'Blessed Orb': [], 'Glassblowers Bauble': [], 'Orb of Binding': [], 'Exalted Shard': [], 'Screaming Essence of Scorn': [], 'Exalted Orb': [],
					'Screaming Essence of Torment': [], 'Shrieking Essence of Woe': [], 'Remnant of Corruption': [], 'Orb of Chance': [], 'Orb of Alteration': [], 'Screaming Essence of Envy': [],  'Screaming Essence of Misery': [],
					'Screaming Essence of Anguish': [], 'Screaming Essence of Wrath': [], 'Screaming Essence of Dread': [], 'Screaming Essence of Suffering': [], 'Screaming Essence of Zeal': [],
					'Screaming Essence of Fear': [], 'Wailing Essence of Loathing': [], 'Screaming Essence of Anger': [], 'Screaming Essence of Hatred': [], 'Gemcutters Prism': [], 'Deafening Essence of Hatred': [],
					'Divine Orb': [], 'Jewellers Orb': [], 'Splinter of Uul-Netol': [], 'Splinter of Esh': [], 'Screaming Essence of Spite': [], 'Silver Coin': [], 'Armourers Scrap': [], 'Orb of Transmutation': [],
					'Apprentice Cartographers Sextant': [], 'Cartographers Chisel': [], 'Orb of Augmentation': [], 'Orb of Regret': [], 'Orb of Fusing': [], 'Blacksmiths Whetstone': [], 'Screaming Essence of Sorrow': [],
					'Splinter of Xoph': [], 'Regal Orb': [], 'Essence of Hysteria': [], 'Journeyman Cartographers Sextant': []}
    count_dict = {'Splinter of Tul': [], 'Splinter of Chayula': [], 'Chaos Orb': [], 'Orb of Annulment': [], 'Screaming Essence of Greed': [], 'Engineers Orb': [], 'Ancient Orb': [], 'Orb of Horizons': [], 'Harbingers Orb': [],
	                'Essence of Insanity': [], 'Vaal Orb': [], 'Orb of Scouring': [], 'Blessed Orb': [], 'Glassblowers Bauble': [], 'Orb of Binding': [], 'Exalted Shard': [], 'Screaming Essence of Scorn': [], 'Exalted Orb': [],
					'Screaming Essence of Torment': [], 'Shrieking Essence of Woe': [], 'Remnant of Corruption': [], 'Orb of Chance': [], 'Orb of Alteration': [], 'Screaming Essence of Envy': [],  'Screaming Essence of Misery': [],
					'Screaming Essence of Anguish': [], 'Screaming Essence of Wrath': [], 'Screaming Essence of Dread': [], 'Screaming Essence of Suffering': [], 'Screaming Essence of Zeal': [],
					'Screaming Essence of Fear': [], 'Wailing Essence of Loathing': [], 'Screaming Essence of Anger': [], 'Screaming Essence of Hatred': [], 'Gemcutters Prism': [], 'Deafening Essence of Hatred': [],
					'Divine Orb': [], 'Jewellers Orb': [], 'Splinter of Uul-Netol': [], 'Splinter of Esh': [], 'Screaming Essence of Spite': [], 'Silver Coin': [], 'Armourers Scrap': [], 'Orb of Transmutation': [],
					'Apprentice Cartographers Sextant': [], 'Cartographers Chisel': [], 'Orb of Augmentation': [], 'Orb of Regret': [], 'Orb of Fusing': [], 'Blacksmiths Whetstone': [], 'Screaming Essence of Sorrow': [],
					'Splinter of Xoph': [], 'Regal Orb': [], 'Essence of Hysteria': [], 'Journeyman Cartographers Sextant': []}
	avgs_dict = {'Splinter of Tul': [], 'Splinter of Chayula': [], 'Chaos Orb': [], 'Orb of Annulment': [], 'Screaming Essence of Greed': [], 'Engineers Orb': [], 'Ancient Orb': [], 'Orb of Horizons': [], 'Harbingers Orb': [],
	                'Essence of Insanity': [], 'Vaal Orb': [], 'Orb of Scouring': [], 'Blessed Orb': [], 'Glassblowers Bauble': [], 'Orb of Binding': [], 'Exalted Shard': [], 'Screaming Essence of Scorn': [], 'Exalted Orb': [],
					'Screaming Essence of Torment': [], 'Shrieking Essence of Woe': [], 'Remnant of Corruption': [], 'Orb of Chance': [], 'Orb of Alteration': [], 'Screaming Essence of Envy': [],  'Screaming Essence of Misery': [],
					'Screaming Essence of Anguish': [], 'Screaming Essence of Wrath': [], 'Screaming Essence of Dread': [], 'Screaming Essence of Suffering': [], 'Screaming Essence of Zeal': [],
					'Screaming Essence of Fear': [], 'Wailing Essence of Loathing': [], 'Screaming Essence of Anger': [], 'Screaming Essence of Hatred': [], 'Gemcutters Prism': [], 'Deafening Essence of Hatred': [],
					'Divine Orb': [], 'Jewellers Orb': [], 'Splinter of Uul-Netol': [], 'Splinter of Esh': [], 'Screaming Essence of Spite': [], 'Silver Coin': [], 'Armourers Scrap': [], 'Orb of Transmutation': [],
					'Apprentice Cartographers Sextant': [], 'Cartographers Chisel': [], 'Orb of Augmentation': [], 'Orb of Regret': [], 'Orb of Fusing': [], 'Blacksmiths Whetstone': [], 'Screaming Essence of Sorrow': [],
					'Splinter of Xoph': [], 'Regal Orb': [], 'Essence of Hysteria': [], 'Journeyman Cartographers Sextant': []}
	#need a list of the abbreviated names...
    transactions = get_item_name()
    for row in transactions:
	    for name in names_list:
            if row[0] == name:
			    #need another logic statement here to check and see what the other item is and only combine averages of matching sets.....how?.....and how to reformat the avgs dict
			    sum_dict[name] = sum_dict[name] + (row[2] / row[3])
                count_dict[name] = count_dict[name] + 1
			    avgs_dict[name] = Fraction(sum_dict[name] / count_dict[name]).limit_denominator(100)
	return avgs_dict

def post_stats():
    #put the data in the trends table in this order: selling_item, ratio, buying_item
	conn = makeConnection()
	curs = conn.cursor()
	transactions = get_item_name()
	#need a for loop here to go through the transactions
	prices = trends()
	#also need a loop to go through the averages
	query = ???
	curs.execute(query)
	
	return 1 
	
	
#get_data()
trends()


#****************************************************************************************************************************************************************
'''
def get_data():
    #connect with DB
    conn = makeConnection()
    curs = conn.cursor()
    #query to pull needed data
    query = "SELECT seller_item, item_wanted, amount_item_traded, amount_item_wanted  FROM market;"
    #execute query and store data
    curs.execute(query)
    results = curs.fetchall()
    conn.close()
    return results

def get_item_name():
    transactions = get.data()
    conn = makeConnection()
    curs = conn.cursor()
    for row in transactions:
        #need code to SELECT from 'item' table based on seller_item
        query = "SELECT type_line FROM item WHERE id='%d';" % (row[0])
        curs.execute(query)
        name = curs.fetchone()
        row[0] = name
    conn.close()
    return transactions

def trends():
    #think i need to make a dict here to store the new averages
    avg = 0.0
    names_list = [
    transactions = get_item_name()
    for row in transactions:
        if row[0] == 'Chaos' and row[1] == 'exa':
            avg = avg + (row[2] / row[3])



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
'''