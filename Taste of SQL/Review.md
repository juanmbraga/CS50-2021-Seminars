# A Taste of SQL
These collected lessons do not substitute Brian Yu's accessible explanations, but are a pretty good window into how they were planned, how the content was presented and in which order the selected topics were judged to be intuitive for learning (presumably).

## Some things I learned
To normalize is to organize the data in a database in order to improve efficiency and avoid redundancy. (memory may be traded for processing power)

(Opening a file on SQL requires only the use of "sqlite3" followed by the name of the file to open, for example: `sqlite fiftyville.db`)

### 1. In order to view the structure of a database (a .db file) the following command can be used. Additionally, and more intuitively, checking a table for somw of it's content is also valuable, and can be achieved with the second command below (a limit of 5 was used).
```SQL
.SCHEMA
SELECT * FROM table LIMIT 5;
```

### 2. In SQL it is simple to require a filtered result, which will take as many arguments as necesssary (making sure to provide the right data types).
```SQL
SELECT * FROM shows WHERE title = "Black Mirror";
```

### 3. The cells that SQL will "answer" the user can also be selected, and different values can be naturally used as condition (=, >, <, =>, <=, ...).
```SQL 
SELECT title, year FROM shows WHERE year > 2020;
```

### 4. The results can be counted using the command COUNT(*).
```SQL
SELECT COUNT(*) FROM shows WHERE year > 2020;
```

### 5. Searching for content within the cells (intead of using the entire cell for comparison).
```SQL
SELECT * FROM shows WHERE title LIKE "%Lord of the Rings%";
```

### 6. As stated above, it is easy to concatenate multiple criteria for filtering the results.
```SQL
SELECT id FROM shows WHERE title = "Stranger Things" AND year = 2016;
```

### 7. Nesting is also possible. With additional, slow thinking, doing this can actually help follow a linear line of thought instead of the immediate, somewhat recursive (yet intuitive), copy and pasting of multiple queries.
In such cases, the queries work similar to functions on programming, or how we should solve mathematical operations with parenthesis (do everything that is inside, then use the result and add to be used on the outside).
```SQL
SELECT genre FROM genres WHERE show_id =
(SELECT id FROM shows WHERE title = "Stranger Things" AND year = 2016);
```

### 8. Results can be ordered by the contents of whatever type as needed. 
```SQL
SELECT * FROM shows WHERE title = "The Office" ORDER BY episodes;
```

### 9. Descending, or ascending (default).
```SQL 
SELECT * FROM shows WHERE title = "The Office" ORDER BY episodes DESC;
```
### 10. When asking questions to cases where the result of a nested query are a list of objects, the equal (=) sign is actually going to only allow one result to be displayed.
```SQL
SELECT name FROM people WHERE id =
(SELECT person_id FROM stars WHERE show_id =
(SELECT id FROM shows WHERE title = "The Office" ORDER BY episodes DESC LIMIT 1))
```
Result: 

	name
	Angela Kinsey

### 11. In order to show the full list, one must use "IN", as in "find the names of the people which id's are contained IN the following list (query to provide list)"
```SQL 
SELECT name FROM people WHERE id IN
(SELECT person_id FROM stars WHERE show_id =
(SELECT id FROM shows WHERE title = "The Office" ORDER BY episodes DESC LIMIT 1))
```

- The most common error I had was of not fully knowing the database, and confusing "phone_number" from one table to "caller id" from another, or "id" and "person_id". The structure of the language was simpler to learn, but the database could perhaps have some naming improvements.
