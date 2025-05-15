import mysql.connector
from datetime import datetime, timedelta
import random
import csv
import os
from app.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')

    try:
        # Read and insert categories
        with open(os.path.join(data_dir, 'categories.csv'), 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO categories (id, name) VALUES (%s, %s)",
                    (row['id'], row['name'])
                )

        # Read and insert products
        with open(os.path.join(data_dir, 'products.csv'), 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO products (name, category_id, price) VALUES (%s, %s, %s)",
                    (row['name'], row['category_id'], row['price'])
                )

        # Get all product IDs
        cursor.execute("SELECT id FROM products")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert inventory data
        for product_id in product_ids:
            quantity = random.randint(10, 100)
            cursor.execute(
                "INSERT INTO inventory (product_id, quantity) VALUES (%s, %s)",
                (product_id, quantity)
            )

        # Generate sales data for the last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)

        for product_id in product_ids:
            # Generate 1-5 sales per product
            num_sales = random.randint(1, 5)
            for _ in range(num_sales):
                sale_date = start_date + timedelta(
                    seconds=random.randint(0, int((end_date - start_date).total_seconds()))
                )
                quantity_sold = random.randint(1, 5)
                
                # Get product price
                cursor.execute("SELECT price FROM products WHERE id = %s", (product_id,))
                base_price = cursor.fetchone()[0]
                
                # Add some random discount (0-20%)
                discount = random.uniform(0, 0.2)
                sale_price = base_price * (1 - discount)
                
                cursor.execute(
                    "INSERT INTO sales (product_id, quantity_sold, sale_price, sale_date) VALUES (%s, %s, %s, %s)",
                    (product_id, quantity_sold, round(sale_price, 2), sale_date)
                )

        conn.commit()
        print("Database seeded successfully!")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        conn.rollback()
    except FileNotFoundError as err:
        print(f"File Error: {err}")
        conn.rollback()
    except Exception as err:
        print(f"Unexpected Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    seed_database() 