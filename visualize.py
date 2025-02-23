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
    FROM customer_orders o
    JOIN game_of_thrones_customers c ON o.customer_id = c.id
    GROUP BY c.first_name, c.last_name
    ORDER BY total_spent DESC
    LIMIT 10;
"""
df = pd.read_sql(query, conn)

# 🎨 Bar Chart
plt.figure(figsize=(12, 6))
sns.barplot(x=df["total_spent"], y=df["first_name"] + " " + df["last_name"], palette="coolwarm")
plt.xlabel("Total Amount Spent (Gold Coins)")
plt.ylabel("Customer Name")
plt.title("💼 Top 10 Customers by Spending")
plt.grid(axis="x", linestyle="--")
plt.savefig("top_customers.png")
plt.show()

### 🚀 2. BEST SELLING MEDIEVAL PRODUCTS ###
query = """
    SELECT p.name, SUM(o.quantity) AS total_sold
    FROM customer_orders o
    JOIN medieval_store_products p ON o.product_id = p.id
    GROUP BY p.id
    ORDER BY total_sold DESC;
"""
df = pd.read_sql(query, conn)

# 🎨 Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df["total_sold"], labels=df["name"], autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("⚔️ Most Popular Medieval Products Sold")
plt.savefig("top_products.png")
plt.show()

### 🚀 3. SALES TREND OVER TIME ###
query = """
    SELECT DATE_TRUNC('month', order_date) AS sales_month, 
           SUM(total_price) AS total_sales
    FROM customer_orders
    GROUP BY sales_month
    ORDER BY sales_month;
"""
df = pd.read_sql(query, conn)


# 🎨 Fixed Sales Trend Line Chart
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["sales_month"], y=df["total_sales"], marker="o", color="blue")

plt.xlabel("Month")
plt.ylabel("Total Sales (Gold Coins)")
plt.title("📆 Monthly Sales Trend Over Time")

plt.xticks(rotation=45)
plt.grid()
plt.savefig("sales_trend_fixed.png")
plt.show()


### 🚀 4. CUSTOMER SEGMENTATION ###
query = """
    SELECT first_name, last_name, total_spent,
           CASE 
               WHEN total_spent > 1000 THEN 'Noble'
               WHEN total_spent > 500 THEN 'Merchant'
               ELSE 'Commoner'
           END AS tier
    FROM (
        SELECT c.first_name, c.last_name, SUM(o.total_price) AS total_spent
        FROM customer_orders o
        JOIN game_of_thrones_customers c ON o.customer_id = c.id
        GROUP BY c.first_name, c.last_name
    ) AS spending_data;
"""
df = pd.read_sql(query, conn)

# 🎨 Category Bar Chart
plt.figure(figsize=(10, 6))
sns.countplot(x=df["tier"], palette="coolwarm")
plt.xlabel("Customer Tier")
plt.ylabel("Number of Customers")
plt.title("🏆 Customer Spending Segments")
plt.savefig("customer_segments.png")
plt.show()

# Close database connection
conn.close()
