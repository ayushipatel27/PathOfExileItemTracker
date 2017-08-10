from dbfunctions import *

tracked_item = {}

def splitNote(note):
    try:
        attemptSplitNote(note)
    except:
        return

def attemptSplitNote(note):
    note_subs = []
    note.strip()
    seller_paying_amount = 0.0
    seller_wanting_amount = 0.0
    item_wanted = ""
    if note.find("~b/o", 0, 4) != 1 or note.find("~price", 0, 6) != -1:
        note_subs = note.split()
        if len(note_subs) == 3:
            item_wanted = note_subs[2]
        price = note_subs[1]
        if price.find('/') != -1:
            raw_numbers = price.split('/')
            seller_paying_amount = float(raw_numbers[1])
            seller_wanting_amount = float(raw_numbers[0])
        elif float(price) == 1:
            seller_paying_amount = 1.0
            seller_wanting_amount = 1.0
        elif float(price) > 1:
            seller_paying_amount = 1.0
            seller_wanting_amount = float(price)
        elif (float(price) < 1) and (float(price) > 0):
            seller_paying_amount = 1 / float(price)
            seller_wanting_amount = 1.0
    tracked_item['seller_paying_amount'] = seller_paying_amount
    tracked_item['seller_wanting_amount'] = seller_wanting_amount
    tracked_item['item_wanted'] = item_wanted

def createItem(item, stash):
    note = item['note']
    tracked_item['note'] = note
    splitNote(note)
    tracked_item['seller_account_id'] = stash['accountName']
    tracked_item['seller_character_name'] = stash['lastCharacterName']
    tracked_item['item_id'] = item['id']
    tracked_item['icon'] = item['icon']
    # typeLine is the item name
    tracked_item['type_line'] = item['typeLine']
    tracked_item['league'] = item['league']
    tracked_item['quantity'] = item['stackSize']
    tracked_item['frame_type'] = item['frameType']
    try:
        # Tries to insert item into the database.
        insertItem(**tracked_item)
    except:
        # If item cannot be inserted into database it prints the item on the console
        print("\nERROR entering item!")
        print(tracked_item)