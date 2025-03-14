import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("train.csv")
print(df.head())
print(df.info())

# Handle missing values
df = df.dropna(subset=["Sales", "Category"])
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Sales"] = df["Sales"].astype(float)
df = df[["Order Date", "Category", "Sales", "Region"]]
print(df.head())

# Total sales by category
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("Sales by Category:\n", sales_by_category)

# Total sales by region
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("Sales by Region:\n", sales_by_region)

# Monthly sales trend
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print("Monthly Sales (first 5 months):\n", monthly_sales.head())

# Visualize: Sales by Category (Bar Chart)
plt.figure(figsize=(10, 6))
sales_by_category.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# Visualize: Sales by Region (Bar Chart)
plt.figure(figsize=(10, 6))
sales_by_region.plot(kind="bar", color="lightgreen")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# Visualize: Monthly Sales Trend (Line Chart)
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o", color="purple")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()