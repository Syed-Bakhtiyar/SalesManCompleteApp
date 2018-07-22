import psycopg2
import base64
import datetime
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
        return psycopg2.connect(user='Bakhtiyar', password='pakistan', database='salesman', host='localhost')
    
    def getPublicConnection(self):
        return self.connection

    def __init__(self):
        self.connection = self.__getconnection__()
        
        with self.connection.cursor() as cursor:
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

    # def createManager(self,name,email,password,company_name,isonline):
    #     query = "INSERT INTO manager (NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE) VALUES (%s,%s,%s,%s,%s)";

    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(name,email,password,company_name,isonline))
    #             self.connection.commit()
    #             return {'error':-1}
    #         except Exception as e:
    #             print(str(e))
    #             self.connection.rollback()
    #             return {'error': 1}

    # def updateManager(self, id,name,company_name):
    #     query = "UPDATE manager SET NAME = %s, COMPANYNAME = %s WHERE id = "+str(id);

    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(name,company_name))
    #             self.connection.commit()
    #             return {'error':-1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error': 1}


    # def createAreaManager(self,manager_id,name,password,time_stamp,latitude,longitude):
    #     location_id = self.createLocationForAreaManager(latitude,longitude);
    #     print(str(location_id))
    #     query = "INSERT INTO area_manager(MANAGER_ID,NAME,PASSWORD,DATE_TODAY,LOCATION_ID) VALUES(%s,%s,%s,%s,%s)";
    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(manager_id,name,password,time_stamp,location_id))
    #             self.connection.commit()
    #             return {'error':-1}
    #         except psycopg2.ProgrammingError:
    #             self.connection.rollback()
    #             return {'error': 1}
    #         except psycopg2.InterfaceError:
    #             self.connection = self.__getconnection__()
    #             with self.connection.cursor() as cursor:
    #                 cursor.execute(query, (manager_id, name, password, time_stamp, location_id))
    #                 self.connection.commit()
    #                 return {'error': -1}

    # def createLocationForAreaManager(self,latitude,longitude):

    #     query = "INSERT INTO merch_location(LATITUDE, LONGITUDE) VALUES (%s,%s) RETURNING ID";

    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(latitude,longitude))
    #             self.connection.commit()
    #             id = cursor.fetchone()[0]
    #             return id
    #         except Exception:
    #             self.connection.rollback()
    #             return 0

    # def createMerchandiser(self,AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,time_stamp):
    #     query = "INSERT INTO merchandiser(AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,DATETODAY) " \
    #              "VALUES(%s,%S,%s,%s,%s,%s,%s,%s)";

    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,time_stamp))
    #             self.connection.commit()
    #             return {'error':-1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error':1}


    # def createShop(self,MANAGER_ID,AREA_MANAGER_ID,MERCH_ID,SHOP_NAME):
    #     query = "INSERT INTO shop(MANAGER_ID,MERCH_ID,SHOP_NAME) VALUES" \
    #              "(%s,%s,%s)";


    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query, (MANAGER_ID, MERCH_ID, SHOP_NAME))
    #             self.connection.commit()
    #             return {'error': -1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error':1}

    # def createDisplay(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    #     IMAGE_PATH = self.convertBase64ToImage(image);
    #     query = "INSERT INTO display(SHOP_ID,PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
    #             "(%s,%s,%s,%s,%s)";
    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
    #             self.connection.commit()
    #             return {'error':-1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error':1}


    # def creatrOurActivity(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    #     IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

    #     query = "INSERT INTO our_activities (SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,$COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
    #             "(%s,%s,%s,%s,%s,%s)"

    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
    #             self.connection.commit()
    #             return {'error': -1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error': 1}

    # def creatrCompActivity(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

    #     IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

    #     query = "INSERT INTO competitor_activities (SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,$COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
    #             "(%s,%s,%s,%s,%s,%s)"

    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
    #             self.connection.commit()
    #             return {'error': -1}
    #         except Exception as e:
    #             print(str(e))
    #             self.connection.rollback()
    #             return {'error': 1}

    # def createPictures(self,SHOP_ID,COMMENTS,IMAGE,DATE_TODAY):
    #     IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

    #     query = "INSERT INTO pictures (SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY) VALUES " \
    #             "(%s,%s,%s,%s)"
    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY))
    #             self.connection.commit()
    #             return {'error':-1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error': 1}

    # def createProductType(self,manager_id,product_type_title,product_sub_type_title,product_title, image):
    #     image_path = "image converter"
    #     query = "INSERT INTO product_type_table (MANAGER_ID,TITLE) VALUES" \
    #             "(%S,%S) RETURNING ID"
    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query,(manager_id,product_type_title))
    #             self.connection.commit()
    #             product_type_id = cursor.fetchone()['0']
    #             self.createProductSubType(manager_id,product_type_id,product_sub_type_title,product_title,image_path)
    #             return {'error': -1}
    #         except Exception:
    #             return {'error': 1}

    # def createProductSubType(self,manager_id,product_type_id,title,product_title,image_path):
    #     query = "INSERT INTO product_sub_type_table(PRODUCT_TYPE_ID,TITLE) VALUES" \
    #             "(%S,%S) RETURNING ID"
    #     with self.connection.cursor() as cursor:
    #         try:
    #             cursor.execute(query, (product_type_id, title))
    #             self.connection.commit()
    #             product_sub_type_id = cursor.fetchone()['0']
    #             self.createProduct(manager_id,product_type_id,product_sub_type_id,product_title,image_path)
    #             return {'error': -1}
    #         except Exception:
    #             self.connection.rollback()
    #             return {'error': 1}

    def convertBase64ToImage(self, image):
        date = datetime.datetime.now()
        image_name = 'IMG_' + str(date.day) + "_" + str(date.month) + "_" + str(date.year) + "_" + str(
            date.hour) + "_" + str(date.minute) + "_" + str(date.microsecond) + ".jpg"
        ima_64_decode = base64.b64decode(image)
        with open(image_name, 'wb') as f:
            f.write(ima_64_decode)
            return image_name

connection = Connection();