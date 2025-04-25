import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import numpy as np


df = pd.read_csv("C:\\Users\\ankit.yadav2\\Downloads\\bps_price.csv")
step = 5
xticks = df["RUNSTART"][::step]

print(df.head())

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="RUNSTART", y="timediff")
plt.title("Job Duration Over Time")
plt.xlabel("Date")
plt.ylabel("Duration (in minutes)")
# plt.xticks(xticks, rotation=90)
plt.grid(True, linestyle="--", alpha=0.7)  # Turns on gridlines for both axes
plt.tight_layout()
plt.show()
