sqlCreateOurTable = "CREATE TABLE IF NOT EXISTS our_activities (ID SERIAL PRIMARY KEY, " \
                            "SHOP_ID INTEGER NOT NULL, " \
                            "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                            "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
                            "COMMENTS CHARACTER VARYING(400) NOT NULL, " \
                            "IMAGE_PATH CHARACTER VARYING(400), " \
                            "DATE_TODAY TIMESTAMP DEFAULT NOW())"
