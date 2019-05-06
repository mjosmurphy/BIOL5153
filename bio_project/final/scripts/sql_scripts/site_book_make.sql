CREATE TABLE site_book(
	site_nick VARCHAR(45),
	site_name VARCHAR(45),
	latitude FLOAT(6,4),
	longtiude FLOAT(6,4),
	PRIMARY KEY(site_nick)
);


LOAD DATA LOCAL INFILE
'~/projects/BIOL5153/bio_project/final/site_book.csv'
INTO TABLE site_book
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(site_nick,site_name,latitude,longtiude);