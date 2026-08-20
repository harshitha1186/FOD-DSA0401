#6. Scenario: You are a cashier at a grocery store and need to calculate the total cost of a customer's purchase, including applicable discounts and taxes. You have the item prices and quantities in separate  lists, and the discount and tax rates are given as percentages. Your task is to calculate the total cost for  the customer. 
#Question: Use arithmetic operations to calculate the total cost of a customer's purchase, including discounts and taxes, given the item prices, quantities, discount rate, and tax rate? 



import pandas as pd

# Get CSV file path from the user
file_path = input("Enter the CSV file path: ")

df = pd.read_csv(r"C:\Users\harsh\Downloads\EXP 6.CSV")

# Display the data
print("\nCustomer Purchase Details:")
print(df)

# Get discount and tax rates
discount_rate = float(input("\nEnter Discount Rate (%): "))
tax_rate = float(input("Enter Tax Rate (%): "))

# Calculate cost of each item
df["Item_Total"] = df["Price"] * df["Quantity"]

# Calculate subtotal
subtotal = df["Item_Total"].sum()

discount = subtotal * (discount_rate / 100)

amount_after_discount = subtotal - discount

tax = amount_after_discount * (tax_rate / 100)

# Final total
final_total = amount_after_discount + tax

# Display calculations
print("\n----- BILL -----")
print(df[["Item", "Price", "Quantity", "Item_Total"]])

print(f"\nSubtotal           : ₹{subtotal:.2f}")
print(f"Discount ({discount_rate}%) : ₹{discount:.2f}")
print(f"Amount After Discount : ₹{amount_after_discount:.2f}")
print(f"Tax ({tax_rate}%)      : ₹{tax:.2f}")
print(f"Final Total        : ₹{final_total:.2f}")
