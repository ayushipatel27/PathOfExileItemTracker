import requests
import sys
import pymysql
import time
from dbfunctions import *
from itemcreator import *

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

def updateid(last_id, next_id):
    try:
        updateJsonId(last_id, next_id)
    except:
        print('Error upating API ID in stashwatch.py')


def parseRetrievedStashes(stashes):
    for stash in stashes:
        for item in stash['items']:
            # frameType 5 is a currency item.
            if (item['frameType'] is 5):
                # note is where someone will list a price if its for sale.
                if ('note' in item):
                    createItem(item, stash)


def parseStash(api_id):
    try:
        stash_data = requests.get(poe_api + api_id).json()
        stashes = stash_data['stashes']
        parseRetrievedStashes(stashes)
        next_id = stash_data['next_change_id']
        updateid(api_id, next_id)
        return next_id
    except:
        print("Next JSON not ready. ID: " + api_id)
        time.sleep(15)
        return api_id

def findJsonId():
    try:
        next_id = getNextJsonId().strip()
        if(next_id == None):
            raise Exception
    except:
        request_id = requests.get('http://api.poe.ninja/api/Data/GetStats').json()
        return request_id['nextChangeId']

# Shows ASCII title when ran.
graffiti()
last_id = findJsonId()
# Runs an endless loop to continually get the newest API ID and find items for the database.
while True:
    last_id = parseStash(last_id)