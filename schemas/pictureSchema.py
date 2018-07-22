sqlCreatePicturesTable = "CREATE TABLE IF NOT EXISTS pictures (ID SERIAL PRIMARY KEY, " \
                                "SHOP_ID INTEGER NOT NULL, " \
                                "COMMENTS CHARACTER VARYING(50) NOT NULL, " \
                                "IMAGE_PATH CHARACTER VARYING(400), " \
                                "DATE_TODAY TIMESTAMP DEFAULT NOW())"
