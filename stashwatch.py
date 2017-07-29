import requests
import sys
import pymysql
import time

# Neat. http://www.network-science.de/ascii/
def graffiti():
    print("  _________________________    _________ ___ ___")
    print(" /   _____/\__    ___/  _  \  /   _____//   |   \ ")
    print(" \_____  \   |    | /  /_\  \ \_____  \/    ~    \ ")
    print(" /        \  |    |/    |    \/        \    Y    /")
    print("/_______  /  |____|\____|__  /_______  /\___|_  / ")
    print("        \/                 \/        \/       \/  ")
    print(" __      __  _________________________   ___ ___  ")
    print("/  \    /  \/  _  \__    ___/\_   ___ \ /   |   \ ")
    print("\   \/\/   /  /_\  \|    |   /    \  \//    ~    \ ")
    print(" \        /    |    \    |   \     \___\    Y    /")
    print("  \__/\  /\____|__  /____|    \______  /\___|_  / ")
    print("       \/         \/                 \/       \/  ")

# Main API endpoint.
poe_api = 'http://api.pathofexile.com/api/public-stash-tabs?id='

# Gets the most updated api ID from poe.ninja.
request_id = requests.get('http://api.poe.ninja/api/Data/GetStats').json()
last_id = request_id['nextChangeId']

# Meat and bones of this program.
# Returns the API's next ID.
def parseStash(api_id):
    # stash_data is the link to the api with the next id concatenated at its end.
    stash_data = requests.get(poe_api + api_id).json()
    # Tries to look into the api for items. Will throw exception if the API is empty at the next id.
    try:
        stashes = stash_data['stashes']
        # For each stash in the list of all stashes from the api.
        for stash in stashes:
            # The stash owner.
            for item in stash['items']:
                # frameType 5 is a currency item.
                if (item['frameType'] is 5):
                    # note is where someone will list a price if its for sale.
                    if('note' in item):
                        seller_account_id = stash['accountName']
                        seller_character_name = stash['lastCharacterName']
                        item_id = item['id']
                        icon = item['icon']
                        # typeLine is the item name
                        type_line = item['typeLine']
                        league = item['league']
                        note = item['note']
                        quantity = item['stackSize']
                        frame_type = item['frameType']
                        tracked_item = {
                            'item_id': item_id,
                            'seller_account_id': seller_account_id,
                            'seller_character_name': seller_character_name,
                            'icon': icon,
                            'type_line': type_line,
                            'league': league,
                            'note': note,
                            'quantity': quantity,
                            'frame_type': frame_type,
                        }
                        # Tries to insert item into the database.
                        try:
                            insertItem(**tracked_item)
                        # If item cannot be inserted into database it prints the item on the console.
                        except:
                            print("\nERROR entering item!")
                            print(tracked_item)
        # Gets the next ID for the next API stash dump.
        next_id = stash_data['next_change_id']
        # Returns next_id for an endless loop.
        return next_id
    # If the API is empty on this ID. Most likely when at the end of the data "river".
    # Needs to wait for information to be posted.
    except:
        print("Next JSON not ready. ID: " + api_id)
        # Waits 15 seconds before asking for information.
        time.sleep(15)
        return api_id

# Inserts item into database.
def insertItem(**tracked_item):
    item_id = tracked_item['item_id'].strip()
    frame_type = tracked_item['frame_type']
    # Attempt at getting rid of apostrophes from type_line (type_line is the item name).
    type_line = tracked_item['type_line'].strip().translate(str.maketrans({"'":None}))
    # icon appears to be going into the database as "None" it is suppose to be a link to a cdn of items.
    icon = tracked_item['icon'].strip()
    note = tracked_item['note'].strip()
    seller_account_id = tracked_item['seller_account_id'].strip()
    seller_character_name = tracked_item['seller_character_name'].strip()
    league = tracked_item['league'].strip()
    quantity = tracked_item['quantity']
    conn = makeConnection()
    c = conn.cursor()

    # Insert item data.
    query = "CALL post_item ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (item_id, icon, note, seller_account_id, seller_character_name, league, quantity, type_line, frame_type)
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

# Shows ASCII title when ran.
graffiti()
# Runs an endless loop to continually get the newest API ID and find items for the database.
while True:
    last_id = str(parseStash(last_id))