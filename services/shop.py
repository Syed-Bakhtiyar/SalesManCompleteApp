from database_connection import connection
from services.latlng import createLocation
getPublicConnection = connection.getPublicConnection()

def createShop(company_id, shop_name, latitude, longitude):
    # COMPANY_ID INT DEFAULT NULL," \
    # "LOCATION_ID INT DEFAULT NULL,"
    #                     "SHOP_NAME VARCHAR(255) NOT NULL DEFAULT ''," \
    #                     "IS_ACTIVE TINYINT(1) DEFAULT 0,"\
    location_id = None
    if latitude > 0 and longitude > 0:
        location_id = createLocation(latitude, longitude)

    query = "INSERT INTO shop(COMPANY_ID, LOCATION_ID, SHOP_NAME) VALUES" \
             "(%s,%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query, (company_id, location_id, shop_name))
            getPublicConnection.commit()
            return {'error': -1}
        except Exception:
            getPublicConnection.rollback()
            return {'error':1}
