CREATE DATABASE customer_retention_analysis;
USE customer_retention_analysis;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    Gender VARCHAR(10),
    Age INT,
    City VARCHAR(100),
    JoinDate DATE
);

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(150),
    CategoryID INT,
    FOREIGN KEY (CategoryID)
        REFERENCES Categories(CategoryID)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(12,2),

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)
);


CREATE TABLE Returns (
    ReturnID INT PRIMARY KEY,
    OrderID INT,
    ReturnDate DATE,
    Reason VARCHAR(255),

    FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID)
);



                              