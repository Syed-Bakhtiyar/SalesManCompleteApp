# import psycopg2
import mysql.connector as mysql
import base64
import datetime
from schemas.user import sqlCreateUser
from schemas.company import sqlCreateCompanyTable
from schemas.shopSchema import sqlCreateShopTable
from schemas.displaySchema import sqlCreateDisplayTable
from schemas.activitySchema import sqlCreateOurTable
from schemas.competitorActivitySchema import sqlCreateCompetitorTable
from schemas.pictureSchema import sqlCreatePicturesTable
from schemas.product.productTypeSchema import sqlCreateProductTypeTable
from schemas.product.productSubTypeSchema import sqlCreateProductSubTypeTable
from schemas.product.productSchema import sqlCreateProductTable
from schemas.latlngSchema import sqlCreateLatLongTable

class Connection():
    def __getconnection__(self):
        return mysql.connect(user='root', password='', database='store_perfect', host='localhost')
    
    def getPublicConnection(self):
        return self.connection

    def __init__(self):
        try:
            self.connection = self.__getconnection__()
            
            with self.connection.cursor() as cursor:
                cursor.execute(sqlCreateUser)
                cursor.execute(sqlCreateCompanyTable)
                cursor.execute(sqlCreateShopTable)
                cursor.execute(sqlCreateDisplayTable)
                cursor.execute(sqlCreateOurTable)
                cursor.execute(sqlCreateCompetitorTable)
                cursor.execute(sqlCreatePicturesTable)
                cursor.execute(sqlCreateProductTypeTable)
                cursor.execute(sqlCreateProductSubTypeTable)
                cursor.execute(sqlCreateProductTable)
                cursor.execute(sqlCreateLatLongTable)
            self.connection.commit()
        except Exception as identifier:
            print(str(identifier))

connection = Connection();