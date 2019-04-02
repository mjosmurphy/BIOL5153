# read in watermelon gff
# " " watermelon fsa
# extract all the features from the genome

# call this parse_GFF

dirname = "/home/mjmurphy/projects/BIOL5153/watermelon_files/"

# open the required files
FASTA_name = dirname+"watermelon.fsa"
GFF_name = dirname+"watermelon.gff"

FASTA_open = open(FASTA_name)
GFF = open(GFF_name, "r")

# strip out the header from the sequence
# the variable 'genome' holds the genome sequence
FASTA = FASTA_open.read()

header = FASTA.split("\n")[0]
genome = FASTA.split("\n")[1]

print(header)



for line in GFF:
	#skip blank lines

	#remove the line breaks
	line = line.rstrip("\n")
	# split the line by tabs
	line = line.split("\t")
	# get position of beginning of feature
	start = int(line[3])-1
	# get position of end of feature
	end = int(line[4])-1
	# extract the DNA sequence from the genome for this feature
	substring = genome[start:end]
#	print(substring)

	# calculate the GC content for this feature
	# calculate the number of A, C, G, T
	substring_length = float(len(substring))
	numA = float(substring.count('A'))
	numC = float(substring.count('C'))
	numG = float(substring.count('G'))
	numT = float(substring.count('T'))

	# calculate the frequency of A, C, G, T
	freqA = numA/substring_length
	freqC = numC/substring_length
	freqG = numG/substring_length
	freqT = numT/substring_length
	GC_content = freqC+freqG
	GC_content = GC_content*100
	GC_cont_str = round(GC_content,2)
	GC_cont_str = str(GC_cont_str)

	# print the DNA sequence for this feature
	print("feature position: " + str(start) + " -- " + str(end))
	print("feature length: " + str(substring_length)[0:-2] + " bases")
	print("GC content: " + GC_cont_str + "%")
#	print("GC content: " + str(GC_content) + "%")
	print("\n")

FASTA_open.close()
GFF.close()