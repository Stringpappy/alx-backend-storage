 0x00-MySQL_Advanced Task
1)  a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
If the table already exists, your script should not fail
Your script can be executed on any database

1. In and not out
mandatory
Write a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
If the table already exists, your script should not fail
Your script can be executed on any database

2. Best band ever!
mandatory
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: origin and nb_fans
Your script can be executed on any database
Context: Calculate/compute something is always power intensive… better to distribute the load!

3. Old school band
mandatory
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
You should use attributes formed and split for computing the lifespan

4. Buy buy buy
mandatory
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");


5. Email validation to sent
mandatory
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);



6. Add bonus
mandatory
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

Procedure AddBonus is taking 3 inputs (in this order):
user_id, a users.id value (you can assume user_id is linked to an existing users)
project_name, a new or already exists projects - if no projects.name found in the table, you should create it
score, the score value for the correction
Context: Write code in SQL is a nice level up!


7. Average score
mandatory
Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)

#
8. Optimize simple search
mandatory
Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name must be indexed
Context: Index is not the solution for any performance issue, but well used, it’s really powerful!


9. Optimize search and score
mandatory
Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name AND score must be indexed
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql> 
mysql> exit
bye


10. Safe divide
mandatory
Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:

You must create a function
The function SafeDiv takes 2 arguments:
a, INT
b, INT
And returns a / b or 0 if b == 0


11. No table for a meeting
mandatory
Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

Requirements:

The view need_meeting should return all students name when:
They score are under (strict) to 80
AND no last_meeting date OR more than a month
bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-need_meeting.sql | mysql -uroot -p holberton
Enter password: 
