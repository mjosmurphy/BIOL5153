from datetime import date, datetime, timedelta
import mysql.connector
import argparse

# define acceptable Yes/No responses:
affirmation = [Y, y, YES, Yes, yes]
declination = [N, n, NO, No, no]

# define functions for identifying data to be added:
def add_species()
	# Add species one by one
	i = int()
	i = 0
	print("Now add species observations:")
	while (i<1):
		sp_name = input("Species name: ")
		sp_n = input("# observed: ")
		name.extend(name,sp_name)
		n.extend(n,sp_n)
		print("species" + "\t" + "n")
		for j in name:
			print(name[j] + ": " + n[j])
		more_test = input("Any more species to add? (Y/n")
		if more_test in affirmation:
			i = 0
		else:
			i += 1
			species = {
				"name" = name,
				"n" = n
			}
			return(species)

def add_weather()
	# Add weather information
	print("Now add weather for the current observation:")
	cloud_cover = input("Cloud cover: ")
	precipitation = input("Describe precipitation: ")
	temperature = input("Temperature (in deg. C): ")
	wind_speed = input("Wind speed (in km/h): ")
	data_source = input("Where did you get these data? ")
	weather = {
		"cloud_cover" : cloud_cover,
		"precipitation" : precipitation,
		"temperature" : temperature,
		"wind_speed" : wind_speed,
		"data_source" : data_source
	}
	return(weather)

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

print("Now to add new observations")

date = input("Date collected ( format: YYYY-MM-DD ): ")
site = input("Field site where collected: ")

print("You collected these data on " + data + "at " + site + "\n\n\n")
ans = input("Is this correct? (Y/n")

if ans in affirmation:
	add_species()
elif ans in declination:
	# this will be fixed ... (loop back to re-enter)
else:
	# return an error and loop back

# add the observations
print("Adding observation(s) ... ")
add_observation(date, site, name, n)
print("Observation(s) added!")

ans = str()