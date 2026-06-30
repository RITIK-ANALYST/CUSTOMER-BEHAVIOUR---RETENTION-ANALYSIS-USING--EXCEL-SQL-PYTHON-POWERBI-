USE customer_retention_analysis;


/*--- Total customers----*/

SELECT count(distinct customerid) as total_customers from customers;

/*--Total Orders--*/

SELECT count(distinct orderid) as Total_orders from orders;

/*--Total Revenue--*/

SELECT sum(totalamount) as Total_revenue from orders;

/*--Total products Sold--*/

SELECT count(productid)  as total_products_sold from order_details;

/*==Average Revenue per customer===*/

SELECT customerid, avg(TotalAmount) Average_Revenue from orders
 GROUP BY customerid
 order by Customerid;
 
 /*=====Revenue by Month=====*/
 
 SELECT year(orderdate)as year, month(orderdate) as month, sum(totalamount) as Total_Revenue
 from Orders
 group by year, month
 order by year, month;
 
 /*====Revenue By Product Category====*/
 
 SELECT p.categoryid,p.productname ,sum(od.quantity * od.unitprice) as Total_Revenue
 from products p JOIN order_details od
 on p.productid = od.productid
 GROUP BY p.categoryid,p.productname
 Order BY p.categoryid,p.productname;
 


 







                              