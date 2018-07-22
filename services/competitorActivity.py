from database_connection import connection
getPublicConnection = connection.getPublicConnection()

def creatrCompActivity(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

    query = "INSERT INTO competitor_activities (SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,$COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
            "(%s,%s,%s,%s,%s,%s)"

    with self.connection.cursor() as cursor:
        try:
            cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
            self.connection.commit()
            return {'error': -1}
        except Exception as e:
            print(str(e))
            self.connection.rollback()
            return {'error': 1}

