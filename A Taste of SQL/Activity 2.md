# Activity 2
Using shows.db, write a SQL query to answer each of the following questions:

1. In what Year was Jerry Seinfeld born?
2. How many shows have a perfect 10.0 rating?
3. What genres are associated with the show The Crown?
4. Who wrote Arrested Development?
5. What shows has Allison Janney starred in?

## Queries

### 1. In what Year was Jerry Seinfeld born?
```SQL
SELECT birth FROM people WHERE name = "Jerry Seinfeld";
```
	birth
	1954

### 2. How many shows have a perfect 10.0 rating?
```SQL
SELECT COUNT(*) FROM ratings WHERE rating = 10;
```
	COUNT(*)
	27

### 3. What genres are associated with the show The Crown?
```SQL
SELECT genre FROM genres where show_id =
   ...> (SELECT id FROM shows WHERE title = "The Crown");
```
	genre
	Drama
	History

### 4. Who wrote Arrested Development?
```SQL
SELECT name FROM people WHERE id =
   ...> (SELECT person_id FROM writers WHERE show_id =
   ...> (SELECT id FROM shows WHERE title = "Arrested Development"));
```
	name
	Mitchell Hurwitz

### 5. What shows has Allison Janney starred in?
```SQL
SELECT title FROM shows WHERE id IN
   ...> (SELECT show_id FROM stars WHERE person_id =
   ...> (SELECT id FROM people WHERE name = "Allison Janney"));
```
	title
	Morton & Hayes
	The West Wing
	The Richard and Judy Show
	The EcoZone Project
	Mr. Sunshine
	Mom
	The Adventures of Mr. Clown
	Break a Hip
	The Late Late Show with James Corden
	I'll Have What Phil's Having