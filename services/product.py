from database_connection import connection
getPublicConnection = connection.getPublicConnection()

def createProduct(self,MANAGER_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, TITLE, IMAGE_PATH, IS_AVAILABLE):
    IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

    query = "INSERT INTO product (MANAGER_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, TITLE, IMAGE_PATH, ISAVAILABLEPRODUCT) VALUES " \
            "(%s,%s,%s,%s,%s,%s)"
    with self.connection.cursor() as cursor:
        try:
            cursor.execute(query,(MANAGER_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, TITLE, IMAGE_PATH, IS_AVAILABLE))
            self.connection.commit()
            return {'error':-1}
        except Exception:
            self.connection.rollback()
            return {'error': 1}


# sqlCreateProductTable = "CREATE TABLE IF NOT EXISTS product (ID SERIAL PRIMARY KEY, " \
#                                     "MANAGER_ID INTEGER NOT NULL," \
#                                     "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
#                                     "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
#                                     "TITLE CHARACTER VARYING(40) DEFAULT '', " \
#                                     "IMAGE_PATH CHARACTER VARYING(80) DEFAULT '',"\
#                                     "ISAVAILABLEPRODUCT BOOLEAN DEFAULT FALSE)"
