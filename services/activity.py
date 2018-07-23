from database_connection import connection
from common.common import convertBase64ToImage
getPublicConnection = connection.getPublicConnection()

def creatrOurActivity(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    IMAGE_PATH = convertBase64ToImage(image)

    query = "INSERT INTO our_activities (SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,$COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
            "(%s,%s,%s,%s,%s,%s)"

    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
            getPublicConnection.commit()
            return {'error': -1}
        except Exception:
            getPublicConnection.rollback()
            return {'error': 1}
