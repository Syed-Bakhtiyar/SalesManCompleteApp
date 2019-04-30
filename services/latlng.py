from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createLocation(latitude,longitude):
    
    query = "INSERT INTO location(LATITUDE, LONGITUDE) VALUES (%s,%s)";

    with getPublicConnection as cursor:
        try:
            cursor.execute(query,(latitude,longitude))
            getPublicConnection.commit()
            return cursor.lastrowid
        except Exception:
            getPublicConnection.rollback()
            return 0