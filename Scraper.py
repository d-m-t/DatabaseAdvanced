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
        # if it needs to be bases of USD then just add $ to re search and make that index a float
        row = re.split('Hash|\(BTC\)| BTCAmount|Time|Amount|\(USD\)', i.text)
        row[4] = float(row[4])
        finalrow = [row[1], row[2], row[4], row[6]]
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


