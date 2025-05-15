from ..db.connection import get_connection
from ..db.dml.product_queries import *

class ProductController:
    @staticmethod
    def create_product(name, category_id, price):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(CREATE_PRODUCT, (name, category_id, price))
            conn.commit()
            return True, "Product created successfully"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_all_products():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_ALL_PRODUCTS)
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_product_by_id(product_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_PRODUCT_BY_ID, (product_id,))
            return True, cursor.fetchone()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_products_by_category(category_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_PRODUCTS_BY_CATEGORY, (category_id,))
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_products_by_price_range(min_price, max_price):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_PRODUCTS_BY_PRICE_RANGE, (min_price, max_price))
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_products_by_category_and_price(category_id, max_price):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_PRODUCTS_BY_CATEGORY_AND_PRICE, (category_id, max_price))
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_product(product_id, name, category_id, price):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(UPDATE_PRODUCT, (name, category_id, price, product_id))
            conn.commit()
            return True, "Product updated successfully"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_product(product_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(DELETE_PRODUCT, (product_id,))
            conn.commit()
            return True, "Product deleted successfully"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close() 