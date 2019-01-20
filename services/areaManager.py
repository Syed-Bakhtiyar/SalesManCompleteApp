from database_connection import connection
from common.common import convertBase64ToImage
from services.latlng import createLocation
import psycopg2

getPublicConnection = connection.getPublicConnection()

def addAreaManager(admin_id, first_name, last_name, email, password, role):
    query = "INSERT INTO user (ADMIN_ID, FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ISONLINE, ROLE) VALUES (%s, %s,%s,%s,%s,%s, %s)";
    try:
        getPublicConnection.cursor().execute(query,(admin_id,first_name, last_name, email, password, 1, role))
        getPublicConnection.commit()
        print(str(getPublicConnection) + 'this isssssssssss')
        return {
            'id': 1,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }
    except Exception as e:
        print(str(e))
        getPublicConnection.rollback()
        raise e

def getAllAreaManagers(admin_id):
    try:
        query = "SELECT * FROM user where ADMIN_ID = " + "'" + admin_id+"' AND ROLE = 'AREAMANAGER'"
        print(query)
        cursor = getPublicConnection.cursor(buffered=True)
        cursor.execute(query)
        managers = cursor.fetchall()
        if not managers:
            return {
                'status': 404,
                'message': 'Not Found'
            }
        return {
                'status': 200,
                'message': managers 
        } 
    except Exception as error:
        print('error ',error)
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }

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
