from database_connection import connection
from latlng import createLocationForAreaManager
import psycopg2

getPublicConnection = connection.getPublicConnection()

def addAreaManager(self,manager_id,name,password,time_stamp,latitude,longitude):
        location_id = createLocationForAreaManager(latitude,longitude);
        print(str(location_id))
        query = "INSERT INTO area_manager(MANAGER_ID,NAME,PASSWORD,DATE_TODAY,LOCATION_ID) VALUES(%s,%s,%s,%s,%s)";
        with getPublicConnection as cursor:
            try:
                cursor.execute(query,(manager_id,name,password,time_stamp,location_id))
                self.connection.commit()
                return {'error':-1}
            except psycopg2.ProgrammingError:
                self.connection.rollback()
                return {'error': 1}
            except psycopg2.InterfaceError:
                self.connection = self.__getconnection__()
                with self.connection.cursor() as cursor:
                    cursor.execute(query, (manager_id, name, password, time_stamp, location_id))
                    self.connection.commit()
                    return {'error': -1}
