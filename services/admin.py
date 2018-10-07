from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createAdmin(name,email,password,isonline):
    query = "INSERT INTO admin (NAME,EMAIL,PASSWORD,ISONLINE) VALUES (%s,%s,%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(name,email,password,isonline))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception as e:
            print(str(e))
            getPublicConnection.rollback()
            return {'error': 1}
