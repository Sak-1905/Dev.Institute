CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    product_name VARCHAR,
    price DECIMAL(10, 2)
);

CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES product_orders(order_id),
    product_name VARCHAR,
    price DECIMAL(10, 2)
);

CREATE OR REPLACE FUNCTION calculate_order_total(order_id INT) RETURNS DECIMAL AS $$
DECLARE
    total DECIMAL(10, 2);
BEGIN
    SELECT SUM(price) INTO total
    FROM items
    WHERE order_id = order_id;
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;

SELECT calculate_order_total(1); -- Replace with the desired order_id

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

CREATE OR REPLACE FUNCTION calculate_order_total_for_user(user_id INT, order_id INT) RETURNS DECIMAL AS $$
DECLARE
    total DECIMAL(10, 2);
BEGIN
    SELECT SUM(price) INTO total
    FROM items
    WHERE order_id = order_id
    AND order_id IN (SELECT order_id FROM product_orders WHERE user_id = user_id);
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;

SELECT calculate_order_total_for_user(1, 1); -- Replace with the desired user_id and order_id
