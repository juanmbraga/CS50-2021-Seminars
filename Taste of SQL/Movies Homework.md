# Movies Homework
Run wget https://cdn.cs50.net/2021/x/seminars/sql/movies.db

Write a SQL query to answer each of the following questions.

	1. What are the titles of all movies released in 2008?
	2. In what year was Emma Stone born?
	3. How many movies have an IMDb rating of 10.0?
	4. What are the titles and release years of all Harry Potter movies, in chronological order?
	5. Who starred in Toy Story?
	6. What are the movies in which both Johnny Depp and Helena Bonham Carter starred?

# Queries

## 1. What are the titles of all movies released in 2008?
```SQL
SELECT title FROM movies WHERE year = 2008;
```
	(A long list)

## 2. In what year was Emma Stone born?
```SQL
SELECT birth FROM people WHERE name = "Emma Stone";
```
	Birth
	1988

## 3. How many movies have an IMDb rating of 10.0?
```SQL
SELECT COUNT(*) FROM ratings WHERE rating = 10;
```
	COUNT(*)
	45
	
## 4. What are the titles and release years of all Harry Potter movies, in chronological order?
```SQL 
SELECT title, year FROM movies WHERE title LIKE "%Harry Potter%" ORDER BY year;
```
	title | year
	Harry Potter and the Sorcerer's Stone | 2001
	Harry Potter and the Chamber of Secrets | 2002
	Harry Potter and the Prisoner of Azkaban | 2004
	Harry Potter and the Goblet of Fire | 2005
	Harry Potter and the Order of the Phoenix | 2007
	Harry Potter and the Half-Blood Prince | 2009
	Harry Potter and the Deathly Hallows: Part 1 | 2010
	Creating the World of Harry Potter, Part 4: Sound and Music | 2010
	The Seekers Guide to Harry Potter | 2010
	Harry Potter and the Deathly Hallows: Part 2 | 2011
	Harry Potter and the Untold Stories of Hogwarts | 2012
	Harry Potter: A History of Magic | 2017
	The Harry Potter Saga Analyzed | 2018
	Darla's Book Club: Discussing the Harry Potter Series | 2020

## 5. Who starred in Toy Story?
```SQL
SELECT name FROM people WHERE id IN
   ...> (SELECT person_id FROM stars WHERE movie_id =
   ...> (SELECT id FROM movies WHERE title = "Toy Story"));
```
	name
	Tom Hanks
	Tim Allen
	Jim Varney
	Don Rickles

## 6. What are the movies in which both Johnny Depp and Helena Bonham Carter starred?
```SQL
SELECT * FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE movie_id IN (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = "Johnny Depp")) AND person_id = (SELECT id FROM people WHERE name = "Helena Bonham Carter"));
```

Translation: Show info about movies which ID is in (Find movies from stars table which movieID in in (list of movieID in which Johnny Depp starred) and have the person id of Helena Bonham Carter).

	id | title | year
	121164 | Corpse Bride | 2005
	367594 | Charlie and the Chocolate Factory | 2005
	408236 | Sweeney Todd: The Demon Barber of Fleet Street | 2007
	1014759 | Alice in Wonderland | 2010
	1077368 | Dark Shadows | 2012
	2567026 | Alice Through the Looking Glass | 2016

