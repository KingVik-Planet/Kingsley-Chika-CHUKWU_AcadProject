import matplotlib.pyplot as plt
import numpy as np

# Data
points = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']

ndvi_2014 = [0.0671118, 0.0730248, 0.0613345, 0.0546245, 0.0577109, 0.0580380, 0.0676076, 0.0818335, 0.0595732, 0.0639808]
ndvi_2024 = [0.1479580, 0.0876628, 0.1689500, 0.1694080, 0.1089720, 0.1442740, 0.1619340, 0.1525120, 0.1606730, 0.1608590]

ndmi_2014 = [0.1172890, 0.0897930, 0.1168790, 0.1055170, 0.0991640, 0.0920040, 0.0960122, 0.0907293, 0.1085430, 0.0967805]
ndmi_2024 = [-0.0247039, -0.0212241, 0.0488535, -0.0034423, 0.1142280, -0.0396003, -0.0192293, -0.0267965, -0.0299451, -0.0233911]

ndwi_2014 = [-0.0814535, -0.0774962, -0.0740089, -0.0689326, -0.0681141, -0.0690232, -0.0779626, -0.0894176, -0.0721087, -0.0737986]
ndwi_2024 = [-0.1462780, -0.0821359, -0.1545880, -0.1655550, -0.0881139, -0.1444870, -0.1584750, -0.1472730, -0.1583970, -0.1557100]

# Create subplots
plt.figure(figsize=(15, 7))

# NDVI Plot
plt.subplot(3, 1, 1)
plt.plot(points, ndvi_2014, marker='o', label='NDVI 2014', color='green')
plt.plot(points, ndvi_2024, marker='o', label='NDVI 2024', color='darkgreen')
plt.title('Spectral Indices of Ikwo Local Govt. Area, \nEbonyi State, Nigeria(2014 and 2024.\nNDVI Comparison (2014 and 2024)')
plt.ylabel('NDVI Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# NDMI Plot
plt.subplot(3, 1, 2)
plt.plot(points, ndmi_2014, marker='o', label='NDMI 2014', color='blue')
plt.plot(points, ndmi_2024, marker='o', label='NDMI 2024', color='navy')
plt.title('NDMI Comparison (2014 and 2024)')
plt.ylabel('NDMI Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# NDWI Plot
plt.subplot(3, 1, 3)
plt.plot(points, ndwi_2014, marker='o', label='NDWI 2014', color='red')
plt.plot(points, ndwi_2024, marker='o', label='NDWI 2024', color='darkred')
plt.title('NDWI Comparison (2014 and 2024)')
plt.ylabel('NDWI Value')
plt.xlabel('Sampling Points of the Spectral Indices of Ikwo Local Govt. Area (P1-P10)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()