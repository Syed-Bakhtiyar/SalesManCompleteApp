import psycopg2
import base64
import datetime

class Connection():
    def __getconnection__(self):
        return psycopg2.connect(user='Bakhtiyar', password='pakistan', database='salesman', host='localhost')
    
    def getPublicConnection(self):
        return self.connection

    def __init__(self):
        self.connection = self.__getconnection__()

        self.sqlCreateManagerTable = "CREATE TABLE IF NOT EXISTS manager (" \
                                     "ID serial primary key," \
                                     "NAME character varying(255) NOT NULL, " \
                                     "EMAIL character varying(255) NOT NULL UNIQUE," \
                                     "PASSWORD character varying(255) NOT NULL," \
                                     "COMPANYNAME CHARACTER VARYING(50) NOT NULL UNIQUE," \
                                     "ISONLINE BOOLEAN DEFAULT FALSE)"

        self.sqlCreateAreaManagerTable = "CREATE TABLE IF NOT EXISTS area_manager(ID serial primary key," \
                                         "MANAGER_ID INTEGER NOT NULL," \
                                         "NAME CHARACTER VARYING(50) NOT NULL," \
                                         "PASSWORD CHARACTER VARYING(50) NOT NULL," \
                                         "DATE_TODAY TIMESTAMP DEFAULT NOW()," \
                                         "LOCATION_ID INTEGER DEFAULT 0)"

        self.sqlCreateMerchandiserTable = "CREATE TABLE IF NOT EXISTS merchandiser (ID SERIAL PRIMARY KEY," \
                                          "AREA_MANAGER_ID INTEGER NOT NULL," \
                                          "SHOP_ID INTEGER DEFAULT 0," \
                                          "NAME CHARACTER VARYING(50) NOT NULL," \
                                          "EMAIL CHARACTER VARYING(50) NOT NULL UNIQUE," \
                                          "PASSWORD CHARACTER VARYING(50) NOT NULL," \
                                          "COMPANYNAME CHARACTER VARYING(50) NOT NULL UNIQUE," \
                                          "ISONLINE BOOLEAN DEFAULT FALSE," \
                                          "DATETODAY TIMESTAMP DEFAULT NOW())"

        self.sqlCreateShopTable = "CREATE TABLE IF NOT EXISTS shop(ID SERIAL PRIMARY KEY," \
                                  "MANAGER_ID INTEGER DEFAULT 0," \
                                  "MERCH_ID INTEGER DEFAULT 0," \
                                  "SHOP_NAME CHARACTER VARYING(255) NOT NULL DEFAULT '', " \
                                  "IS_ACTIVE BOOLEAN DEFAULT FALSE)"

        self.sqlCreateDisplayTable = "CREATE TABLE IF NOT EXISTS display(ID SERIAL PRIMARY KEY," \
                                     "SHOP_ID INTEGER NOT NULL, " \
                                     "PRODUCT_TYPE_ID INTEGER NOT NULL," \
                                     "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL," \
                                     "COMMENTS CHARACTER VARYING(255) NOT NULL UNIQUE, " \
                                     "IMAGE_PATH CHARACTER VARYING(400) DEFAULT '', " \
                                     "DATE_TODAY TIMESTAMP DEFAULT NOW())"

        self.sqlCreateOurTable = "CREATE TABLE IF NOT EXISTS our_activities (ID SERIAL PRIMARY KEY, " \
                                 "SHOP_ID INTEGER NOT NULL, " \
                                 "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                                 "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
                                 "COMMENTS CHARACTER VARYING(400) NOT NULL, " \
                                 "IMAGE_PATH CHARACTER VARYING(400), " \
                                 "DATE_TODAY TIMESTAMP DEFAULT NOW())"

        self.sqlCreateCompetitorTable = "CREATE TABLE IF NOT EXISTS competitor_activities (ID SERIAL PRIMARY KEY, " \
                                        "SHOP_ID INTEGER NOT NULL, " \
                                        "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                                        "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
                                        "COMMENTS CHARACTER VARYING(50) NOT NULL, " \
                                        "IMAGE_PATH CHARACTER VARYING(400), " \
                                        "DATE_TODAY TIMESTAMP DEFAULT NOW())"

        self.sqlCreatePicturesTable = "CREATE TABLE IF NOT EXISTS pictures (ID SERIAL PRIMARY KEY, " \
                                      "SHOP_ID INTEGER NOT NULL, " \
                                      "COMMENTS CHARACTER VARYING(50) NOT NULL, " \
                                      "IMAGE_PATH CHARACTER VARYING(400), " \
                                      "DATE_TODAY TIMESTAMP DEFAULT NOW())"

        self.sqlCreateProductTypeTable = "CREATE TABLE IF NOT EXISTS product_type_table(ID SERIAL PRIMARY KEY, " \
                                         "MANAGER_ID INTEGER NOT NULL," \
                                         "TITLE CHARACTER VARYING(40) NOT NULL DEFAULT '')";

        self.sqlCreateProductSubTypeTable = "CREATE TABLE IF NOT EXISTS product_sub_type_table(ID SERIAL PRIMARY KEY, " \
                                            "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                                            "TITLE CHARACTER VARYING(40) NOT NULL DEFAULT '')"

        self.sqlCreateProductTable = "CREATE TABLE IF NOT EXISTS product (ID SERIAL PRIMARY KEY, " \
                                     "MANAGER_ID INTEGER NOT NULL," \
                                     "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                                     "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
                                     "TITLE CHARACTER VARYING(40) DEFAULT '', " \
                                     "IMAGE_PATH CHARACTER VARYING(80) DEFAULT '',"\
                                     "ISAVAILABLEPRODUCT BOOLEAN DEFAULT FALSE)"

        self.sqlCreateLatLongTable = "CREATE TABLE IF NOT EXISTS merch_location(ID SERIAL PRIMARY KEY, " \
                                     "MERCH_ID INTEGER DEFAULT 0, " \
                                     "LATITUDE CHARACTER VARYING(80) NOT NULL, " \
                                     "LONGITUDE CHARACTER VARYING(80) NOT NULL)"

        with self.connection.cursor() as cursor:
            cursor.execute(self.sqlCreateManagerTable)
            cursor.execute(self.sqlCreateAreaManagerTable)
            cursor.execute(self.sqlCreateMerchandiserTable)
            cursor.execute(self.sqlCreateShopTable)
            cursor.execute(self.sqlCreateDisplayTable)
            cursor.execute(self.sqlCreateOurTable)
            cursor.execute(self.sqlCreateCompetitorTable)
            cursor.execute(self.sqlCreatePicturesTable)
            cursor.execute(self.sqlCreateProductTypeTable)
            cursor.execute(self.sqlCreateProductSubTypeTable)
            cursor.execute(self.sqlCreateProductTable)
            cursor.execute(self.sqlCreateLatLongTable)
        self.connection.commit()

    def createManager(self,name,email,password,company_name,isonline):
        query = "INSERT INTO manager (NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE) VALUES (%s,%s,%s,%s,%s)";

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query,(name,email,password,company_name,isonline))
                self.connection.commit()
                return {'error':-1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}



    def createAreaManager(self,manager_id,name,password,time_stamp,latitude,longitude):

        location_id = self.createLocationForAreaManager(latitude,longitude);

        print(str(location_id))

        query = "INSERT INTO area_manager(MANAGER_ID,NAME,PASSWORD,DATE_TODAY,LOCATION_ID) VALUES(%s,%s,%s,%s,%s)";

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query,(manager_id,name,password,time_stamp,location_id))
                self.connection.commit()
                return {'error':-1}
            except psycopg2.ProgrammingError as e:
                self.connection.rollback()
                return {'error': 1}
            except psycopg2.InterfaceError as e:
                self.connection = self.__getconnection__()
                with self.connection.cursor() as cursor:
                    cursor.execute(query, (manager_id, name, password, time_stamp, location_id))
                    self.connection.commit()
                    return {'error': -1}

    def createLocationForAreaManager(self,latitude,longitude):

        query = "INSERT INTO merch_location(LATITUDE, LONGITUDE) VALUES (%s,%s) RETURNING ID";

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query,(latitude,longitude))
                self.connection.commit()
                id = cursor.fetchone()[0]
                return id
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return 0

    def createMerchandiser(self,AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,time_stamp):
        query = "INSERT INTO merchandiser(AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,DATETODAY) " \
                 "VALUES(%s,%S,%s,%s,%s,%s,%s,%s)";

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query,(AREA_MANAGER_ID,SHOP_ID,NAME,EMAIL,PASSWORD,COMPANYNAME,ISONLINE,time_stamp))
                self.connection.commit()
                return {'error':-1}
            except Exception as e:
                self.connection.rollback()
                return {'error':1}





    def createShop(self,MANAGER_ID,AREA_MANAGER_ID,MERCH_ID,SHOP_NAME):
        query = "INSERT INTO shop(MANAGER_ID,MERCH_ID,SHOP_NAME) VALUES" \
                 "(%s,%s,%s)";


        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (MANAGER_ID, MERCH_ID, SHOP_NAME))
                self.connection.commit()
                return {'error': -1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error':1}

    def createDisplay(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

        IMAGE_PATH = self.convertBase64ToImage(image);
        query = "INSERT INTO display(SHOP_ID,PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
                "(%s,%s,%s,%s,%s)";
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
                self.connection.commit()
                return {'error':-1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error':1}


    def creatrOurActivity(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

        IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

        query = "INSERT INTO our_activities (SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,$COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
                "(%s,%s,%s,%s,%s,%s)"

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
                self.connection.commit()
                return {'error': -1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}

    def creatrCompActivity(self,SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,COMMENTS,image,DATETODAY):

        IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

        query = "INSERT INTO competitor_activities (SHOP_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,$COMMENTS,IMAGE_PATH,DATETODAY) VALUES " \
                "(%s,%s,%s,%s,%s,%s)"

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (SHOP_ID, PRODUCT_TYPE_ID, PRODUCT_SUB_TYPE_ID, COMMENTS, IMAGE_PATH, DATETODAY))
                self.connection.commit()
                return {'error': -1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}

    def createPictures(self,SHOP_ID,COMMENTS,IMAGE,DATE_TODAY):

        IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';

        query = "INSERT INTO pictures (SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY) VALUES " \
                "(%s,%s,%s,%s)"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query,(SHOP_ID,COMMENTS,IMAGE_PATH,DATE_TODAY))
                self.connection.commit()
                return {'error':-1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}

    # product is available or not
    def createStatus(self,REF_ID,IS_ACTIVE = 0):
        query = "INSERT INTO STATUS (REF_ID,IS_ACTIVE) VALUES " \
                "(%s,%s)"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (REF_ID,IS_ACTIVE ))
                self.connection.commit()
                return {'error': -1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}

    def createProductType(self,manager_id,product_type_title,product_sub_type_title,product_title, image):
        image_path = "image converter"
        query = "INSERT INTO product_type_table (MANAGER_ID,TITLE) VALUES" \
                "(%S,%S) RETURNING ID"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query,(manager_id,product_type_title))
                self.connection.commit()
                product_type_id = cursor.fetchone()['0']
                self.createProductSubType(manager_id,product_type_id,product_sub_type_title,product_title,image_path)
                return {'error': -1}
            except Exception as e:
                self.connection.rollback()
                return {'error': 1}

    def createProductSubType(self,manager_id,product_type_id,title,product_title,image_path):
        query = "INSERT INTO product_sub_type_table(PRODUCT_TYPE_ID,TITLE) VALUES" \
                "(%S,%S) RETURNING ID"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (product_type_id, title))
                self.connection.commit()
                product_sub_type_id = cursor.fetchone()['0']
                self.createProduct(manager_id,product_type_id,product_sub_type_id,product_title,image_path)
                return {'error': -1}
            except Exception as e:
                self.connection.rollback()
                return {'error': 1}

    def createProduct(self,MANAGER_ID,PRODUCT_TYPE_ID = 0,PRODUCT_SUB_TYPE_ID = 0,TITLE = '',IMAGE = ''):
        IMAGE_PATH = 'THERE IS IMAGE CONVERTER FUNCTION WILL CALL';
        query = "INSERT INTO STATUS (MANAGER_ID,PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,TITLE,IMAGE_PATH) VALUES " \
                "(%s,%s,%s,%s,%s)"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (MANAGER_ID, PRODUCT_TYPE_ID,PRODUCT_SUB_TYPE_ID,TITLE,IMAGE_PATH))
                self.connection.commit()
                return {'error': -1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}

    def createIsAvailable(self,PRODUCT_ID,SHOP_ID,ISAVAILABLEPRODUCT):
        query = "INSERT INTO STATUS (PRODUCT_ID,SHOP_ID,ISAVAILABLEPRODUCT) VALUES " \
                "(%s,%s,%s)"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, (PRODUCT_ID,SHOP_ID,ISAVAILABLEPRODUCT))
                self.connection.commit()
                return {'error': -1}
            except Exception as e:
                print(str(e))
                self.connection.rollback()
                return {'error': 1}

    def convertBase64ToImage(self, image):
        date = datetime.datetime.now()
        image_name = 'IMG_' + str(date.day) + "_" + str(date.month) + "_" + str(date.year) + "_" + str(
            date.hour) + "_" + str(date.minute) + "_" + str(date.microsecond) + ".jpg"
        ima_64_decode = base64.b64decode(image)
        with open(image_name, 'wb') as f:
            f.write(ima_64_decode)
            return image_name
        print(str(date.day))
        print(str(date.month))
        print(str(date.year))
        print(str(date.hour))
        print(str(date.minute))
        print(str(date.second))
        print(str(date.microsecond))

connection = Connection();