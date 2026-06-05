import pandas as pd

# Read CSV file
data = pd.read_csv("sales_data.csv")

# Show first 5 rows
print("DATASET:")
print(data.head())

# Total Sales
print("\nTOTAL SALES:", data["SALES"].sum())

# Total Profit
print("TOTAL PROFIT:", data["PROFIT"].sum())

# Sales by Product
print("\nSALES BY PRODUCT:")
print(data.groupby("PRODUCT")["SALES"].sum())

# Profit by Product
print("\nPROFIT BY PRODUCT:")
print(data.groupby("PRODUCT")["PROFIT"].sum())

# Sales by City
print("\nSALES BY CITY:")
print(data.groupby("CITY")["SALES"].sum())

# Sales by Month
print("\nSALES BY MONTH:")
print(data.groupby("MONTH")["SALES"].sum())

import matplotlib.pyplot as plt

data.groupby("PRODUCT")["SALES"].sum().plot(kind="bar")
plt.show()
