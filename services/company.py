from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createCompany(adminId, companyName):
    query = "INSERT INTO company (ADMIN_ID, NAME) VALUES (%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(adminId, companyName))
            getPublicConnection.commit()
            return {'error':-1}
        except Exception as e:
            print(str(e))
            getPublicConnection.rollback()
            return {'error': 1}
