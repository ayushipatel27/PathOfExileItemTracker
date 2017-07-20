'''
Created on Jul 11, 2017

@author: Craig Brewton
         CS421
         POEparser
         071117
         The purpose of this project is to read JSON files from a URL and parse that file
         into a python dictionary then check it for specific currency items that the user is
         searching for in the application.
'''

import contextlib, urllib.request, json
#from re import search

print("Hey Craig!\n")#test statement
#a module for interfacing with the rest of the application and getting the item of interest, pass the item name to the search method
def get_item():
    checkbit = 0
    while checkbit == 0:
        #this will be removed for production and the method will have a parameter received from the user interface / database
        item = input("Please enter the item you are looking for: ")#this needs to be passed to the search
        #a list of acceptable item names that will be taken
        item_list = ['Albino Rhoa Feather', 'Apprentice Cartographer\'s Seal', 'Apprentice Cartargrapher\'s Sextant', 'Armourer\'s Scrap',
                     'Blacksmith\'s Whetstone', 'Blessed Orb', 'Blessing of Chayula', 'Blessing of Esh', 'Blessing of Tul', 'Blessing of Uul-Netol', 
                     'Blessing of Xoph', 'Cartographer\'s Chisel', 'Chaos Orb', 'Chromatic Orb', 'Divine Orb', 'Exhalted Orb', 'Gemcutter\'s Prism', 
                     'Glassblower\'s Bauble', 'Jeweller\'s Orb', 'Journeyman Cartographer\'s Seal', 'Journeyman Cartographer\'s Sextant', 'Master Cartographer\'s Seal', 
                     'Master Cartographer\'s Sextant', 'Mirror of Kalandra', 'Orb of Alchemy', 'Orb of Alteration', 'Orb of Augmentation', 'Orb of Chance', 
                     'Orb of Fusing', 'Orb of Regret', 'Orb of Scouring', 'Orb of Transmutation', 'Perandus Coin', 'Portal Scroll', 'Prophecy', 'Regal Orb', 
                     'Scroll of Wisdom', 'Silver Coin', 'Stacked Deck', 'Unshaping Orb', 'Vaal Orb', 'Alchemy Shard', 'Alteration Shard', 'Scroll Fragment', 
                     'Splinter of Chayula', 'Splinter of Esh', 'Splinter of Tul', 'Splinter of Uul-Netol', 'Splinter of Xoph', 'Transmutation Shard', 
                     'Perandus Coin', 'Eternal Orb', 'Imprint', 'The Emperor\'s Trove']
        #check to verify the item selection for search
        if any(i in item for i in item_list):
            checkbit = 1
        else:
            print('Invalid choice! Try again.')
            checkbit = 0
    return item

#the module that opens the url, reads the json and decodes it, then passes that to the search method
def get_json():
    url = "http://api.pathofexile.com/public-stash-tabs"#this url may need to be altered....dont think its getting the most current stash list
    with contextlib.closing(urllib.request.urlopen(url)) as x:
        data2 = x.read()
        output2 = json.loads(data2)
    return output2
    
#a search module that checks the json for the item of interest, it will get a string and the json as parameters
def search_json(output, item):
    #need to be careful with the varying lengths of lists for stashes and items...keep getting 'index out of range'
    #the following code seems to work properly....tested with 'Orb of Chance'
    for i in range(len(output['stashes'])):
        for a in range(len(output['stashes'][i]['items'])):
            print(output['stashes'][i]['items'][a]['typeLine'])#test output.....worried about 'typeline' not always being the right value....check with bryan
            if item == output['stashes'][i]['items'][a]['typeLine']:
                print(i)#test output
                print(a)#test output
                print('It\'s a Match')#test output
            else:
                print(i)#test output
                print(a)#test output
                print('Item not found')#test output
                
    '''the following method was not working...almost ALWAYS returned true even when it should not
    print('Almost there...')#test output
    print(item + 'is what we are searching for...')#test output
    for b in range(len(output['stashes'])):#this cycles through 608 stashes but it skips some numbers....
        for n in range(len(output['stashes'][b]['items'])):#i think the stash loop skips those stashes because their item list length is null
            print(output['stashes'][b]['items'][n]['typeLine'])#test output
            if any(i in item for i in output['stashes'][b]['items'][n]['typeLine']):#always evaluating true....????????????
                print(b)#test output
                print(n)#test output
                print("Success")#test output
            else:
                print(b)#test output
                print(n)#test output
                print("Item not found")#test output
    '''
#main method to run program, will eventually need to accept arguments from user interface and/or database
if __name__ == '__main__':
    output3 = get_json()
    item2 = get_item()
    search_json(output3, item2)
    print("\nfinished!")#test statement

#******************************************************************************************************************
#**************************************all junk and notes below here***********************************************
#******************************************************************************************************************

'''
from pprint import pprint
import contextlib
import urllib.request, json
print("Hey Craig!")
print()
item = input("Please enter the item you are looking for: ")#this needs to be passed to the search
file = open("C:/Users/Craig/Documents/School/UAB/Summer 2017/CS421 - Advanced Web Dev/POE/sampleOutput.txt", "w")
url = "http://api.pathofexile.com/public-stash-tabs"
data = urllib.request.urlopen(url).read()
output = json.loads(data)
print(output['next_change_id'])#works to here
print(list(output['stashes'][0]['accountName']))#works to here, prints first account name, but it prints as a character list
print(output['stashes'][0]['accountName'])#works to here, prints first account name as a string
print(output['stashes'][3]['items'])#works to here, prints all of items
print(output['stashes'][3]['items'][0])#works to here, prints the first item in items
print(output['stashes'][3]['items'][0]['typeLine'])#works to here, prints the value for the key 'typeLine'...mission accomplished for now

'''

#need to read in JSON
    #source URL = http://api.pathofexile.com/public-stash-tabs
    #this may need some other details to get the latest list
    #need latest 'change id'

#need to parse JSON for objects of interest

#what are the items of interest
    #Orbs and Scrolls
        #Albino Rhoa Feather
        #Apprentice Cartographer's Seal
        #Apprentice Cartargrapher's Sextant
        #Armourer's Scrap
        #Blacksmith's Whetstone
        #Blessed Orb
        #Blessing of Chayula
        #Blessing of Esh
        #Blessing of Tul
        #Blessing of Uul-Netol
        #Blessing of Xoph
        #Cartographer's Chisel
        #Chaos Orb
        #Chromatic Orb
        #Divine Orb
        #Exhalted Orb
        #Gemcutter's Prism
        #Glassblower's Bauble
        #Jeweller's Orb
        #Journeyman Cartographer's Seal
        #Journeyman Cartographer's Sextant
        #Master Cartographer's Seal
        #Master Cartographer's Sextant
        #Mirror of Kalandra
        #Orb of Alchemy
        #Orb of Alteration
        #Orb of Augmentation
        #Orb of Chance
        #Orb of Fusing
        #Orb of Regret
        #Orb of Scouring
        #Orb of Transmutation
        #Perandus Coin
        #Portal Scroll
        #Prophecy
        #Regal Orb
        #Scroll of Wisdom
        #Silver Coin
        #Stacked Deck
        #Unshaping Orb
        #Vaal Orb
    #Shards and Fragments
        #Alchemy Shard
        #Alteration Shard
        #Scroll Fragment
        #Splinter of Chayula
        #Splinter of Esh
        #Splinter of Tul
        #Splinter of Uul-Netol
        #Splinter of Xoph
        #Transmutation Shard
    #League Specific Items
        #Perandus Coin
    #Discontinued Items
        #Eternal Orb
        #Imprint
        #The Emperor's Trove

#what it looks like in the JSON
    #"typeLine":"Orb of Alchemy"
    #but names will also appear in other segments such as: "descrText":"A stack of 20 shards becomes an Orb of Alchemy."
    #"typeLine":"Alteration Shard"
    #"typeLine":"Jeweller's Orb"
    
#will need to collect all (or most) of the attributes for that particular item to display for user
    #primary attributes of interest
        #name of item ->
        #whether it is currency or not -> "frameType":5
        #public or not ->
    #secondary attributes of interest
        #slots ->
        #stash id ->
        
#will need a unit test for each item