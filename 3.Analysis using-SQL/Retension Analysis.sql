USE customer_retention_analysis; 

/*===1. How many new customers were acquired each month?====*/

with firstorder as (SELECT CustomerID,
        MIN(OrderDate) as first_order_date FROM Orders
    GROUP BY CustomerID)
    SELECT
    YEAR(first_order_date) as order_year,
    MONTH(first_order_date) as order_month,
    COUNT(*) as new_customers from firstorder
GROUP BY YEAR(first_order_date), MONTH(first_order_date)
ORDER BY order_year, order_month;

/*====2. How many returning customers placed orders each month?====*/

SELECT YEAR(o.OrderDate) AS order_year, MONTH(o.OrderDate) AS order_month,
    COUNT(DISTINCT o.CustomerID) AS returning_customers FROM Orders o JOIN
    (SELECT CustomerID, MIN(OrderDate) AS first_order_date FROM Orders
    GROUP BY CustomerID
) f
ON o.CustomerID = f.CustomerID
WHERE o.OrderDate > f.first_order_date
GROUP BY YEAR(o.OrderDate), MONTH(o.OrderDate)
ORDER BY order_year, order_month;

/*====3. Name customers made only one purchase?====*/ 

SELECT c.customername , count(o.orderid) as  total_orders, 
row_number() over(order by c.customername ) as row_num from customers c
JOIN orders o on o.customerid = c.customerid 
GROUP BY c.customername
having count(o.orderid)=1;

/*===5. What percentage of customers are repeat customers?====*/

SELECT ROUND(COUNT(DISTINCT CASE WHEN order_count > 1 THEN CustomerID END) * 100.0
        / COUNT(DISTINCT CustomerID),2) AS repeat_customer_percentage
FROM (SELECT CustomerID, COUNT(OrderID) AS order_count
    FROM Orders GROUP BY CustomerID) t;
    
/*===6. Which customers have the highest number of repeat purchases?====*/    

SELECT c.CustomerID,c.CustomerName,COUNT(o.OrderID) AS total_orders
FROM Customers c JOIN Orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CustomerName
HAVING COUNT(o.OrderID) > 1
ORDER BY total_orders DESC;
