import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="thronedb",
    user="postgres",
    password="2686",
    host="localhost",
    port="5432"
)

### 🚀 1. TOP CUSTOMERS BY SPENDING ###
query = """
    SELECT c.first_name, c.last_name, SUM(o.total_price) AS total_spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.id
    ORDER BY total_spent DESC
    LIMIT 10;
"""
df = pd.read_sql(query, conn)

# 🎨 Bar Chart
plt.figure(figsize=(12, 6))
sns.barplot(x=df["total_spent"], y=df["first_name"] + " " + df["last_name"], palette="coolwarm")
plt.xlabel("Total Amount Spent ($)")
plt.ylabel("Customer Name")
plt.title("🛍️ Top 10 Customers by Spending")
plt.grid(axis="x", linestyle="--")
plt.show()

### 🚀 2. BEST SELLING FLOWERS ###
query = """
    SELECT f.name, SUM(o.quantity) AS total_sold
    FROM orders o
    JOIN flowers f ON o.flower_id = f.id
    GROUP BY f.id
    ORDER BY total_sold DESC;
"""
df = pd.read_sql(query, conn)

# 🎨 Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df["total_sold"], labels=df["name"], autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("🌸 Most Popular Flowers Sold")
plt.show()

### 🚀 3. SALES TREND OVER TIME ###
query = """
    SELECT DATE(order_date) AS order_day, SUM(total_price) AS total_sales
    FROM orders
    GROUP BY order_day
    ORDER BY order_day;
"""
df = pd.read_sql(query, conn)

# 🎨 Line Chart
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["order_day"], y=df["total_sales"], marker="o", color="blue")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.title("📅 Sales Trends Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()

### 🚀 4. CUSTOMER SEGMENTATION ###
query = """
    SELECT first_name, last_name, total_spent,
           CASE 
               WHEN total_spent > 40 THEN 'Gold'
               WHEN total_spent > 20 THEN 'Silver'
               ELSE 'Regular'
           END AS tier
    FROM (
        SELECT c.first_name, c.last_name, SUM(o.total_price) AS total_spent
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        GROUP BY c.id
    ) AS spending_data;
"""
df = pd.read_sql(query, conn)

# 🎨 Category Bar Chart
plt.figure(figsize=(10, 6))
sns.countplot(x=df["tier"], palette="coolwarm")
plt.xlabel("Customer Tier")
plt.ylabel("Number of Customers")
plt.title("🏆 Customer Spending Segments")
