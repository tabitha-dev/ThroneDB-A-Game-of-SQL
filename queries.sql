-- Find the Highest-Spending Customer
SELECT c.first_name, c.last_name, SUM(o.total_price) AS total_spent
FROM customer_orders o
JOIN game_of_thrones_customers c ON o.customer_id = c.id
GROUP BY c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 1;

-- Find the Most Popular Product
SELECT p.name, SUM(o.quantity) AS total_sold
FROM customer_orders o
JOIN medieval_store_products p ON o.product_id = p.id
GROUP BY p.name
ORDER BY total_sold DESC
LIMIT 1;

-- Rank Customers by Spending Tier
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

-- Check Inventory Levels
SELECT name, stock_quantity FROM medieval_store_products ORDER BY stock_quantity ASC;

-- Find Customers Who Have Not Placed an Order
SELECT c.first_name, c.last_name
FROM game_of_thrones_customers c
LEFT JOIN customer_orders o ON c.id = o.customer_id
WHERE o.id IS NULL;

-- Calculate Average Order Value
SELECT ROUND(AVG(total_price), 2) AS avg_order_value FROM customer_orders;

-- Find the Most Recent Order
SELECT * FROM customer_orders ORDER BY order_date DESC LIMIT 1;

-- Predict Stock Depletion (Based on Sales Rate)
SELECT p.name, p.stock_quantity, SUM(o.quantity) AS total_sold,
       (p.stock_quantity / NULLIF(SUM(o.quantity), 0)) AS estimated_remaining_orders
FROM customer_orders o
JOIN medieval_store_products p ON o.product_id = p.id
GROUP BY p.name, p.stock_quantity
ORDER BY estimated_remaining_orders ASC;
