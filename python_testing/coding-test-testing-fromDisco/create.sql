DROP DATABASE tdd_test;
CREATE DATABASE tdd_test;

\c tdd_test;
CREATE TABLE IF NOT EXISTS humans (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);