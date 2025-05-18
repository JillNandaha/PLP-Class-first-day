-- Question 1
-- Show total payment amount per payment date, sorted by date desc, top 5 latest
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
-- Find average credit limit per customer, grouped by name and country
SELECT 
    customerName,
    country,
    AVG(creditLimit) AS average_credit_limit
FROM 
    customers
GROUP BY 
    customerName, country;


-- Question 3
-- Find total price of products ordered (quantity * priceEach)
SELECT 
    productCode,
    quantityOrdered,
    (quantityOrdered * priceEach) AS total_price
FROM 
    orderdetails
GROUP BY 
    productCode, quantityOrdered;


-- Question 4
-- Show highest payment amount per check number
SELECT 
    checkNumber,
    MAX(amount) AS highest_amount
FROM 
    payments
GROUP BY 
    checkNumber;
