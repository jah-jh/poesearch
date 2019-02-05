#!/usr/bin/python3.6
import argparse
import requests
import mysql.connector
import time
import sys
import json

parser = argparse.ArgumentParser()
parser.add_argument("--iname", help="Item name")
parser.add_argument("--scount", help="Count of sockets")
parser.add_argument("--scolors", help="Socket`s colors. G, W, R, B, A. Stands for: green, white, red, blue, abyss (though not a colour but type).")
parser.add_argument("--links", help="Number of minimum links")
args = parser.parse_args()




item_name = args.iname
#item_name = "<<set:MS>><<set:M>><<set:S>>" + args.iname
print(item_name)

cnx = mysql.connector.connect(host='127.0.0.1',user='poe',password='wantmore',database='POEID')
cursor = cnx.cursor()





PRICE_DICT = {}

def get_price(dirty_price, ex_price):
    diasambled_price = dirty_price.split(" ")
    if diasambled_price[2] == "exa":
        price = float(diasambled_price[1]) * int(ex_price)
        return(price)
    else:
        price = diasambled_price[1]
        return(price)




while True:
    OUTPUT_FILE = open('/home/devyaterikovrg/poedsearch/output.log','a')
    cnx = mysql.connector.connect(host='127.0.0.1',user='poe',password='wantmore',database='POEID')
    cursor = cnx.cursor()
    cursor.execute('SELECT CHANGE_ID from CHANGE_ID order by ID DESC  LIMIT 1;')
    cid = cursor.fetchone()
    print(cid[0])
    url = "http://api.pathofexile.com/public-stash-tabs?id=" + str(cid[0])
    r = requests.get(url).json()
    for stashes in r["stashes"]:
        for item_list in stashes["items"]:
            #print(item_list)
            if item_list['name'] == item_name and item_list['league'] == "Betrayal":
                #OUTPUT_FILE.write(str(item_list))
                #json.dump(item_list,OUTPUT_FILE)
                OUTPUT_FILE.write("\n")
                if "note" in item_list:
                    print(get_price(item_list["note"],150))
                    PRICE_DICT['price'] = str(get_price(item_list["note"], 150))
                    PRICE_DICT['item_name'] = item_name
                    json.dump(PRICE_DICT, OUTPUT_FILE)
                    price_dirty = item_list["note"]
                else:
                    price_dirty = "" 
                print(item_list["name"] + "-----SOLD BY------" + stashes["accountName"] + "  PRICE: " + str(price_dirty))
                #print(item_list["sockets"])
                ######### WORK WITH SOCKETS ###################
                if len(item_list["sockets"]) == int(args.scount):
                    for sockets in item_list["sockets"]:
                        sockets_link = []
                        sockets_link.append(sockets["group"])
                        #print(sockets["group"])
                    #print(sockets_link)
    OUTPUT_FILE.close()
    time.sleep(5)
    cnx.close()
