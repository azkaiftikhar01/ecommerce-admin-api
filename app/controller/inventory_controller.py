from ..db.connection import get_connection
from ..db.dml.inventory_queries import *

class InventoryController:
    @staticmethod
    def update_inventory(product_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # TODO: Add quantity validation
            cursor.execute(UPDATE_INVENTORY, (product_id, quantity, quantity))
            conn.commit()
            return True, "Inventory updated successfully"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_inventory(product_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_INVENTORY, (product_id,))
            return True, cursor.fetchone()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    # FIXME: Add caching for frequently accessed inventory
    @staticmethod
    def get_all_inventory():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_ALL_INVENTORY)
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_low_stock_products(threshold):
        # TODO: Add dynamic threshold based on product category
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_LOW_STOCK_PRODUCTS, (threshold,))
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_recently_updated_inventory(days):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_RECENTLY_UPDATED_INVENTORY, (days,))
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close() 