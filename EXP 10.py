import pandas as pd
import matplotlib.pyplot as plt

# Enter CSV file path
file_path = input("Enter the CSV file path: ")

# Read CSV file
sales = pd.read_csv(file_path)

print("\nMonthly Sales Data")
print(sales)

# -------- Line Plot --------
plt.figure(figsize=(7,5))

plt.plot(sales["Month"], sales["Sales"], marker="o", color="blue")

plt.title("Monthly Sales Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# -------- Bar Plot --------
plt.figure(figsize=(7,5))

plt.bar(sales["Month"], sales["Sales"], color="green")

plt.title("Monthly Sales Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
