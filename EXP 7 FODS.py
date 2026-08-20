#7. Scenario: You are working as a data analyst for an e-commerce company. You have been given a  dataset containing information about customer orders, stored in a Pandas DataFrame named order_data. The DataFrame has columns for customer ID, order date, product name, and order quantity.  Your task is to analyze the data and answer specific questions about the orders. 
#Question: Using Pandas DataFrame operations, how would you find the following information from  the order_data DataFrame: 
#1. The total number of orders made by each customer. 
#2. The average order quantity for each product. 
#3. The earliest and latest order dates in the dataset. 



import pandas as pd
import matplotlib.pyplot as plt

# Enter CSV file path
file_path = input("Enter the CSV file path: ")

# Read CSV file
order_data = pd.read_csv(file_path)

# Convert Order_Date into datetime
order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

print("\nCustomer Orders Data")
print(order_data)

# 1. Total number of orders made by each customer
orders = order_data.groupby("Customer_ID").size()

print("\nTotal Orders by Each Customer")
print(orders)

# 2. Average order quantity for each product
avg_quantity = order_data.groupby("Product_Name")["Order_Quantity"].mean()

print("\nAverage Order Quantity for Each Product")
print(avg_quantity)

# 3. Earliest and Latest Order Dates
print("\nEarliest Order Date:", order_data["Order_Date"].min())
print("Latest Order Date:", order_data["Order_Date"].max())

# -------- Graph --------
plt.figure(figsize=(6,4))
orders.plot(kind="bar", color="skyblue")

plt.title("Total Orders by Customer")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")
plt.grid(axis="y")

plt.show()
