This Scraper works by
-creating a method to scrape
-creates a new text file "MVH.txt" whenever the program is started new
-Uses requests to get the html info from the website
-Finds all the divs with the necessary class id
-Create an empty list called "listoftransactions"
-then loops through each row of data, splits the info based on the items in the string that are not needed(ex. "Hash", "(BTC)"...)
	-Then converts the string of the BTC number to a float
	-makes a list from the indexes of the row that are containing the needed information
	-then append that list into the "listoftransactions"
	
-Then sorts the "listoftransactions" by the index of the BTC amount highest to lowest.
-Appends the highest BTC hash info to the file named "MVH.txt"
-program sleeps for 60 seconds
-Does it all again on a loop until the user closes out the program