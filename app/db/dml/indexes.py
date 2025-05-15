# Create indexes for better query performance
CREATE_INDEXES = """
-- Drop existing indexes
DROP INDEX idx_category_name ON categories;
DROP INDEX idx_product_name ON products;
DROP INDEX idx_product_category ON products;
DROP INDEX idx_product_price ON products;
DROP INDEX idx_product_created ON products;
DROP INDEX idx_inventory_product ON inventory;
DROP INDEX idx_inventory_updated ON inventory;
DROP INDEX idx_sales_product ON sales;
DROP INDEX idx_sales_date ON sales;
DROP INDEX idx_sales_price ON sales;
DROP INDEX idx_product_category_price ON products;
DROP INDEX idx_inventory_product_quantity ON inventory;

-- Category indexes
CREATE INDEX idx_category_name ON categories(name);

-- Product indexes
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_price ON products(price);
CREATE INDEX idx_product_created ON products(created_at);

-- Inventory indexes
CREATE INDEX idx_inventory_product ON inventory(product_id);
CREATE INDEX idx_inventory_updated ON inventory(last_updated);

-- Sales indexes
CREATE INDEX idx_sales_product ON sales(product_id);
CREATE INDEX idx_sales_date ON sales(sale_date);
CREATE INDEX idx_sales_price ON sales(sale_price);

-- Composite indexes for common query patterns
CREATE INDEX idx_product_category_price ON products(category_id, price);
CREATE INDEX idx_inventory_product_quantity ON inventory(product_id, quantity);
""" 