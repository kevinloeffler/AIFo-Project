ALTER TABLE title_ratings
ADD CONSTRAINT fk_ratings_basics
	FOREIGN KEY (tconst) REFERENCES title_basics (tconst)
	ON DELETE CASCADE
;

ALTER TABLE title_crew
ADD CONSTRAINT fk_crew_basics
	FOREIGN KEY (tconst) REFERENCES title_basics (tconst)
	ON DELETE CASCADE
;

ALTER TABLE title_principals
ADD CONSTRAINT fk_principals_basics
	FOREIGN KEY (tconst) REFERENCES title_basics (tconst)
	ON DELETE CASCADE
;

ALTER TABLE title_principals
ADD CONSTRAINT fk_principals_names
	FOREIGN KEY (nconst) REFERENCES name_basics (nconst)
	ON DELETE CASCADE
;