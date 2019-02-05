#!/usr/bin/python3.6
import mysql.connector
import requests
import datetime
url = "http://api.pathofexile.com/public-stash-tabs"

BASE_ID = "327385650-338914419-320052547-366853283-346648115"
base_url = url + "?id=" + BASE_ID

r = requests.get(base_url).json()
#print(r)
FIRST_ID = (r["next_change_id"])
print(FIRST_ID)

cnx = mysql.connector.connect(host='127.0.0.1',user='poe',password='wantmore',database='POEID')
cursor = cnx.cursor()


url2 = "http://api.pathofexile.com/public-stash-tabs?id=" + FIRST_ID
print(url2)
r = requests.get(url2).json()
SECOND_ID = (r["next_change_id"])
print(SECOND_ID)
cid = SECOND_ID
while True:
    url = "http://api.pathofexile.com/public-stash-tabs?id=" + cid
    print(requests.get(url).status_code)
    r = requests.get(url).json()
    cid = r["next_change_id"]
    added = datetime.datetime.now().replace(microsecond=0)
    print(cid + "    " + str(added))
    ID_TO_DB = ('INSERT INTO CHANGE_ID (CHANGE_ID,ADDED) VALUES(' + "'" + str(cid)+ "'"+','+ "'" + str(added) + "'" +  ');')
    cnx = mysql.connector.connect(host='127.0.0.1',user='poe',password='wantmore',database='POEID')
    cursor = cnx.cursor()
    print(ID_TO_DB)
    cursor.execute(ID_TO_DB)
    cnx.commit()
    cnx.close()
