from database_connection import connection
getPublicConnection = connection.getPublicConnection()

def createUser(first_name, last_name, email, password, role):
    query = "INSERT INTO user (FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ISONLINE, ROLE) VALUES (%s,%s,%s,%s,%s)";
    with getPublicConnection.cursor() as cursor:
        try:
            cursor.execute(query,(first_name, last_name, email, password, 1, role))
            getPublicConnection.commit()
            return {
                'id': cursor.lastrowid,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password
            }
        except Exception as e:
            print(str(e))
            getPublicConnection.rollback()
            return {'error': 1}

