SELECT *
FROM customer;

SELECT first_name || ' ' || last_name AS full_name
FROM customer;

SELECT DISTINCT create_date
FROM customer;

SELECT *
FROM customer
ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT a.address, a.phone
FROM customer c
JOIN address a ON c.address_id = a.address_id
WHERE a.district = 'Texas';

SELECT *
FROM film
WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'YourFavoriteMovieTitle';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE SUBSTRING(title FROM 1 FOR 2) = 'YY';

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

SELECT film_id, title, rental_rate
FROM (
    SELECT film_id, title, rental_rate,
           ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num
    FROM film
) AS ranked_films
WHERE row_num > 10 AND row_num <= 20;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id, p.payment_id;

SELECT film_id, title
FROM film
WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);

SELECT city.city_id, city.city, country.country
FROM city
JOIN country ON city.country_id = country.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, s.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN rental r ON p.rental_id = r.rental_id
JOIN staff s ON r.staff_id = s.staff_id
ORDER BY s.staff_id;

