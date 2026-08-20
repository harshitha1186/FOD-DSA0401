import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Read CSV file
data = pd.read_csv("C:/Users/harsh/Downloads/PATIENT.csv")

# Display the data
print("Clinical Trial Data:")
print(data)

# Separate the two groups
control = data[data["Group"] == "Control"]["Recovery_Score"]
treatment = data[data["Group"] == "Treatment"]["Recovery_Score"]

# Calculate means
control_mean = control.mean()
treatment_mean = treatment.mean()

print("\nControl Group Mean:", control_mean)
print("Treatment Group Mean:", treatment_mean)

# Perform independent two-sample t-test
t_statistic, p_value = ttest_ind(treatment, control)

print("\nT-statistic:", t_statistic)
print("P-value:", p_value)

# Hypothesis testing
alpha = 0.05

if p_value < alpha:
    print("\nResult: Reject the null hypothesis.")
    print("The new treatment has a statistically significant effect.")
else:
    print("\nResult: Fail to reject the null hypothesis.")
    print("The new treatment does not have a statistically significant effect.")

# Visualization
groups = ["Control", "Treatment"]
means = [control_mean, treatment_mean]

plt.figure(figsize=(8, 5))

bars = plt.bar(groups, means)

plt.title("Clinical Trial: Control vs Treatment")
plt.xlabel("Group")
plt.ylabel("Average Recovery Score")

# Display mean values on bars
for bar, mean in zip(bars, means):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{mean:.2f}",
        ha="center",
        va="bottom"
    )

# Display p-value
plt.text(
    0.5,
    max(means) * 0.95,
    f"p-value = {p_value:.6f}",
    ha="center",
    fontsize=12
)

plt.tight_layout()
plt.show()
