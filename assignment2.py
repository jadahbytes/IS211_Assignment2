import argparse
import urllib.request
import datetime
import logging

#url https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv
#url = input('Insert URL here: ')

#url_default = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"

def downloadData(url):
	response = urllib.request.urlopen(url)
	data = response.read().decode('utf-8')
	#print(data)
	return data

def processData(file_content):
	dictionary = {}
	#print(file_content)
    # [
    #	"1,Charles Paige,06/01/1963",
	#	"2,Andrew Bell,29/03/1972",
    #	...
    # 	"99,Alan Wilson,03/04/1960",
    #	"100,Austin Burgess,04/06/1979"
    # ]


	line_number = 0
	data_items = file_content.splitlines()
	for line in data_items[1:]:
		data_pieces = line
		data_pieces = data_pieces.split(',')
		# ["1", "Charles Paige", "06/01/1963"]
		line_number = line_number + 1
		#print(data_pieces)
	#	dictionary[data_pieces[0]] = (data_pieces[1]), datetime.datetime.strptime((data_pieces[2]), '%d/%m/%Y')
		try:
			dictionary[data_pieces[0]] = (data_pieces[1]), datetime.datetime.strptime((data_pieces[2]), '%d/%m/%Y')
		except ValueError:
			logging.error("Error processing line #" + str(line_number) + " for ID #" + str(data_pieces[0]))
	return dictionary

def displayPerson(id, personData):
	#print(personData)
	#return
	try:
		print("Person #: " + id + " is " + personData[id][0] + " with a birthday of " + personData[id][1].strftime(('%Y-%m-%d')))
	except:
		print("No user found with that id")


def main(url):
	logger = logging.getLogger('assignment2')
	logging.basicConfig(filename='error.log', filemode='w', level=logging.ERROR)
	# Read URL arg
	try:
		csvData = downloadData(url)
	except urllib.error.URLError:
			logging.error("URL open error. Please make sure your URL is valid, and/or your internet connection is stable.")
	personData = processData(csvData)
	#print(values)
	while True:
		id = input("ID:")
		if int(id) <= 0:
			print("You must enter a non-zero positive number")
			exit()
		else:
			displayPerson(id, personData)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
	args = parser.parse_args()
	main(args.url)
