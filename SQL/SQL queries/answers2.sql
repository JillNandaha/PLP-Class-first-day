-- answers.sql

-- Question 1
-- Show total payment amount for each payment date, sorted by latest 5 dates
SELECT 
    paymentDate, 
    SUM(amount) AS total_amount
FROM 
    payments
GROUP BY 
    paymentDate
ORDER BY 
    paymentDate DESC
LIMIT 5;

-- Question 2
-- Find the average credit limit per customer, grouped by customer name and country
SELECT 
    customerName, 
    country, 
    AVG(creditLimit) AS average_credit_limit
FROM 
    customers
GROUP BY 
    customerName, country;

-- Question 3
-- Calculate total price for each product (quantityOrdered * priceEach), grouped by productCode and quantityOrdered
SELECT 
    productCode, 
    quantityOrdered, 
    (quantityOrdered * priceEach) AS total_price
FROM 
    orderdetails
GROUP BY 
    productCode, quantityOrdered;

-- Question 4
-- Find the highest payment amount per check number
SELECT 
    checkNumber, 
    MAX(amount) AS highest_amount
FROM 
    payments
GROUP BY 
    checkNumber;
