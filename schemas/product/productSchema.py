sqlCreateProductTable = "CREATE TABLE IF NOT EXISTS product (ID SERIAL PRIMARY KEY, " \
                                    "MANAGER_ID INTEGER NOT NULL," \
                                    "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
                                    "TITLE CHARACTER VARYING(40) DEFAULT '', " \
                                    "IMAGE_PATH CHARACTER VARYING(80) DEFAULT '',"\
                                    "ISAVAILABLEPRODUCT BOOLEAN DEFAULT FALSE)"
