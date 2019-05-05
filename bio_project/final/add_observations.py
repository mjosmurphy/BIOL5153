from datetime import date, datetime, timedelta
import mysql.connector
import argparse

# define acceptable Yes/No responses:
affirmation = [Y, y, YES, Yes, yes]
declination = [N, n, NO, No, no]

# define functions for identifying data to be added:
def add_species(*args):
	# Add species one by one
	i = int()
	i = 0
	print("Now add species observations:")
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
		if(more_test in affirmation):
			i=0

		# if not, close the loop and return the values
		else:
			i+=1
			#print(name)
			#print(n)
			return(name,n)

def add_weather(*args):
	# Add weather information
	print("Now add weather for the current observation:")
	weather["cloud_cover"] = input("Cloud cover: ")
	weather["precipitation"] = input("Describe precipitation: ")
	weather["temperature"] = input("Temperature (in deg. C): ")
	weather["wind_speed"] = input("Wind speed (in km/h): ")
	weather["data_source"] = input("Where did you get these data? ")
	return(weather)

def add_notes(*args):
	# Add optional notes for this entry
	i = int()
	ans = chr()
	i = 0
	while (i<1):
		note = input("Notes for this entry: /n")
		print("Your notes for this entry: /n" note)
		ans = input("Is this correct?")
		if ans in affirmation:
			i += 1
			return(note)
		elif ans in declination:
			i = 0
			print("Note deleted; re-enter your notes ...")
		else:
			print("Error! Re-enter your notes.")
			i = 0


# define function for committing data to the database:
def input_species(species):
	cnx = mysql.connector.connect(user='mjmurphy', database='butterfly')
	cursor = cnx.cursor()

	# set up new observation
	add_observation = ("INSERT INTO observation_book "
	               "(date, site, name, n) "
	               "VALUES (%s, %s, %s, %s, %s)")

	insert_observation = species
	# begin insert observation_book
	cursor.execute(add_observation)

	# commit new data and close the connection
	cnx.commit()
	cursor.close()
	cnx.close()

def input_weather(weather):
	cnx = mysql.connector.connect(user='mjmurphy', database='butterfly')
	cursor = cnx.cursor()

	# set up new observation
	insert_weather = ("INSERT INTO observation_book "
	               "(date, cloud_cover, precipitation, temperature, wind_speed, data_source)"
	               "VALUES (%s, %s, %s, %s, %s, %s)")

	# begin insert observation_book
	cursor.execute(insert_weather)

	# add observation data
	
	cursor.execute(insert_weather)

	# commit new data and close the connection
	cnx.commit()
	cursor.close()
	cnx.close()

def input_notes(note):
	cnx = mysql.connector.connect(user='mjmurphy', database='butterfly')
	cursor = cnx.cursor()

	# set up new observation
	add_notes = ("INSERT INTO note_book "
	               "(ID,note)"
	               "VALUES (%s, %s)")
	
	insert_notes = note
	# begin insert note_book
	cursor.execute(insert_notes)

	# add observation data
	cursor.execute(insert_notes)

	# commit new data and close the connection
	cnx.commit()
	cursor.close()
	cnx.close()

# add object names ...
print("Now to add new observations")
name = []
n = []
weather = {
	"cloud_cover" : str(),
	"precipitation" : str(),
	"temperature" : int(),
	"wind_speed" : int(),
	"data_source" : str()
}

date = input("Date collected ( format: YYYY-MM-DD ): ")
site = input("Field site where collected: ")

print("You collected these data on " + date + " at " + site + "\n\n\n")
ans = input("Is this correct? (Y/n): ")

add_species()

add_weather()

print(name)
print(n)
print(weather)



# input the observations
print("Inputting new observation(s) ... ")
# add_observation(date, site, name, n)
print("Observation(s) added to the database!")