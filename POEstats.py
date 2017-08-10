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

def get_data():
    #connect with DB
    conn = makeConnection()
    curs = conn.cursor()
    #query to pull needed data
    query = "SELECT seller_item, item_wanted, seller_paying_amount, seller_buying_amount  FROM market;"
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
                    if float(row[3]) != 0:
                        running_total = running_total + (float(row[2]) / float(row[3]))
                    sum_dict[name][want] = running_total
                else:
                    if float(row[3]) != 0:
                        sum_dict[name][want] = (float(row[2]) / float(row[3]))
                    else:
                        sum_dict[name][want] = 0#fall back case
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
                    avgs_dict[name][want] = Fraction(str(running_avg)).limit_denominator(100)
                else:
                    numerator = sum_dict[name][want]
                    denominator = count_dict[name][want]
                    avgs_dict[name][want] = Fraction(str((numerator / denominator))).limit_denominator(100)
    return avgs_dict

def post_stats():
    #put the data in the trends table in this order: selling_item, ratio, buying_item
    conn = makeConnection()
    curs = conn.cursor()
    #need a for loop here to go through the transactions
    trends_dict = trends()
    #cycle through dict and insert items into 'trends' table as you go
    for sell, buy in trends_dict.items():
        for want, price in buy.items():
            query = "INSERT INTO trends (item_buying, avg_price, item_selling) VALUES ('%s', '%s', '%s');" % (want, str(price), sell)
            try:
                # Tries to insert item into the database.
                curs.execute(query)
                conn.commit()
            except pymysql.InternalError as error:
                # If item cannot be inserted into database it prints the item on the console
                print("\nERROR entering item!")
                print(sell)
                print(buy)
                print(error)
    conn.close()
    return 1

post_stats()