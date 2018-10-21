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
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }

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

def updateCompany(company_id, name):
    query = "UPDATE company SET NAME = %s WHERE ID = %s"
    try:
        getPublicConnection.cursor().execute(query,(name, company_id))
        getPublicConnection.commit()
        return {
            'message': 'Updated Successfully'
        }
    except Exception as error:
        print(str(error))
        getPublicConnection.rollback()
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }

def deleteCompany(company_id):
    query = 'DELETE FROM company where ID = %s'
    try:    
        getPublicConnection.cursor().execute(query,(str(company_id),))
        getPublicConnection.commit()
        return {
            'message': 'Deleted Successfully'
        }
    except Exception as error:
        print(str(error))
        getPublicConnection.rollback()
        return {
                'status': 500,
                'message': 'Internal Server Error'
        }