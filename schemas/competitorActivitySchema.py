sqlCreateCompetitorTable = "CREATE TABLE IF NOT EXISTS competitor_activities (ID SERIAL PRIMARY KEY, " \
                                "SHOP_ID INTEGER NOT NULL, " \
                                "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                                "PRODUCT_SUB_TYPE_ID INTEGER NOT NULL, " \
                                "COMMENTS CHARACTER VARYING(50) NOT NULL, " \
                                "IMAGE_PATH CHARACTER VARYING(400), " \
                                "DATE_TODAY TIMESTAMP DEFAULT NOW())"
