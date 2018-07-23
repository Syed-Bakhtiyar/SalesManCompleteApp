from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createMerchandiser(self,AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,time_stamp):
        query = "INSERT INTO merchandiser(AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,DATETODAY) " \
                "VALUES(%s,%S,%s,%s,%s,%s,%s,%s)";
        with getPublicConnection as cursor:
            try:
                cursor.execute(query,(AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,time_stamp))
                getPublicConnection.commit()
                return {'error':-1}
            except Exception:
                getPublicConnection.rollback()
                return {'error':1}
