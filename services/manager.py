from database_connection import connection

getPublicConnection = connection.getPublicConnection()

def createManager(admin_id, first_name, last_name, email, password, role):
    query = "INSERT INTO user (ADMIN_ID, FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, ISONLINE, ROLE) VALUES (%s, %s, %s, %s, %s, %s, %s)";
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

def getAllManagers(admin_id):
    try:
        query = "SELECT * FROM user where ADMIN_ID = " + "'" + admin_id+"' AND ROLE = 'MANAGER'"
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

# def createManager(name,email,password,company_name,isonline):
#     query = "INSERT INTO manager (NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE) VALUES (%s,%s,%s,%s,%s)";
#     with getPublicConnection.cursor() as cursor:
#         try:
#             cursor.execute(query,(name,email,password,company_name,isonline))
#             getPublicConnection.commit()
#             return {'error':-1}
#         except Exception as e:
#             print(str(e))
#             getPublicConnection.rollback()
#             return {'error': 1}

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

