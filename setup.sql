-- Drop existing tables if they exist
DROP TABLE IF EXISTS customer_orders;
DROP TABLE IF EXISTS medieval_store_products;
DROP TABLE IF EXISTS game_of_thrones_customers;

-- Customers Table
CREATE TABLE game_of_thrones_customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    house VARCHAR(50),  
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15)
);

-- Products Table
CREATE TABLE medieval_store_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),  
    price DECIMAL(7,2),
    stock_quantity INT DEFAULT 10
);

-- Orders Table
CREATE TABLE customer_orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES game_of_thrones_customers(id),
    product_id INT REFERENCES medieval_store_products(id),
    quantity INT NOT NULL CHECK (quantity > 0),
    total_price DECIMAL(7,2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
