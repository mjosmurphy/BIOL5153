import argparse
import csv
from Bio import SeqIO

# create an ArgumentParser object ('parser') that will hold all the information necessary
# to parse the command line
parser = argparse.ArgumentParser(description = "automatically parses a GFF file")

# add positional (required) arguments
parser.add_argument( "-f", "--FASTA", help = "the name of the FASTA file" )
parser.add_argument( "-g", "--GFF", help = "the name of the GFF file" )
# add optional arguments

args = parser.parse_args()

# Get data
# Read in FASTA file using the SeqIO module

genomes = []
for record in SeqIO.parse(args.FASTA, "fasta"):
	genomes = str(genomes) + str(record.seq)

# Read in GFF file using the csv reader module
with open(args.GFF, newline='') as gff:
    annotation = csv.reader(gff, delimiter='\t')
    for row in annotation:
    	substring = genomes[int(row[3]):int(row[4])]
    	substring_length =int(row[4])-int(row[3])
    	substring_length = float(len(substring))
 
    	numC = float(substring.count('C'))
    	numG = float(substring.count('G'))

    	freqC = numC/substring_length
    	freqG = numG/substring_length

    	GC_content = round(((freqC+freqG)*100),2)
    	GC_cont_str = str(GC_content)

    	print("feature position: " + str(row[3]) + " -- " + str(row[4]))
    	print("feature length: " + str(substring_length) + " bases")
    	print("GC content: " + GC_cont_str + "%")
    	print("\n")
