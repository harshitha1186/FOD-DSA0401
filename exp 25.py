import pandas as pd
import numpy as np
from scipy import stats

# CSV file path
filename = r"C:\Users\harsh\Downloads\25.csv"

# Read CSV
data = pd.read_csv(filename)

print("\nAvailable columns:")
print(data.columns.tolist())

# Ask user for rating column
column = input("\nEnter the rating column name: ")

# Get rating data
ratings = pd.to_numeric(data[column], errors="coerce").dropna()

# Check data
if len(ratings) < 2:
    print("Not enough rating data.")
    exit()

# User input
confidence_level = float(
    input("Enter confidence level (example: 95): ")
)

# Sample size
n = len(ratings)

# Mean
mean_rating = ratings.mean()

# Standard deviation
std_rating = ratings.std(ddof=1)

# Standard error
standard_error = std_rating / np.sqrt(n)

# Confidence level
confidence = confidence_level / 100

# Degrees of freedom
df = n - 1

# t critical value
t_critical = stats.t.ppf(
    (1 + confidence) / 2,
    df
)

# Margin of error
margin_error = t_critical * standard_error

# Confidence interval
lower_limit = mean_rating - margin_error
upper_limit = mean_rating + margin_error

# Customer satisfaction
# Rating >= 4 is considered satisfied
satisfied = (ratings >= 4).sum()

satisfaction_percentage = (satisfied / n) * 100

# Display results
print("\n========== CUSTOMER REVIEW RESULTS ==========")

print("Number of reviews:", n)

print("Average rating:",
      round(mean_rating, 2))

print("Standard deviation:",
      round(std_rating, 2))

print("Confidence level:",
      confidence_level, "%")

print("Margin of error:",
      round(margin_error, 2))

print("\nConfidence Interval:")
print("Lower limit:",
      round(lower_limit, 2))

print("Upper limit:",
      round(upper_limit, 2))

print("\nCustomer Satisfaction:")
print("Satisfied customers:", satisfied)

print("Satisfaction percentage:",
      round(satisfaction_percentage, 2), "%")
