import time
import pymongo
import redis

# Make a script that gets the data from redis and sends it to mongodb

#Making the needed connections
r = redis.StrictRedis(host='localhost', port=6379,decode_responses=True)

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bitcoin666"]
mycol=mydb["TopTransactions"]

for key in r.keys(pattern="*"):
    Hash = key
    BTC=float(r.hvals(key)[0])
    Time=str(r.hvals(key)[1])
    USD=float(r.hvals(key)[2])
    print(USD)
    mydict = {"_id": Hash, "Time(h/m)": Time,"BTC_Value":BTC,"USD_Value":USD}
    x = mycol.insert_one(mydict)
    if(x):
        print("Successfully scraped and added to DB")
    else:
        print("Failed to add value to DB")