SELECT *
FROM language;

SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;

SELECT f.title, f.description, COALESCE(l.name, 'No Language') AS language_name
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

INSERT INTO new_film (name)
VALUES
    ('New Film 1'),
    ('New Film 2'),
    ('New Film 3');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(customer_id),
    film_id INT REFERENCES film(film_id),
    review_text TEXT,
    review_date DATE
);

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR,
    score INT CHECK (score >= 1 AND score <= 10),
    review_text TEXT,
    last_update TIMESTAMP
);

-- Add the first movie review
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
    ((SELECT id FROM new_film WHERE name = 'New Film 1'), 
     (SELECT language_id FROM language WHERE name = 'English'), 
     'Great Movie', 9, 'This movie was really enjoyable.', NOW());

-- Add the second movie review
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
    ((SELECT id FROM new_film WHERE name = 'New Film 2'), 
     (SELECT language_id FROM language WHERE name = 'Spanish'), 
     'Could be Better', 6, 'The film had its moments, but lacked depth.', NOW());

-- Delete a film from the new_film table
DELETE FROM new_film WHERE name = 'New Film 1';

UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'New Language')
WHERE title IN ('Film Title 1', 'Film Title 2');

DROP TABLE customer_review;

SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

SELECT f.title, f.rental_rate, r.rental_date
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

SELECT f.title, f.description, f.release_year, a.first_name || ' ' || a.last_name AS actor_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo wrestler%'
AND a.first_name || ' ' || a.last_name = 'Penelope Monroe'
LIMIT 1;

SELECT title, description, length, rating
FROM film
WHERE length < '01:00:00' AND rating = 'R'
LIMIT 1;

SELECT f.title, f.rental_rate, r.rental_date, r.return_date
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name || ' ' || c.last_name = 'Matthew Mahan'
AND f.rental_rate > 4.00
AND r.rental_date >= '2005-07-28' AND r.rental_date <= '2005-08-01'
LIMIT 1;

SELECT f.title, f.description, f.replacement_cost
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name || ' ' || c.last_name = 'Matthew Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
AND f.replacement_cost > 20.00
LIMIT 1;
