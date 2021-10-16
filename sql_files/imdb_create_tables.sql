CREATE TABLE title_ratings (
	tconst TEXT PRIMARY KEY,
	averageRating FLOAT(1),
	numVotes INTEGER
);

CREATE TABLE title_crew (
	tconst TEXT PRIMARY KEY,
	directors TEXT,
	writers TEXT
);

CREATE TABLE title_basics (
	tconst TEXT PRIMARY KEY,
	titleType TEXT,
	primaryTitle TEXT,
	originalTitle TEXT,
	isAdult BOOLEAN,
	startYear TEXT,
	endYear TEXT,
	runtimeMinutes TEXT,
	genres TEXT
);

CREATE TABLE name_basics (
	nconst TEXT PRIMARY KEY,
	primaryName TEXT,
	birthYear TEXT,
	deathYear TEXT,
	primaryProfession TEXT,
	knownForTitles TEXT
);

CREATE TABLE title_principals (
	tconst TEXT,
	ordering INTEGER,
	nconst TEXT,
	category TEXT,
	job TEXT,
	characters TEXT,
	PRIMARY KEY(tconst, ordering)
);
