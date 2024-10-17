-- a SQL script that creates a table users
CREATE TABLE IF NOT EXISTS users (
    id NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
