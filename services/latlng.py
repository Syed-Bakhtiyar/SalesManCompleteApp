from database_connection import connection
import psycopg2

getPublicConnection = connection.getPublicConnection()

def createLocationForAreaManager(latitude,longitude):
    
    query = "INSERT INTO merch_location(LATITUDE, LONGITUDE) VALUES (%s,%s) RETURNING ID";

    with getPublicConnection as cursor:
        try:
            cursor.execute(query,(latitude,longitude))
            getPublicConnection.commit()
            id = cursor.fetchone()[0]
            return id
        except Exception:
            getPublicConnection.rollback()
            return 0