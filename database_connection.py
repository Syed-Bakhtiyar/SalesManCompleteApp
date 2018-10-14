# import psycopg2
import mysql.connector
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
        # print(mysql.connect(user='root', password='', database='store_perfect', host='localhost'))
        return mysql.connector.connect(user='root', password='', database='store_perfect', host='localhost')
    
    def getPublicConnection(self):
        return self.connection

    def __init__(self):
        self.connection = self.__getconnection__()
        self.createTable()
            
    def createTable(self):
        try:
            self.connection = self.__getconnection__()
            self.connection.cursor().execute(sqlCreateUser)
            self.connection.cursor().execute(sqlCreateCompanyTable)
            self.connection.cursor().execute(sqlCreateShopTable)
            self.connection.cursor().execute(sqlCreateProductTypeTable)
            self.connection.cursor().execute(sqlCreateProductSubTypeTable)
            self.connection.cursor().execute(sqlCreateProductTable)
            self.connection.cursor().execute(sqlCreateDisplayTable)
            self.connection.cursor().execute(sqlCreateOurTable)
            self.connection.cursor().execute(sqlCreateCompetitorTable)
            self.connection.cursor().execute(sqlCreatePicturesTable)
            self.connection.cursor().execute(sqlCreateLatLongTable)
            self.connection.commit()
        except Exception as error:
            print(error)
connection = Connection();