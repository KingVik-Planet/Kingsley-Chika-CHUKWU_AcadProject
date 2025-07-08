import matplotlib.pyplot as plt
import pandas as pd

# Load CSV
df = pd.read_csv("Data/UNILAK/Sample Points.csv")

# Check column names
print(df.columns)

# indexing
if "index" not in df.columns:
    df["index"] = range(1, len(df) + 1)

plt.figure(figsize=(10, 6)),
plt.plot(df["index"], df["Y1517"], label="Year 2015 & 2017", color="blue", linestyle="-", marker="o")
plt.plot(df["index"], df["Y1921"], label="Year 2019 & 2021", color="red", linestyle="--", marker="s")
plt.plot(df["index"], df["Y2325"], label="Year 2023 & 2025", color="green", linestyle=":", marker="^")

# Formatting
plt.xlabel("Sample Points")
plt.ylabel("Deformation Rate (Meters)")
#plt.title("Trend of Ground Deforemation of Rugongo Mining Site \nYear: 2015 & 2017, 2019 and 2021, 2023 & 2025")
plt.legend( loc = 3)
plt.grid(True)

# Save the figure
plt.savefig('Deformation Trend.png', dpi=1000, bbox_inches='tight')

# Show plot
plt.show()
