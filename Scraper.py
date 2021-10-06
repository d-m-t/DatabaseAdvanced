import requests
from bs4 import BeautifulSoup
import re
import time


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

    file = open('MVH.txt', 'a')
    for item in listoftransactions[0]:
        file.write(str(item) + "  ")
    file.write("\n")
    file.close()
    time.sleep(60)
    scraper()


file=open('MVH.txt','w')
scraper()


