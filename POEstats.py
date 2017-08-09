import sys
import pymysql
from fractions import Fraction
from pprint import pprint

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
    new_list = []
    transactions = get_data()
    transactions_list = list(transactions)
    conn = makeConnection()
    curs = conn.cursor()
    for row in transactions_list:
        query = "SELECT type_line FROM item WHERE id='%d';" % (row[0])
        curs.execute(query)
        name1 = curs.fetchone()
        name2 = str(name1).strip(')').strip('(').strip(',')
        row_list = list(row)
        row_list[0] = name2
        new_list.append(row_list)
    conn.close()
    return new_list

def trends():
    names_list = ['Splinter of Tul', 'Splinter of Chayula', 'Chaos Orb', 'Orb of Annulment', 'Screaming Essence of Greed', 'Engineers Orb', 'Ancient Orb', 'Orb of Horizons', 'Harbingers Orb', 'Essence of Insanity', 'Vaal Orb', 'Orb of Scouring', 'Blessed Orb', 'Glassblowers Bauble', 'Orb of Binding', 'Exalted Shard', 'Screaming Essence of Scorn', 'Exalted Orb', 'Screaming Essence of Torment', 'Shrieking Essence of Woe', 'Remnant of Corruption', 'Orb of Chance', 'Orb of Alteration', 'Screaming Essence of Envy',  'Screaming Essence of Misery', 'Screaming Essence of Anguish', 'Screaming Essence of Wrath', 'Screaming Essence of Dread', 'Screaming Essence of Suffering', 'Screaming Essence of Zeal', 'Screaming Essence of Fear', 'Wailing Essence of Loathing', 'Screaming Essence of Anger', 'Screaming Essence of Hatred', 'Gemcutters Prism', 'Deafening Essence of Hatred', 'Divine Orb', 'Jewellers Orb', 'Splinter of Uul-Netol', 'Splinter of Esh', 'Screaming Essence of Spite', 'Silver Coin', 'Armourers Scrap', 'Orb of Transmutation', 'Apprentice Cartographers Sextant', 'Cartographers Chisel', 'Orb of Augmentation', 'Orb of Regret', 'Orb of Fusing', 'Blacksmiths Whetstone', 'Screaming Essence of Sorrow', 'Splinter of Xoph', 'Regal Orb', 'Essence of Hysteria', 'Journeyman Cartographers Sextant']
    sum_dict = {'Splinter of Tul': {}, 'Splinter of Chayula': {}, 'Chaos Orb': {}, 'Orb of Annulment': {}, 'Screaming Essence of Greed': {}, 'Engineers Orb': {}, 'Ancient Orb': {}, 'Orb of Horizons': {}, 'Harbingers Orb': {}, 'Essence of Insanity': {}, 'Vaal Orb': {}, 'Orb of Scouring': {}, 'Blessed Orb': {}, 'Glassblowers Bauble': {}, 'Orb of Binding': {}, 'Exalted Shard': {}, 'Screaming Essence of Scorn': {}, 'Exalted Orb': {}, 'Screaming Essence of Torment': {}, 'Shrieking Essence of Woe': {}, 'Remnant of Corruption': {}, 'Orb of Chance': {}, 'Orb of Alteration': {}, 'Screaming Essence of Envy': {},  'Screaming Essence of Misery': {}, 'Screaming Essence of Anguish': {}, 'Screaming Essence of Wrath': {}, 'Screaming Essence of Dread': {}, 'Screaming Essence of Suffering': {}, 'Screaming Essence of Zeal': {}, 'Screaming Essence of Fear': {}, 'Wailing Essence of Loathing': {}, 'Screaming Essence of Anger': {}, 'Screaming Essence of Hatred': {}, 'Gemcutters Prism': {}, 'Deafening Essence of Hatred': {}, 'Divine Orb': {}, 'Jewellers Orb': {}, 'Splinter of Uul-Netol': {}, 'Splinter of Esh': {}, 'Screaming Essence of Spite': {}, 'Silver Coin': {}, 'Armourers Scrap': {}, 'Orb of Transmutation': {}, 'Apprentice Cartographers Sextant': {}, 'Cartographers Chisel': {}, 'Orb of Augmentation': {}, 'Orb of Regret': {}, 'Orb of Fusing': {}, 'Blacksmiths Whetstone': {}, 'Screaming Essence of Sorrow': {}, 'Splinter of Xoph': {}, 'Regal Orb': {}, 'Essence of Hysteria': {}, 'Journeyman Cartographers Sextant': {}}
    count_dict = {'Splinter of Tul': {}, 'Splinter of Chayula': {}, 'Chaos Orb': {}, 'Orb of Annulment': {}, 'Screaming Essence of Greed': {}, 'Engineers Orb': {}, 'Ancient Orb': {}, 'Orb of Horizons': {}, 'Harbingers Orb': {}, 'Essence of Insanity': {}, 'Vaal Orb': {}, 'Orb of Scouring': {}, 'Blessed Orb': {}, 'Glassblowers Bauble': {}, 'Orb of Binding': {}, 'Exalted Shard': {}, 'Screaming Essence of Scorn': {}, 'Exalted Orb': {}, 'Screaming Essence of Torment': {}, 'Shrieking Essence of Woe': {}, 'Remnant of Corruption': {}, 'Orb of Chance': {}, 'Orb of Alteration': {}, 'Screaming Essence of Envy': {},  'Screaming Essence of Misery': {}, 'Screaming Essence of Anguish': {}, 'Screaming Essence of Wrath': {}, 'Screaming Essence of Dread': {}, 'Screaming Essence of Suffering': {}, 'Screaming Essence of Zeal': {}, 'Screaming Essence of Fear': {}, 'Wailing Essence of Loathing': {}, 'Screaming Essence of Anger': {}, 'Screaming Essence of Hatred': {}, 'Gemcutters Prism': {}, 'Deafening Essence of Hatred': {}, 'Divine Orb': {}, 'Jewellers Orb': {}, 'Splinter of Uul-Netol': {}, 'Splinter of Esh': {}, 'Screaming Essence of Spite': {}, 'Silver Coin': {}, 'Armourers Scrap': {}, 'Orb of Transmutation': {}, 'Apprentice Cartographers Sextant': {}, 'Cartographers Chisel': {}, 'Orb of Augmentation': {}, 'Orb of Regret': {}, 'Orb of Fusing': {}, 'Blacksmiths Whetstone': {}, 'Screaming Essence of Sorrow': {}, 'Splinter of Xoph': {}, 'Regal Orb': {}, 'Essence of Hysteria': {}, 'Journeyman Cartographers Sextant': {}}
    avgs_dict = {'Splinter of Tul': {}, 'Splinter of Chayula': {}, 'Chaos Orb': {}, 'Orb of Annulment': {}, 'Screaming Essence of Greed': {}, 'Engineers Orb': {}, 'Ancient Orb': {}, 'Orb of Horizons': {}, 'Harbingers Orb': {}, 'Essence of Insanity': {}, 'Vaal Orb': {}, 'Orb of Scouring': {}, 'Blessed Orb': {}, 'Glassblowers Bauble': {}, 'Orb of Binding': {}, 'Exalted Shard': {}, 'Screaming Essence of Scorn': {}, 'Exalted Orb': {}, 'Screaming Essence of Torment': {}, 'Shrieking Essence of Woe': {}, 'Remnant of Corruption': {}, 'Orb of Chance': {}, 'Orb of Alteration': {}, 'Screaming Essence of Envy': {},  'Screaming Essence of Misery': {}, 'Screaming Essence of Anguish': {}, 'Screaming Essence of Wrath': {}, 'Screaming Essence of Dread': {}, 'Screaming Essence of Suffering': {}, 'Screaming Essence of Zeal': {}, 'Screaming Essence of Fear': {}, 'Wailing Essence of Loathing': {}, 'Screaming Essence of Anger': {}, 'Screaming Essence of Hatred': {}, 'Gemcutters Prism': {}, 'Deafening Essence of Hatred': {}, 'Divine Orb': {}, 'Jewellers Orb': {}, 'Splinter of Uul-Netol': {}, 'Splinter of Esh': {}, 'Screaming Essence of Spite': {}, 'Silver Coin': {}, 'Armourers Scrap': {}, 'Orb of Transmutation': {}, 'Apprentice Cartographers Sextant': {}, 'Cartographers Chisel': {}, 'Orb of Augmentation': {}, 'Orb of Regret': {}, 'Orb of Fusing': {}, 'Blacksmiths Whetstone': {}, 'Screaming Essence of Sorrow': {}, 'Splinter of Xoph': {}, 'Regal Orb': {}, 'Essence of Hysteria': {}, 'Journeyman Cartographers Sextant': {}}
    transactions = get_item_name()
    for row in transactions:
        check = str(row[0].strip('\''))
        for name in names_list:
            if check == name:
                want = str(row[1].strip('\''))
                if want in sum_dict[name].keys():
                    running_total = sum_dict[name][want]
                    if row[3] != 0:
                        running_total = running_total + (row[2] / row[3])
                    sum_dict[name][want] = running_total
                else:
                    if row[3] != 0:
                        sum_dict[name][want] = (row[2] / row[3])
                    else:
                        sum_dict[name][want] = 0#not sure about this....just a test case to solve a problem....maybe brians version of split note will fix it
                if want in count_dict[name].keys():
                    running_count = count_dict[name][want]
                    running_count = running_count + 1
                    count_dict[name][want] = running_count
                else:
                    count_dict[name][want] = 1
    for row in transactions:
        check = str(row[0].strip('\''))
        for name in names_list:
            if check == name:
                want = str(row[1].strip('\''))
                if want in avgs_dict[name].keys():
                    running_avg = avgs_dict[name][want]
                    numerator = sum_dict[name][want]
                    denominator = count_dict[name][want]
                    running_avg = running_avg + (numerator / denominator)
                    avgs_dict[name][want] = running_avg
                else:
                    numerator = sum_dict[name][want]
                    denominator = count_dict[name][want]
                    avgs_dict[name][want] = (numerator / denominator)
    #pprint(sum_dict)
    #pprint(count_dict)
    pprint(avgs_dict)
    #avgs_dict[name][row[1]] = Fraction(sum_dict[name][row[1]] / count_dict[name][row[1]]).limit_denominator(100)
    return avgs_dict

def post_stats():
    #put the data in the trends table in this order: selling_item, ratio, buying_item
	conn = makeConnection()
	curs = conn.cursor()
	transactions = get_item_name()
	#need a for loop here to go through the transactions
	prices = trends()
	#also need a loop to go through the averages
	query = None
	curs.execute(query)
	
	return 1 
	
#get_data()
trends()

