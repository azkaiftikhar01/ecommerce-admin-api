# Product DML Queries
CREATE_PRODUCT = """
INSERT INTO products (name, category_id, price) 
VALUES (%s, %s, %s)
"""

GET_ALL_PRODUCTS = """
SELECT p.id, p.name, p.price, p.created_at, c.name as category_name 
FROM products p 
LEFT JOIN categories c ON p.category_id = c.id 
ORDER BY p.name
"""

GET_PRODUCT_BY_ID = """
SELECT p.id, p.name, p.price, p.created_at, c.name as category_name 
FROM products p 
LEFT JOIN categories c ON p.category_id = c.id 
WHERE p.id = %s
"""

# New optimized queries
GET_PRODUCTS_BY_CATEGORY = """
SELECT p.id, p.name, p.price, p.created_at, c.name as category_name 
FROM products p 
LEFT JOIN categories c ON p.category_id = c.id 
WHERE p.category_id = %s
ORDER BY p.name
"""

GET_PRODUCTS_BY_PRICE_RANGE = """
SELECT p.id, p.name, p.price, p.created_at, c.name as category_name 
FROM products p 
LEFT JOIN categories c ON p.category_id = c.id 
WHERE p.price BETWEEN %s AND %s
ORDER BY p.price
"""

GET_PRODUCTS_BY_CATEGORY_AND_PRICE = """
SELECT p.id, p.name, p.price, p.created_at, c.name as category_name 
FROM products p 
LEFT JOIN categories c ON p.category_id = c.id 
WHERE p.category_id = %s AND p.price <= %s
ORDER BY p.price
"""

UPDATE_PRODUCT = """
UPDATE products 
SET name = %s, category_id = %s, price = %s 
WHERE id = %s
"""

DELETE_PRODUCT = """
DELETE FROM products 
WHERE id = %s
"""

# Indexes for faster product searches
CREATE_PRODUCT_INDEXES = """
CREATE INDEX IF NOT EXISTS idx_product_name ON products(name);
CREATE INDEX IF NOT EXISTS idx_product_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_product_price ON products(price);
""" 