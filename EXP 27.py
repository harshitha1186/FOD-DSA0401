import pandas as pd
import matplotlib.pyplot as plt

# CSV file path
file_path = r"C:\Users\harsh\Downloads\27.CSV"

# Read CSV file
df = pd.read_csv(file_path)

print("\n========== PLAYER DATA ==========")
print(df)

# Display column names
print("\nColumns in CSV:")
print(df.columns.tolist())

# Top 5 players by goals
top_goals = df.nlargest(5, 'Goals')

print("\n========== TOP 5 GOAL SCORERS ==========")
print(top_goals[['Name', 'Goals']])

# Top 5 players by salary
top_salary = df.nlargest(5, 'Salary')

print("\n========== TOP 5 HIGHEST SALARIES ==========")
print(top_salary[['Name', 'Salary']])

# Average age
average_age = df['Age'].mean()

print("\nAverage Age:", round(average_age, 2))

# Players above average age
above_average = df[df['Age'] > average_age]

print("\n========== PLAYERS ABOVE AVERAGE AGE ==========")

if len(above_average) > 0:
    print(above_average[['Name', 'Age']])
else:
    print("No players are above the average age.")

# Position distribution
position_count = df['Position'].value_counts()

print("\n========== POSITION DISTRIBUTION ==========")
print(position_count)

# Bar chart
plt.figure(figsize=(8, 5))

position_count.plot(kind='bar')

plt.title("Distribution of Players Based on Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")

plt.tight_layout()
plt.show()
