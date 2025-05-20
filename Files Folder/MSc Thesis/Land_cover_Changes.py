import matplotlib.pyplot as plt
import numpy as np

# Data
classes = ['Baresoil', 'Built Area', 'Farmland', 'Vegetation', 'Water']
percent_2000 = [4.29, 4.62, 65.13, 25.33, 0.63]
percent_2010 = [11.54, 14.00, 52.05, 19.23, 3.18]
percent_2020 = [21.06, 22.35, 42.98, 9.49, 4.12]

years = ['2000', '2010', '2020']
x = np.arange(len(classes))
width = 0.2

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, percent_2000, width, label='2000', color='blue')
rects2 = ax.bar(x, percent_2010, width, label='2010', color='green')
rects3 = ax.bar(x + width, percent_2020, width, label='2020', color='orange')

# Labels and formatting
ax.set_xlabel('Land Cover Class')
ax.set_ylabel('Percentage (%) Changes')
ax.set_title("Land Cover Changes in Rutungo Mining Study Area of Year 2000, 2010 and 2020")
ax.set_xticks(x)
ax.set_xticklabels(classes, rotation=45, ha="right")
ax.legend()
ax.grid(linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
