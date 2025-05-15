# Inventory DML Queries
UPDATE_INVENTORY = """
INSERT INTO inventory (product_id, quantity) 
VALUES (%s, %s) 
ON DUPLICATE KEY UPDATE quantity = %s
"""

GET_INVENTORY = """
SELECT i.id, p.name as product_name, i.quantity, i.last_updated 
FROM inventory i 
JOIN products p ON i.product_id = p.id 
WHERE i.product_id = %s
"""

GET_ALL_INVENTORY = """
SELECT i.id, p.name as product_name, i.quantity, i.last_updated 
FROM inventory i 
JOIN products p ON i.product_id = p.id 
ORDER BY p.name
"""

# New optimized queries
GET_LOW_STOCK_PRODUCTS = """
SELECT i.id, p.name as product_name, i.quantity, i.last_updated 
FROM inventory i 
JOIN products p ON i.product_id = p.id 
WHERE i.quantity <= %s
ORDER BY i.quantity
"""

GET_RECENTLY_UPDATED_INVENTORY = """
SELECT i.id, p.name as product_name, i.quantity, i.last_updated 
FROM inventory i 
JOIN products p ON i.product_id = p.id 
WHERE i.last_updated >= %s
ORDER BY i.last_updated DESC
"""

# Index for faster inventory lookups
CREATE_INVENTORY_INDEX = """
CREATE INDEX IF NOT EXISTS idx_inventory_product ON inventory(product_id)
""" 