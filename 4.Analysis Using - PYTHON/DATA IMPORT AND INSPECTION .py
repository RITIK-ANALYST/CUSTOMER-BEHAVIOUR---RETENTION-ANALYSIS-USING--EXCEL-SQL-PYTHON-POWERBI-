#  ==========================
#     IMPORT ALL LIBRARIES
#  ==========================

import pandas as pd
import matplotlib.pyplot as plt

#  ==========================
#     IMPORT DATASETS 
#  ==========================


customers = pd.read_csv(r"D:\analyst project\Customer Behaviour or retension Analysis\2.Dataset used\Customers.csv")
orders  = pd.read_csv(r"D:\analyst project\Customer Behaviour or retension Analysis\2.Dataset used\orders.csv")
products = pd.read_csv(r"D:\analyst project\Customer Behaviour or retension Analysis\2.Dataset used\Products.csv")
returns = pd.read_csv(r"D:\analyst project\Customer Behaviour or retension Analysis\2.Dataset used\Returns.csv")
categories = pd.read_csv(r"D:\analyst project\Customer Behaviour or retension Analysis\2.Dataset used\Categories.csv")
order_details = pd.read_csv(r"D:\analyst project\Customer Behaviour or retension Analysis\2.Dataset used\order_details.csv")


#  ==========================
#     CHECKING NULL VALUES
#  ==========================

print("CHECKING NULL VALUES")

# Customers
print(customers.isnull().sum())

# Orders
print(orders.isnull().sum())

# Order Details
print(order_details.isnull().sum())

# Products
print(products.isnull().sum())

# Categories
print(categories.isnull().sum())

# Employees
print(returns.isnull().sum())


#  ==========================
#     Data Inspection
#  ==========================




# =====  SHAPE =======

print("DATA SHAPE")

print(customers.shape)
print(categories.shape)
print(products.shape)
print(orders.shape)
print(order_details.shape)
print(returns.shape)

# ===== DATA TYPES =======

print("DATA TYPES")

print(customers.dtypes)
print(categories.dtypes)
print(products.dtypes)
print(orders.dtypes)
print(order_details.dtypes)
print(returns.dtypes)

# ===== DATASET INFORMATION =======

print("DATA INFORMATIONS")

customers.info()
categories.info()
products.info()
orders.info()
order_details.info()
returns.info()

# ===== FIRST 5 ROWS =======

print("FIRST 5 ROWS OF THE DATA")

print(customers.head())
print(categories.head())
print(products.head())
print(orders.head())
print(order_details.head())
print(returns.head())

# ===== STATISTICAL SUMMARY =======

print("STATISTICAL SUMMARY OF THE DATA")

print(customers.describe(include='all'))
print(categories.describe(include='all'))
print(products.describe(include='all'))
print(orders.describe(include='all'))
print(order_details.describe(include='all'))
print(returns.describe(include='all'))

