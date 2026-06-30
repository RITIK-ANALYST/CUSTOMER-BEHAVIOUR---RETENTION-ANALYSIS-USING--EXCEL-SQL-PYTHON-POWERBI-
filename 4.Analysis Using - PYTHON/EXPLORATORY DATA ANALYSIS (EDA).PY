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


# =====  TOTAL CUSTOMERS =======

print("Total Customers",
customers["CustomerID"].nunique())

# =====  TOTAL CUSTOMERS =======

print("Total Orders:", orders["OrderID"].nunique())

# =====  TOTAL Revenue =======

merged = order_details.merge(products, on="ProductID")
merged["Revenue"] = merged["Quantity"] * merged["UnitPrice"]

print("Total Revenue:", merged["Revenue"].sum())

# =====  Average Revenue =======

revenue_per_order = merged.groupby("OrderID")["Revenue"].sum()

print("Average Order Value:", revenue_per_order.mean())

# =====  RETURN RATE =======

return_rate = (returns["OrderID"].nunique() / orders["OrderID"].nunique()) * 100

print(f"Return Rate: {return_rate:.2f}%")


 # ===== MONTHLY REVENUE TREND (Line Chart)=======



# Convert OrderDate to datetime 
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

# Extract Month
orders["Month"] = orders["OrderDate"].dt.to_period("M").astype(str)

# Calculate Monthly Revenue
monthly_revenue = orders.groupby("Month")["TotalAmount"].sum().reset_index()

# Plot Line Chart
plt.figure(figsize=(10,5))
plt.plot(monthly_revenue["Month"],
         monthly_revenue["TotalAmount"],
         marker='o',
         )

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.grid(True)

plt.tight_layout()
plt.show()



 
 #============= Top 10 Products by Revenue (Horizontal Bar Chart)===============



# Merge Products and Order Details
product_sales = pd.merge(order_details, products, on="ProductID")

# Revenue
product_sales["Revenue"] = product_sales["Quantity"] * product_sales["UnitPrice"]

# Top 10 Products
top_products = (product_sales.groupby("ProductName")["Revenue"].sum().sort_values(ascending=False).head(10))

# Plot
plt.figure(figsize=(10,6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.show()