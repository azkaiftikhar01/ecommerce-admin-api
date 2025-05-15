from ..db.dml.category_queries import *


from ..db.connection import get_connection

class CategoryController:
    @staticmethod
    #method to create a new category 
    def create_category(name):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(CREATE_CATEGORY, (name,))
            conn.commit()
            return True, "new category added!"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_all_categories():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_ALL_CATEGORIES)
            return True, cursor.fetchall()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()



    @staticmethod
    def get_category_by_id(category_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(GET_CATEGORY_BY_ID, (category_id,))
            return True, cursor.fetchone()
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_category(category_id, name):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(UPDATE_CATEGORY, (name, category_id))
            conn.commit()
            return True, "category for " + name + " is updated!"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_category(category_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(DELETE_CATEGORY, (category_id,))
            conn.commit()
            return True, "the category with id " + str(category_id) + " is deleted"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cursor.close()
            conn.close() 