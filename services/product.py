from database_connection import connection
from common.common import convertBase64ToImage
getPublicConnection = connection.getPublicConnection()

def createProduct(MANAGER_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, TITLE, IMAGE, IS_AVAILABLE):
    IMAGE_PATH = convertBase64ToImage(IMAGE)

    query = "INSERT INTO product (MANAGER_ID, PRODUCT_SUB_TYPE_ID, TITLE, IMAGE_PATH, ISAVAILABLEPRODUCT) VALUES " \
            "(%s,%s,%s,%s,%s)"
    with getPublicConnection as cursor:
        try:
            cursor.execute(query,(MANAGER_ID, PRODUCT_SUB_TYPE_ID, TITLE, IMAGE_PATH, IS_AVAILABLE))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception:
            getPublicConnection.rollback()
            return {'error': 1}


def createProductType(MANAGER_ID, TITLE):
    query = "INSERT INTO product_type_table (MANAGER_ID, TITLE) VALUES " \
            "(%s,%s)"
    with getPublicConnection as cursor:
        try:
            cursor.execute(query,(MANAGER_ID, TITLE))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception:
            getPublicConnection.rollback()
            return {'error': 1}

def createProductSubType(PRODUCT_TYPE_ID, TITLE):
    query = "INSERT INTO product_sub_type_table (PRODUCT_TYPE_ID, TITLE) VALUES " \
            "(%s,%s)"
    with getPublicConnection as cursor:
        try:
            cursor.execute(query,(PRODUCT_TYPE_ID, TITLE))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception:
            getPublicConnection.rollback()
            return {'error': 1}
