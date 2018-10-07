import psycopg2
import base64
import datetime
from schemas.admin import sqlCreateAdminTable
from schemas.company import sqlCreateCompanyTable
from schemas.managerSchema import sqlCreateManagerTable
from schemas.areaManagerSchema import sqlCreateAreaManagerTable
from schemas.merchandiserSchema import sqlCreateMerchandiserTable
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
        return psycopg2.connect(user='Bakhtiyar', password='pakistan', database='store_perfect', host='localhost')
    
    def getPublicConnection(self):
        return self.connection

    def __init__(self):
        self.connection = self.__getconnection__()
        
        with self.connection.cursor() as cursor:
            cursor.execute(sqlCreateAdminTable)
            cursor.execute(sqlCreateManagerTable)
            cursor.execute(sqlCreateCompanyTable)
            cursor.execute(sqlCreateManagerTable)
            cursor.execute(sqlCreateAreaManagerTable)
            cursor.execute(sqlCreateMerchandiserTable)
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

connection = Connection();