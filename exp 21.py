import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats


def main():
    print("--- Data Input ---")
    use_default = (
        input("Use default 18-adult dataset from question? (y/n): ")
        .strip()
        .lower()
    )

    if use_default == "y":
        age = [
            23,
            23,
            27,
            27,
            39,
            41,
            47,
            49,
            50,
            52,
            54,
            54,
            56,
            57,
            58,
            58,
            60,
            61,
        ]
        fat = [
            9.5,
            26.5,
            7.8,
            17.8,
            31.4,
            25.9,
            27.4,
            27.2,
            31.2,
            34.6,
            42.5,
            28.8,
            33.4,
            30.2,
            34.1,
            32.9,
            41.2,
            35.7,
        ]
    else:
        # Custom user input
        age = list(
            map(
                float,
                input(
                    "Enter Age values separated by spaces: "
                ).split(),
            )
        )
        fat = list(
            map(
                float,
                input(
                    "Enter %fat values separated by spaces: "
                ).split(),
            )
        )

    # Create DataFrame
    df = pd.DataFrame({"Age": age, "%fat": fat})

    # 1. Statistics Summary
    print("\n--- Summary Statistics ---")
    stats_df = pd.DataFrame(
        {
            "Mean": df.mean(),
            "Median": df.median(),
            "Std Dev": df.std(),
        }
    )
    print(stats_df)

    # 2. Boxplots
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    df.boxplot(column=["Age"])
    plt.title("Boxplot of Age")

    plt.subplot(1, 2, 2)
    df.boxplot(column=["%fat"])
    plt.title("Boxplot of %fat")

    plt.tight_layout()
    plt.show()

    # 3. Scatter Plot and Q-Q Plot
    plt.figure(figsize=(12, 5))

    # Scatter Plot
    plt.subplot(1, 2, 1)
    plt.scatter(df["Age"], df["%fat"], color="blue", alpha=0.7)
    plt.title("Scatter Plot: Age vs %fat")
    plt.xlabel("Age")
    plt.ylabel("%fat")
    plt.grid(True)

    # Q-Q Plot for Age
    plt.subplot(1, 2, 2)
    stats.probplot(df["Age"], dist="norm", plot=plt)
    plt.title("Q-Q Plot of Age")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
