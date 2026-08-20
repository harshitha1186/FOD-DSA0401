#24.Scenario:You are a scientist conducting research on rare elements found in a specific region. Your  goal is to estimate the average concentration of a rare element in the region using a random sample of measurements. You will use the NumPy library to perform point estimation and calculate confidence  intervals for the population mean.The rare element concentration data is stored in a CSV file named  "rare_elements.csv," where each row contains a single measurement of the concentration. Question: 
write a Python program that allows the user to input the sample size, confidence level, and desired level of precision. 


import numpy as np
from scipy import stats

# CSV file path
filename = r"C:\Users\harsh\Downloads\24.csv"

# Read data from CSV
data = np.loadtxt(filename, delimiter=",", skiprows=1)

# Convert to 1D array
data = np.ravel(data)

print("Total number of measurements:", len(data))

# Get input from user
sample_size = int(input("Enter sample size: "))

confidence_level = float(
    input("Enter confidence level (example: 95): ")
)

precision = float(
    input("Enter desired level of precision: ")
)

# Check sample size
if sample_size <= 0 or sample_size > len(data):
    print("Invalid sample size.")
    exit()

# Select random sample
sample = np.random.choice(
    data,
    size=sample_size,
    replace=False
)

# Point estimation
sample_mean = np.mean(sample)

# Sample standard deviation
sample_std = np.std(sample, ddof=1)

# Convert confidence level to decimal
confidence = confidence_level / 100

# Degrees of freedom
df = sample_size - 1

# Standard error
standard_error = sample_std / np.sqrt(sample_size)

# t critical value
t_critical = stats.t.ppf(
    (1 + confidence) / 2,
    df
)

# Margin of error
margin_error = t_critical * standard_error

# Confidence interval
lower_limit = sample_mean - margin_error
upper_limit = sample_mean + margin_error

# Display results
print("\n========== RESULTS ==========")

print("Sample Size:", sample_size)
print("Confidence Level:", confidence_level, "%")
print("Desired Precision:", precision)

print("\nSelected Sample:")
print(sample)

print("\nPoint Estimate (Sample Mean):",
      round(sample_mean, 4))

print("Standard Deviation:",
      round(sample_std, 4))

print("Margin of Error:",
      round(margin_error, 4))

print("\n95% Confidence Interval:")
print("Lower Limit:", round(lower_limit, 4))
print("Upper Limit:", round(upper_limit, 4))

# Check precision
if margin_error <= precision:
    print("\nDesired precision is achieved.")
else:
    print("\nDesired precision is NOT achieved.")
    print("Try increasing the sample size.")
