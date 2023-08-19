SELECT first_name AS "First", last_name AS "Last"
FROM employee;

SELECT DISTINCT department_id
FROM employee;

SELECT *
FROM employee
ORDER BY first_name DESC;

SELECT first_name, last_name, salary, salary * 0.15 AS pf
FROM employee;

SELECT employee_id, first_name, last_name, salary
FROM employee
ORDER BY salary ASC;

SELECT SUM(salary) AS total_salary
FROM employee;

SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary
FROM employee;

SELECT AVG(salary) AS average_salary
FROM employee;

SELECT COUNT(*) AS employee_count
FROM employee;

SELECT UPPER(first_name) AS upper_case_first_name
FROM employees;

SELECT SUBSTRING(first_name, 1, 3) AS first_name_prefix
FROM employees;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

SELECT first_name, last_name, LENGTH(CONCAT(first_name, ' ', last_name)) AS full_name_length
FROM employees;

SELECT first_name
FROM employees
WHERE first_name ~ '[0-9]';

SELECT *
FROM your_table_name
LIMIT 10;







SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 10000 AND 15000;

SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 1987;

SELECT *
FROM employees
WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';

SELECT last_name, job, salary
FROM employees
WHERE job NOT IN ('Programmer', 'Shipping Clerk')
  AND salary NOT IN (4500, 10000, 15000);

SELECT last_name
FROM employees
WHERE LENGTH(last_name) = 6;

SELECT last_name
FROM employees
WHERE SUBSTRING(last_name FROM 3 FOR 1) = 'e';

SELECT DISTINCT job
FROM employees;

SELECT *
FROM employees
WHERE last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD');
