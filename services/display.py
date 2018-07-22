from database_connection import connection
getPublicConnection = connection.getPublicConnection()


def createDisplay(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    IMAGE_PATH = self.convertBase64ToImage(image);
    query = "INSERT INTO display(SHOP_ID,PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
            "(%s,%s,%s,%s,%s)";
    with getPublicConnection as cursor:
        try:
            cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
            self.connection.commit()
            return {'error':-1}
        except Exception:
            self.connection.rollback()
            return {'error':1}
