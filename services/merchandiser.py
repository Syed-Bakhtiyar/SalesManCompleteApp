from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createMerchandiser(admin_id, first_name, last_name, email, password, role):
    query = "INSERT INTO user (ADMIN_ID, FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ISONLINE, ROLE) VALUES (%s, %s,%s,%s,%s,%s,%s)";
    try:
        getPublicConnection.cursor().execute(query,(admin_id, first_name, last_name, email, password, 1, role))
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

def getAllMerchandisers(admin_id):
    try:
        query = "SELECT * FROM user where ADMIN_ID = " + "'" + admin_id+"' AND ROLE = 'MERCHANDISER'"
        print(query)
        cursor = getPublicConnection.cursor(buffered=True)
        cursor.execute(query)
        merchandisers = cursor.fetchall()
        if not merchandisers:
            return {
                'status': 404,
                'message': 'Not Found'
            }
        return {
                'status': 200,
                'message': merchandisers 
        } 
    except Exception as error:
        print('error ',error)
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }
