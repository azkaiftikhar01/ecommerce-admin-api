# Category DML Queries
CREATE_CATEGORY = """INSERT INTO categories (name) VALUES (%s)"""

GET_ALL_CATEGORIES = """SELECT id, name FROM categories ORDER BY name"""

GET_CATEGORY_BY_ID = """SELECT id, name FROM categories WHERE id = %s"""

UPDATE_CATEGORY = """UPDATE categories 
SET name = %s 
WHERE id = %s
"""

DELETE_CATEGORY = """DELETE FROM categories 
WHERE id = %s
"""

# Index for faster category name searches
CREATE_CATEGORY_NAME_INDEX = """
CREATE INDEX IF NOT EXISTS idx_category_name ON categories(name)
""" 