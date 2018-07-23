from database_connection import connection
from common.common import convertBase64ToImage
getPublicConnection = connection.getPublicConnection()

def createPictures(self,SHOP_ID,COMMENTS,IMAGE,DATE_TODAY):
    IMAGE_PATH = convertBase64ToImage(image)
    query = "INSERT INTO pictures (SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY) VALUES " \
            "(%s,%s,%s,%s)"
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception:
            getPublicConnection.rollback()
            return {'error': 1}
