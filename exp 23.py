import numpy as np
from scipy import stats

# Input conversion rates
A = list(map(float, input(
    "Enter conversion rates for Design A (comma-separated): "
).split(",")))

B = list(map(float, input(
    "Enter conversion rates for Design B (comma-separated): "
).split(",")))

# Calculate means
mean_A = np.mean(A)
mean_B = np.mean(B)

# Independent two-sample t-test
t_stat, p_value = stats.ttest_ind(A, B, equal_var=False)

print("\n----- A/B TEST RESULTS -----")

print("Design A mean conversion rate:", round(mean_A, 4))
print("Design B mean conversion rate:", round(mean_B, 4))

print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_value, 4))

# Significance level
alpha = 0.05

if p_value < alpha:
    print("\nConclusion: There is a statistically significant difference.")
else:
    print("\nConclusion: There is no statistically significant difference.")
