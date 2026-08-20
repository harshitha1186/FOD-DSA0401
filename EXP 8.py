#8. Scenario: You are a data scientist working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame. 
#Question: How would you find the top 5 products that have been sold the most in the past month? 


import pandas as pd
import matplotlib.pyplot as plt

# Enter CSV file path
file_path = input("Enter the CSV file path: ")

# Read CSV file
sales_data = pd.read_csv(file_path)

print("\nSales Data")
print(sales_data)

# Find Top 5 Selling Products
top5 = sales_data.sort_values(by="Quantity_Sold", ascending=False).head(5)

print("\nTop 5 Selling Products")
print(top5)

# -------- Graph --------
plt.figure(figsize=(7,5))

plt.bar(top5["Product_Name"], top5["Quantity_Sold"], color="green")

plt.title("Top 5 Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Quantity Sold")

plt.grid(axis="y")

plt.show()
