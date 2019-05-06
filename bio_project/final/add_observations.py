from datetime import date, datetime, timedelta
from collections import defaultdict
import mysql.connector
import argparse


# define acceptable Yes/No responses:
affirmation = ['Y', 'y', 'YES', 'Yes', 'yes']
declination = ['N', 'n', 'NO', 'No', 'no']
# initialize standard iterator
i = int()
date = str()
site = str()
name = []
n = []
weather = {
	"cloud_cover" : str(),
	"precipitation" : str(),
	"temperature" : int(),
	"wind_speed" : int(),
	"data_source" : str()
}

## Interactive data addition

# populates date and site info there
def add_collection_info(*args):
	# set iterator to 0; loop execution will depend on user input
	i = 0
	while (i<1):

		# user input: date and site information
		date = input("Date collected ( format: YYYY-MM-DD ): ")
		site = input("Field site where collected: ")

		# confirm user input for date and site information
		print("You collected these data on " + date + " at " + site + "\n")
		ans = input("Is this correct? (Y/n): ")

		# if not correct, prompt to re-enter (go to beginning of loop)
		if ans in affirmation:
			i+= 1
			return(date,site)
		else:
			i = 0

# creates 2 lists: one of species, one of # observed
def add_species(*args):
	# Add species one by one
	i = int()
	i = 0
	while (i<1):
		# for a single species, input the name and # observed:
		sp_name = ""
		sp_name0 = input("Species name: ")
		for x in sp_name0:
			sp_name += x
		sp_n = ""
		sp_n0 = input("# observed: ")
		for x in sp_n0:
			sp_n += x

		# extend the name and number lists:
		name.append(sp_name)
		n.append(sp_n)

		# print off the list of all species and numbers:

		# ask whether this is all
		more_test = input("Any more species to add? (Y/n) ")

		# if so, then keep the loop open
		if(more_test == 'Y'):
			i=0

		# if not, close the loop and return the values
		else:
			i+=1
			#print(name)
			#print(n)
			return(name,n)

# populates weather dictionary for observation
def add_weather(*args):
	# Add weather information
	weather["cloud_cover"] = input("Cloud cover: ")
	weather["precipitation"] = input("Describe precipitation: ")
	weather["temperature"] = input("Temperature (in deg. C): ")
	weather["wind_speed"] = input("Wind speed (in km/h): ")
	weather["data_source"] = input("Data source: ")
	return(weather)

# allows user to add in notes
def add_notes(*args):
	# Add optional notes for this entry
	i = int()
	ans = str()
	i = 0
	while (i<1):
		note = input("Notes for this entry: ")
		print("Your note: " + "\n" + note)
		ans = input("Is this correct? (Y/n) ")
		if ans in affirmation:
			i += 1
			return(note)
		elif ans in declination:
			i = 0
			print("Note deleted; re-enter your notes ...")
# define function for committing data to the database:

# inserts weather data into the database
def enter_weather(weather):
	cnx = mysql.connector.connect(user='mjmurphy', database='butterfly')
	cursor = cnx.cursor()

	# set up new observation
	insert_weather = ("INSERT INTO observation_book "
	               "(date, cloud_cover, precipitation, temperature, wind_speed, data_source)"
	               "VALUES (%s, %s, %s, %s, %s, %s)")

	# add date and weather data
	data_weather = (date, weather['cloud_cover'], weather['precipitation'], weather['tempterature'],weather['wind_speed'],weather['data_source'])

	# insert new weather data
	cursor.execute(insert_weather, data_weather)

	cnx.commit()
	cursor.close()
	cnx.close()


print("======= Add collection info =======")
print("\n")
add_collection_info()
print("\n\n")

print("=========== Add species ===========")
print("\n")
add_species()
print("\n\n")

print("=========== Add weather ===========")
print("\n")
add_weather()
print("\n\n")

print("=========== Add notes =============")
print("\n")
add_notes()
print("\n\n")