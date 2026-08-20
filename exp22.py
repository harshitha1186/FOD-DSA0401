import numpy as np
from scipy import stats

# Input data
drug = list(map(float, input("Enter blood pressure reductions for Drug group (comma-separated): ").split(",")))
placebo = list(map(float, input("Enter blood pressure reductions for Placebo group (comma-separated): ").split(",")))

# Drug group
drug_mean = np.mean(drug)
drug_std = np.std(drug, ddof=1)
drug_n = len(drug)

drug_ci = stats.t.interval(
    confidence=0.95,
    df=drug_n - 1,
    loc=drug_mean,
    scale=drug_std / np.sqrt(drug_n)
)

# Placebo group
placebo_mean = np.mean(placebo)
placebo_std = np.std(placebo, ddof=1)
placebo_n = len(placebo)

placebo_ci = stats.t.interval(
    confidence=0.95,
    df=placebo_n - 1,
    loc=placebo_mean,
    scale=placebo_std / np.sqrt(placebo_n)
)

print("\n----- RESULTS -----")

print("\nDrug Group:")
print("Sample size:", drug_n)
print("Mean reduction:", round(drug_mean, 2))
print("95% Confidence Interval:",
      (round(drug_ci[0], 2), round(drug_ci[1], 2)))

print("\nPlacebo Group:")
print("Sample size:", placebo_n)
print("Mean reduction:", round(placebo_mean, 2))
print("95% Confidence Interval:",
      (round(placebo_ci[0], 2), round(placebo_ci[1], 2)))
