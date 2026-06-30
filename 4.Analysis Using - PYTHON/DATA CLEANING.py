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
#     CHECK DUPLICATES
#  ==========================

print("CHECKING DUPLICATES")

print(customers.duplicated().sum())
print(categories.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())
print(order_details.duplicated().sum())
print(returns.duplicated().sum())

#  ==========================
#     REMOVE DUPLICATES
#  ==========================

print("REMOVING DUPLICATES")

customers = customers.drop_duplicates()
categories = categories.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()
order_details = order_details.drop_duplicates()
returns = returns.drop_duplicates()

#  ====================================
#     CHECK MISSING VALUES AGAIN
#  ====================================

print("CHECKING MISSING VALUES AGAIN")


print(customers.isnull().sum())
print(categories.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())
print(order_details.isnull().sum())
print(returns.isnull().sum())


#  ==========================
#     CONVERT DATE COLUMN
#  ==========================

print("CONVERT DATE COLUMNS")


orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
returns["ReturnDate"] = pd.to_datetime(returns["ReturnDate"])

#  ==============================
#     CHECK NEGATIVE VALUES
#  ==============================

print("CHECK NEGATIVE VALUES")

print(order_details[order_details["Quantity"] < 0])

print(order_details[order_details["UnitPrice"] < 0])