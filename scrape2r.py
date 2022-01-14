import requests
from bs4 import BeautifulSoup
import re
import time
import pymongo
import redis

#This connects to Mongodb and adds top hash to it every minute
# myclient=pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient["Bitcoin"]
# mycol=mydb["Top Transactions"]

r = redis.Redis(host='localhost', port=6379)
def scraper():
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    response = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.text, features="html.parser")
    # print(soup.prettify())
    transactions = soup.find_all("div", {"class": "sc-1g6z4xm-0 hXyplo"})

    listoftransactions = []

    for i in transactions:
        row = re.split('Hash|\(BTC\)| BTCAmount|Time|Amount|\(USD\)\$', i.text)
        Hash=row[1]
        Time=row[2]
        BTC = float(row[4])
        USD = float(row[6].replace(',', ''))
        finalrow = [Hash,Time,BTC,USD]
        listoftransactions.append(finalrow)

    listoftransactions.sort(key=lambda x: x[2], reverse=True)
    print(listoftransactions[0])
    Hash1=listoftransactions[0][0]
    Time1=listoftransactions[0][1]
    BTC1=listoftransactions[0][2]
    USD1=listoftransactions[0][3]
    r.hset(Hash1, "BTC", BTC1)
    r.hset(Hash1, "Time", Time1)
    r.hset(Hash1, "USD", USD1)
    # r.expire(Hash1, 10)
    print(r.hgetall('Hash'))
    # mydict = {"_id": Hash1, "Time(h/m)": Time1,"BTC Value":BTC1,"USD Value":USD1}
    # x=mycol.insert_one(mydict)
    # if(x):
    #     print("Added")
    # else:
    #     print("Not Added")

# Writes top has to file(not needed)
    # file = open('MVH.txt', 'a')
    # for item in listoftransactions[0]:
    #     file.write(str(item) + "  ")
    # file.write("\n")
    # file.close()

# Sleep timer and Recursion for scraper
    time.sleep(60)
    scraper()


# file=open('MVH.txt','w')
scraper()


