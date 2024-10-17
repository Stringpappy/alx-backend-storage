-- a SQL script that creates a table users
CREATE TABLES IF NOT EXISTS users (
    id NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255),
    name VARCHAR(255)
);
