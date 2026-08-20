#9. Scenario: You work for a real estate agency and have been given a dataset containing information  about properties for sale. The dataset is stored in a Pandas DataFrame named property_data. The  DataFrame has columns for property ID, location, number of bedrooms, area in square feet, and listing  price. Your task is to analyze the data and answer specific questions about the properties. 



import pandas as pd
import matplotlib.pyplot as plt

# Enter CSV file path
file_path = input("Enter the CSV file path: ")

# Read CSV file
property_data = pd.read_csv(file_path)

print("\nProperty Data")
print(property_data)

# 1. Average listing price of properties in each location
avg_price = property_data.groupby("Location")["Listing_Price"].mean()

print("\nAverage Listing Price by Location")
print(avg_price)

# 2. Number of properties with more than four bedrooms
count = property_data[property_data["Bedrooms"] > 4].shape[0]

print("\nNumber of Properties with More Than 4 Bedrooms:", count)

# 3. Property with the largest area
largest_property = property_data.loc[property_data["Area"].idxmax()]

print("\nProperty with Largest Area")
print(largest_property)

# -------- Graph --------
plt.figure(figsize=(7,5))

avg_price.plot(kind="bar", color="orange")

plt.title("Average Listing Price by Location")
plt.xlabel("Location")
plt.ylabel("Average Listing Price")
plt.grid(axis="y")

plt.show()
