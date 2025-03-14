import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the dataset
df = pd.read_csv("train.csv")
df = df.dropna(subset=["Sales", "Category"])
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Sales"] = df["Sales"].astype(float)
df = df[["Order Date", "Category", "Sales", "Region"]]
df["Month"] = df["Order Date"].dt.to_period("M")

# Analyze: Calculate sales metrics
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Sales"].sum()

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