-- Insert Customers
INSERT INTO game_of_thrones_customers (first_name, last_name, house, email, phone) VALUES
('Jon', 'Snow', 'Stark', 'jon.snow@westeros.com', '111-222-3333'),
('Daenerys', 'Targaryen', 'Targaryen', 'daenerys@westeros.com', '222-333-4444'),
('Tyrion', 'Lannister', 'Lannister', 'tyrion@westeros.com', '333-444-5555'),
('Arya', 'Stark', 'Stark', 'arya@westeros.com', '444-555-6666'),
('Cersei', 'Lannister', 'Lannister', 'cersei@westeros.com', '555-666-7777'),
('Bran', 'Stark', 'Stark', 'bran@westeros.com', '666-777-8888'),
('Jaime', 'Lannister', 'Lannister', 'jaime@westeros.com', '777-888-9999'),
('Sansa', 'Stark', 'Stark', 'sansa@westeros.com', '888-999-0000'),
('Brienne', 'Tarth', 'Tarth', 'brienne@westeros.com', '999-000-1111'),
('Theon', 'Greyjoy', 'Greyjoy', 'theon@westeros.com', '000-111-2222');

-- Insert Products
INSERT INTO medieval_store_products (name, category, price, stock_quantity) VALUES
('Valyrian Steel Sword', 'Weapon', 1000.00, 5),
('Dragonglass Dagger', 'Weapon', 250.00, 10),
('Castle-forged Armor', 'Armor', 500.00, 8),
('Wildfire Potion', 'Potion', 300.00, 15),
('Maester’s Healing Potion', 'Potion', 100.00, 20),
('Direwolf Cloak', 'Armor', 200.00, 12),
('White Walker Spear', 'Weapon', 700.00, 3),
('King’s Crown', 'Magic Item', 1500.00, 2);

-- Insert Orders
INSERT INTO customer_orders (customer_id, product_id, quantity, total_price) VALUES
(1, 1, 1, 1000.00),  -- Jon Snow buys Valyrian Steel Sword
(2, 2, 2, 500.00),  -- Daenerys buys 2 Dragonglass Daggers
(3, 4, 3, 900.00),  -- Tyrion buys 3 Wildfire Potions
(4, 5, 5, 500.00),  -- Arya buys 5 Healing Potions
(5, 8, 1, 1500.00), -- Cersei buys a King’s Crown
(6, 6, 2, 400.00),  -- Bran buys 2 Direwolf Cloaks
(7, 3, 1, 500.00),  -- Jaime buys Castle-forged Armor
(8, 7, 1, 700.00),  -- Sansa buys a White Walker Spear
(9, 5, 1, 100.00),  -- Brienne buys a Healing Potion
(10, 4, 2, 600.00); -- Theon buys 2 Wildfire Potions
