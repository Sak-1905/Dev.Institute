-- Creating the items table
CREATE TABLE items (
    item_id serial PRIMARY KEY,
    item_name varchar(255) NOT NULL,
    price numeric(10, 2) NOT NULL,
    description text
);

-- Creating the customers table
CREATE TABLE customers (
    customer_id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(100) UNIQUE,
    phone varchar(20),
    address text
);

INSERT INTO items (item_name, price)
VALUES ('Small Desk', 100),
       ('Chair', 50),
       ('Lamp', 20);

INSERT INTO items (item_name, price)
VALUES ('Large Desk', 300);

INSERT INTO items (item_name, price)
VALUES ('Fan', 80);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),
       ('Sandra', 'Jones'),
       ('Scott', 'Scott'),
       ('Trevor', 'Green'),
       ('Melanie', 'Johnson');
SELECT *
FROM items;

SELECT *
FROM items
WHERE price > 80;

SELECT *
FROM items
WHERE price <= 300;

SELECT *
FROM customers
WHERE last_name = 'Smith';

SELECT *
FROM customers
WHERE last_name = 'Jones';

SELECT *
FROM customers
WHERE first_name <> 'Scott';

SELECT *
FROM items
ORDER BY price ASC;

SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC;

SELECT first_name, last_name, email, phone, address
FROM customers
ORDER BY first_name ASC
LIMIT 3;

SELECT last_name
FROM customers
ORDER BY last_name DESC;
