from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createShop(self,MANAGER_ID,AREA_MANAGER_ID,MERCH_ID,SHOP_NAME):
    query = "INSERT INTO shop(MANAGER_ID,MERCH_ID,SHOP_NAME) VALUES" \
             "(%s,%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query, (MANAGER_ID, MERCH_ID, SHOP_NAME))
            self.connection.commit()
            return {'error': -1}
        except Exception:
            self.connection.rollback()
            return {'error':1}
