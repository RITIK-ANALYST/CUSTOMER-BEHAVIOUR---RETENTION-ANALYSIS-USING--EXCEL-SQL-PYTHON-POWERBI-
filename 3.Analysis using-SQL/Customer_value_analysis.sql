USE customer_retention_analysis; 

/*====Q1. Customer Lifetime Value (CLV)====*/

SELECT c.customerid,c.customername,
SUM(od.quantity * od.unitprice) AS customer_lifetime_value FROM customers c
JOIN orders o ON c.customerid = o.customerid
JOIN order_details od
ON o.orderid = od.orderid
GROUP BY c.customerid,c.customername
ORDER BY customer_lifetime_value DESC;

/*===Q2. Top 10 Customers by Revenue====*/

SELECT c.customerid, c.customername,SUM(od.quantity * od.unitprice) AS total_revenue
FROM customers c JOIN orders o
ON c.customerid = o.customerid
JOIN order_details od ON o.orderid = od.orderid
GROUP BY c.customerid,c.customername
ORDER BY total_revenue DESC LIMIT 10;

/*===Q3. Average Revenue per Customer=====*/

SELECT SUM(od.quantity * od.unitprice) /COUNT(DISTINCT o.customerid) AS avg_revenue_per_customer
FROM orders o
JOIN order_details od ON o.orderid = od.orderid;



/*=====Q4. Customers Who Purchased the Highest Quantity of Products====*/

SELECT c.customerid,c.customername,SUM(od.quantity) AS total_quantity_purchased
FROM customers c JOIN orders o
ON c.customerid = o.customerid
JOIN order_details od ON o.orderid = od.orderid
GROUP BY c.customerid,c.customername
ORDER BY total_quantity_purchased DESC;

/*==Q5. Customers Who Purchased the Most Different Products===*/

SELECT c.customerid, c.customername,COUNT(DISTINCT od.productid) AS unique_products_purchased
FROM customers c JOIN orders o
ON c.customerid = o.customerid
JOIN order_details od
ON o.orderid = od.orderid
GROUP BY c.customerid,c.customername
ORDER BY unique_products_purchased DESC;