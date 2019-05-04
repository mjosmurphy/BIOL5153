#!/usr/bin/python3

import csv
from collections import defaultdict

# get the path and the filename to be used for the conversion

path = ''
filename = ''

# hardcoded value
# specifies which column contains the first species entry:
# date | site | species_1 | species_2 | ... | species_n
species_index = 2

# make string to hold the reconfigured csv file
reconfig = str()

# declare a list of the headers in the original file
headers = []

# open the file
with open((path+filename), newline = '') as csvfile:
    
    # read the data using the csv module
    data = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    
    # get the headers populate the headers object
    headers = next(data)
    
    # get the information needed to populate the reconfigured csv file, row by row
    for row in data:
        
        # the first column holds the collection date in POSIX format
        date = row[0]
        
        # the second column holds the field site
        site = row[1]
        
        # the rest of the columns hold the species (incidence) data
        species = row[species_index:]
        
        # create an iterator so i can move across columns
        j = 0
        
        # for each column
        for s in species:
            
            # save into an object x
            x = (str(date) + ',' + site + ',' + str(headers[(species_index + j)]) + ',' + str(s) + '\n')
            reconfig = reconfig + x
            j += 1

# prompt an output file name
outputfile = input('file name: ')

# indicate path and filename that reconfigured file saves to
print('saving as ' + outputfile + ' in directory: ' + path)
print('...')

# write out the reconfigured file
with open((path+outputfile), 'w') as out:
    out.write(out_header)
    out.write(reconfig)

# indicate that saving process finished
print(outputfile + ' saved successfully.')