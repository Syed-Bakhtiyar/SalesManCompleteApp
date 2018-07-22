sqlCreateDisplayTable = "CREATE TABLE IF NOT EXISTS display(ID SERIAL PRIMARY KEY," \
                                "SHOP_ID INTEGER NOT NULL, " \
                                "PRODUCT_TYPE_ID INTEGER NOT NULL," \
                                "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL," \
                                "COMMENTS CHARACTER VARYING(255) NOT NULL UNIQUE, " \
                                "IMAGE_PATH CHARACTER VARYING(400) DEFAULT '', " \
                                "DATE_TODAY TIMESTAMP DEFAULT NOW())"
