from database_connection import connection
getPublicConnection = connection.getPublicConnection()

def createPictures(self,SHOP_ID,COMMENTS,IMAGE,DATE_TODAY):
    IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

    query = "INSERT INTO pictures (SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY) VALUES " \
            "(%s,%s,%s,%s)"
    with self.connection.cursor() as cursor:
        try:
            cursor.execute(query,(SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY))
            self.connection.commit()
            return {'error':-1}
        except Exception:
            self.connection.rollback()
            return {'error': 1}
