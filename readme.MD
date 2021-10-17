Installation:
Ubuntu 20.04.3
Virtual Box extensions 6.1.26r145957
1400MB Ram
15GB Hard Disk
Go to folder in VirtualBox VMS if needed to update, backup, change or migrate to another version
to find packages that are installed : /usr/lib/python3/dist-packages

Python Packages(along with python3):
bs4
requests
re
pymongo

Scraper:
-creating a method to scrape
-creates a new text file "MVH.txt" whenever the program is started new
-Uses requests to get the html info from the website
-Finds all the divs with the necessary class id
-Create an empty list called "listoftransactions"
-then loops through each row of data, splits the info based on the items in the string that are not needed(ex. "Hash", "(BTC)"...)
	-Then converts the string of the BTC number and USD to a float
	-makes a list from the indexes of the row that are containing the needed information
	-then append that list into the "listoftransactions"
	
-Then sorts the "listoftransactions" by the index of the BTC amount highest to lowest.
-Appends the highest BTC hash info to the file named "MVH.txt"
-program sleeps for 60 seconds
-Does it all again on a loop until the user closes out the program


Mongo Install:
Mongo v5.0.3
port:27017

Start:sudo systemctl start mongod / mongosh
verify statuts: sudo systemctl status mongod
stop:sudo systemctl stop mongod

Scraper now scrapes the data and inserts it into the Bitcoin database under the collection Top Transactions.
The Id is the Hash number.
