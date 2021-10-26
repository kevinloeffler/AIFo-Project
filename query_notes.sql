
------- SQL Notes

-- Movie Info Query

SELECT tb.startyear, tb.runtimeminutes, tb.genres, nb.primaryname
FROM title_basics AS tb
INNER JOIN title_crew AS tc
ON tb.tconst = tc.tconst
LEFT JOIN name_basics AS nb
ON tc.directors = nb.nconst
WHERE lower(tb.primarytitle) = 'call me by your name'
AND tb.titletype = 'movie';

-- Director Query

SELECT tb.primarytitle, tr.averagerating
FROM title_basics AS tb
INNER JOIN title_ratings tr ON (tb.tconst = tr.tconst)
INNER JOIN (
  SELECT tp.tconst, tp.category
  FROM title_principals AS tp
  WHERE nconst = (
    SELECT nb.nconst
    FROM name_basics AS nb
    WHERE lower(nb.primaryname) = 'christopher nolan'
    AND nb.primaryprofession LIKE '%director%'
  )
) AS principals ON (tb.tconst = principals.tconst)
WHERE tb.titletype = 'movie'
ORDER BY tr.averagerating DESC;

--------

SELECT tb.primarytitle
FROM title_basics AS tb
INNER JOIN title_ratings tr ON (tb.tconst = tr.tconst)
INNER JOIN (
  SELECT tp.tconst, tp.category
  FROM title_principals AS tp
  WHERE nconst = (
    SELECT nb.nconst
    FROM name_basics AS nb
    WHERE primaryname = 'Joel Coen'
    LIMIT 1
  )
) AS principals ON (tb.tconst = principals.tconst)
WHERE tb.titletype = 'movie'
ORDER BY tr.averagerating DESC;

--------

SELECT tb.tconst, tb.primarytitle,
FROM title_basics AS tb
INNER JOIN (
  SELECT tp.tconst, tp.category
  FROM title_principals AS tp
  WHERE nconst = (
    SELECT nb.nconst
    FROM name_basics AS nb
    WHERE primaryname = 'Christopher Nolan'
    LIMIT 1
  )
) AS principals ON (tb.tconst = principals.tconst);

--------


SELECT primarytitle
FROM title_basics


SELECT nconst
FROM name_basics
WHERE primaryname = 'Christopher Nolan';
