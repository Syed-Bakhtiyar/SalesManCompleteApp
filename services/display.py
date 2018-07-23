from database_connection import connection
from common.common import convertBase64ToImage

getPublicConnection = connection.getPublicConnection()

def createDisplay(SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    IMAGE_PATH = convertBase64ToImage(image);
    query = "INSERT INTO display(SHOP_ID,PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
            "(%s,%s,%s,%s,%s)";
    with getPublicConnection as cursor:
        try:
            cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception:
            getPublicConnection.rollback()
            return {'error':1}
