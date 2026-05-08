import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("toy_hr_data.csv")

mean_sal = df["salary"].mean()
median_sal = df["salary"].median()

fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(df["salary"], bins=15, color="steelblue", edgecolor="white", alpha=0.85)

ax.axvline(mean_sal, color="red", linewidth=2, label=f"Mean: ${mean_sal:,.0f}")
ax.axvline(median_sal, color="blue", linewidth=2, linestyle="--", label=f"Median: ${median_sal:,.0f}")

ax.text(mean_sal + 1500, ax.get_ylim()[1] * 0.92, f"Mean\n${mean_sal:,.0f}",
        color="red", fontsize=9, va="top")
ax.text(median_sal - 1500, ax.get_ylim()[1] * 0.92, f"Median\n${median_sal:,.0f}",
        color="blue", fontsize=9, va="top", ha="right")

ax.set_xlabel("Salary ($)", fontsize=12)
ax.set_ylabel("Number of Employees", fontsize=12)
ax.set_title("Distribution of Salary", fontsize=14)
ax.legend()

plt.tight_layout()
plt.savefig("salary_distribution.png", dpi=150)
print(f"Mean:   ${mean_sal:,.0f}")
print(f"Median: ${median_sal:,.0f}")
