from database_connection import connection
from roles import ROLES
getPublicConnection = connection.getPublicConnection()

def createAdmin(first_name, last_name, email, password, role):
    query = "INSERT INTO user (FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ISONLINE, ROLE) VALUES (%s,%s,%s,%s,%s,%s)";
    # with getPublicConnection.cursor() as cursor:
    try:
        getPublicConnection.cursor().execute(query,(first_name, last_name, email, password, 1, role))
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

def authenticateUser(email, password):
    try:
        query = "SELECT * FROM user where EMAIL = "+ "'"+ email +"'"+" AND PASSWORD = " + "'" + password+ "'"
        print(query)
        cursor = getPublicConnection.cursor(buffered=True)
        cursor.execute(query)
        user = cursor.fetchone()
        if not user:
            return {
                'status': 401,
                'message': 'User Not Authenticated'
            }
        return {
                'status': 200,
                'message': user[0] 
        } 
    except Exception as identifier:
        print('error ',identifier)
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }