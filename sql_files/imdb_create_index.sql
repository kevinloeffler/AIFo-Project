CREATE INDEX primaryname_lower_name_basics ON name_basics (lower(primaryName));

CREATE INDEX title_const_title_basics ON title_basics (tconst);

CREATE INDEX movie_year_title_basics ON title_basics (startYear);

CREATE INDEX rating_desc_title_ratings ON title_ratings (numVotes DESC, averageRating DESC);

CREATE INDEX primarytitle_title_basics ON title_basics (primaryTitle);

CREATE INDEX category_title_principals ON title_principals (category);