from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createCompany(adminId, companyName):
    query = "INSERT INTO company (ADMIN_ID, NAME) VALUES (%s,%s)";
    try:
        getPublicConnection.cursor().execute(query,(adminId, companyName))
        getPublicConnection.commit()
        print(str(getPublicConnection) + 'this isssssssssss')
        return {
            'id': getPublicConnection.cursor().lastrowid,
            'name': companyName,
            'adminId': adminId
        }
    except Exception as e:
        print(str(e))
        getPublicConnection.rollback()
        return {'error': 1}

def getAllCompanies(admin_id):
    try:
        query = "SELECT * FROM company where ADMIN_ID = " + "'" + admin_id+"'"
        print(query)
        cursor = getPublicConnection.cursor(buffered=True)
        cursor.execute(query)
        companies = cursor.fetchall()
        if not companies:
            return {
                'status': 404,
                'message': 'Not Found'
            }
        return {
                'status': 200,
                'message': companies 
        } 
    except Exception as error:
        print('error ',error)
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }
    