import requests
import sys
import pymysql

poe_api = 'http://api.pathofexile.com/api/public-stash-tabs?id='
request_id = requests.get('http://api.poe.ninja/api/Data/GetStats').json()
last_id = request_id['nextChangeId']


def parseStash(api_id):
    stash_data = requests.get(poe_api + api_id).json()
    stashes = stash_data['stashes']
    for stash in stashes:
        seller_account_id = stash['accountName']
        seller_character_name = stash['lastCharacterName']
        for item in stash['items']:
            if (item['frameType'] is 5):
                if('note' in item):
                    id = item['id']
                    icon = item['icon']
                    type_line = item['typeLine']
                    league = item['league']
                    note = item['note']
                    stack_size = item['stackSize']
                    tracked_item = {
                        'id': id,
                        'seller_account_id': seller_account_id,
                        'seller_character_name': seller_character_name,
                        'icon': icon,
                        'type_line': type_line,
                        'league': league,
                        'note': note,
                        'stack_size': stack_size
                    }
                    # print("CALL create_item ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (id, type_line, icon, note, seller_account_id, seller_character_name, league, stack_size))
                    insertItem(**tracked_item)


def insertItem(**tracked_item):
    id = tracked_item['id'].strip()
    type_line = tracked_item['type_line'].strip().translate(str.maketrans({"'":None}))
    icon = tracked_item['icon'].strip()
    note = tracked_item['note'].strip()
    seller_account_id = tracked_item['seller_account_id'].strip()
    seller_character_name = tracked_item['seller_character_name'].strip()
    league = tracked_item['league'].strip()
    stack_size = tracked_item['stack_size']
    conn = makeConnection()
    c = conn.cursor()

    # Insert student data.
    query = "CALL create_item ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (id, type_line, icon, note, seller_account_id, seller_character_name, league, stack_size)
    c.execute(query)
    conn.commit()
    conn.close()


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


while True:
    new_request = requests.get('http://api.poe.ninja/api/Data/GetStats').json()
    updated_id = new_request['nextChangeId']
    if(updated_id is not last_id):
        parseStash(updated_id)
    last_id = updated_id