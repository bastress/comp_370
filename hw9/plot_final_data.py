import pandas as pd
import matplotlib.pyplot as plt

# Read the TSV files for each school
df_mcgill = pd.read_csv("final_labeled_dataset_mcgill.tsv", sep="\t")
df_concordia = pd.read_csv("final_labeled_dataset_concordia.tsv", sep="\t")

# Group by 'coding' and count occurrences for each school
count_a = df_mcgill['coding'].value_counts().rename("School A")
count_b = df_concordia['coding'].value_counts().rename("School B")

# Merge counts into a single DataFrame for plotting
df_counts = pd.concat([count_a, count_b], axis=1).fillna(0)

# Plotting a stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))
df_counts.plot(kind="bar", stacked=True, color=["red", "darkgoldenrod"], ax=ax)
ax.set_title("Coding Counts by School")
ax.set_xlabel("Coding Categories")
ax.set_ylabel("Count")
ax.legend(["McGill", "Concordia"])
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("results.png")
