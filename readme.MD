redisreInstallation:
Ubuntu 20.04.3
Virtual Box extensions 6.1.26r145957
1400MB Ram/upped to 4gb on 5/11
15GB Hard Disk
Go to folder in VirtualBox VMS if needed to update, backup, change or migrate to another version
to find packages that are installed : /usr/lib/python3/dist-packages

Python Packages(along with python3):
bs4
requests
re
pymongo
redis

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
localhost:27017
compass
dom
Start:sudo systemctl start mongod / mongosh
verify statuts: sudo systemctl status mongod
stop:sudo systemctl stop mongod

Scraper now scrapes the data and inserts it into the Bitcoin database under the collection Top Transactions.
The Id is the Hash number.

Redis Install
127.0.0.1:6379
Port: 6379
PID:4917
install redis package on pycharm and ubuntu

Check status:systemctl status redisv
Start Redis -   redis-server
Open command line interface -   redis-cli
Check if connected -   redis-cli ping(pong)
Empty Database -   FLUSHALL ASYNC

Redis hashes to add
HELP @string,sets etc for commands

Docker
 sudo systemctl status docker
 sudo systemctl enable docker

to search for image- docker search <name>
To run container based on docker image -  docker run <options> <image-name>
TO run it in the background use -d - docker run -d redis
to run a specific version add :<version> - docker run -d redis:3.2 or redis:latest
list all runing containers, images used and uptime - docker ps-a
to view all iimages on local machine - docker images
remove a container: docker rm containterID
syssystem


Redis-cli
Quit redis-cli : quit
To stop the redis container : docker stop my-redis