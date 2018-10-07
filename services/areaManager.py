from database_connection import connection
from common.common import convertBase64ToImage
from services.latlng import createLocation
import psycopg2

getPublicConnection = connection.getPublicConnection()

def addAreaManager(manager_id, first_name, last_name, email, password, role):
    query = "INSERT INTO user (MANAGER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ISONLINE, ROLE) VALUES (%s, %s,%s,%s,%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(manager_id, first_name, last_name, email, password, 1, role))
            getPublicConnection.commit()
            return {
                'id': cursor.lastrowid,
                'admin_id': manager_id,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password
            }
        except Exception as e:
            print(str(e))
            getPublicConnection.rollback()
            return {'error': 1}

# def addAreaManager(self,manager_id,name,password,time_stamp,latitude,longitude):
#         location_id = createLocationForAreaManager(latitude,longitude);
#         print(str(location_id))
#         query = "INSERT INTO area_manager(MANAGER_ID,NAME,PASSWORD,DATE_TODAY,LOCATION_ID) VALUES(%s,%s,%s,%s,%s)";
#         with getPublicConnection as cursor:
#             try:
#                 cursor.execute(query,(manager_id,name,password,time_stamp,location_id))
#                 getPublicConnection.commit()
#                 return {'error':-1}
#             except psycopg2.ProgrammingError:
#                 getPublicConnection.rollback()
#                 return {'error': 1}
#             except psycopg2.InterfaceError:
#                 getPublicConnection = self.__getconnection__()
#                 with getPublicConnection.cursor() as cursor:
#                     cursor.execute(query, (manager_id, name, password, time_stamp, location_id))
#                     getPublicConnection.commit()
#                     return {'error': -1}
