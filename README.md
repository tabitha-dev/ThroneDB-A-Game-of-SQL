# 🏠 ThroneDB: A Game of SQL ⚔️🏛️
**A medieval economy modeled with PostgreSQL — Advanced SQL analytics & data-driven storytelling!**

---

## 📈 Overview
**ThroneDB: A Game of SQL** is a **PostgreSQL-based SQL project** that simulates an economy in **Westeros** (Game of Thrones). It showcases **advanced SQL techniques**, including:

- 🔢 **Complex Queries** — `JOIN`, `GROUP BY`, `HAVING`, `CTEs`, `RANK()`, `CASE`
- 💰 **Business Intelligence** — Revenue analysis, customer segmentation, product trends
- ⚡ **Performance Optimization** — Indexing, query tuning, database normalization

---

## 🔧 Database Schema
The project contains **three key tables**:

1. **`game_of_thrones_customers`** 🏰 (Houses & Buyers)
2. **`medieval_store_products`** ⚔️ (Weapons, Armor, Potions, Magic Items)
3. **`customer_orders`** 📝 (Who bought what, when, and for how much?)

📂 **[View the Full Schema Here](setup.sql)**

---

## 📚 Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/tabitha-dev/ThroneDB-A-Game-of-SQL.git
cd ThroneDB-A-Game-of-SQL
```

### 2. Set Up PostgreSQL & Load the Database
```sh
psql -U postgres -d throne_db -f setup.sql
psql -U postgres -d throne_db -f data.sql
psql -U postgres -d throne_db -f queries.sql
```

---

## 📊 Featured Queries
### 1. Find the Highest-Spending Customer
```sql
SELECT c.first_name, c.last_name, SUM(o.total_price) AS total_spent
FROM customer_orders o
JOIN game_of_thrones_customers c ON o.customer_id = c.id
GROUP BY c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 1;
```
📈 *Who is the richest customer in Westeros?*

### 2. Find the Most Popular Product
```sql
SELECT p.name, SUM(o.quantity) AS total_sold
FROM customer_orders o
JOIN medieval_store_products p ON o.product_id = p.id
GROUP BY p.name
ORDER BY total_sold DESC
LIMIT 1;
```
📈 *Which medieval item is in highest demand?*

### 3. Rank Customers by Spending Tier
```sql
SELECT c.first_name, c.last_name, SUM(o.total_price) AS total_spent,
       CASE
           WHEN SUM(o.total_price) > 1000 THEN 'VIP'
           WHEN SUM(o.total_price) BETWEEN 500 AND 1000 THEN 'Gold Member'
           ELSE 'Regular Customer'
       END AS customer_tier
FROM customer_orders o
JOIN game_of_thrones_customers c ON o.customer_id = c.id
GROUP BY c.first_name, c.last_name
ORDER BY total_spent DESC;
```
📈 *Who qualifies for VIP perks in the Iron Bank?*

📂 **[View All Queries Here](queries.sql)**

---

## 🏆 Features
- 💪 **Gamified SQL Learning** — A medieval theme makes SQL fun & engaging!
- 📊 **Real-World Analytics** — Sales trends, customer segmentation, inventory tracking
- ⚡ **Optimized for Performance** — Indexed queries, normalization, and `EXPLAIN ANALYZE`
- 🛠️ **Expandable** — Add more houses, products, and business logic!

---

## 💡 Future Enhancements
✅ Integrate with a **Flask API** to fetch real-time SQL results  
✅ Build **interactive dashboards** with **Power BI / Tableau**  
✅ Expand the dataset with **more medieval products & customers**  


---

## ⭐ **If you find this project useful, give it a star!** 🌟  

🔗 **[GitHub Repository](https://github.com/tabitha-dev/ThroneDB-A-Game-of-SQL)**  

---



