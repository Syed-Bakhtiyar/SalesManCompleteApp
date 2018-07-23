from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createManager(name,email,password,company_name,isonline):
    query = "INSERT INTO manager (NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE) VALUES (%s,%s,%s,%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(name,email,password,company_name,isonline))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception as e:
            print(str(e))
            getPublicConnection.rollback()
            return {'error': 1}

def updateManager(self, id,name,company_name):
    query = "UPDATE manager SET NAME = %s, COMPANYNAME = %s WHERE id = "+str(id);

    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(name,company_name))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception:
            getPublicConnection.rollback()
            return {'error': 1}

