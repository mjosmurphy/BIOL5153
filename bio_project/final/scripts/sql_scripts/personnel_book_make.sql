CREATE TABLE personnel_book(
	email VARCHAR(20),
	family_name VARCHAR(20),
	given_name VARCHAR(20),
	nick VARCHAR(20),
	last_posn VARCHAR(20),
	current VARCHAR(1),
	PRIMARY KEY(email)
);


LOAD DATA LOCAL INFILE
'~/projects/BIOL5153/bio_project/final/personnel_book.csv'
INTO TABLE personnel_book
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(email,family_name,given_name,nick,last_posn,current);