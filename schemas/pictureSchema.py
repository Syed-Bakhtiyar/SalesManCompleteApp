sqlCreatePicturesTable = "CREATE TABLE IF NOT EXISTS pictures (ID INT NOT NULL AUTO_INCREMENT, " \
                                "SHOP_ID INT NOT NULL, " \
                                "COMMENTS VARCHAR(250) DEFAULT NULL, " \
                                "IMAGE_PATH VARCHAR(400), " \
                                "DATE_TODAY TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " \
                                "PRIMARY KEY (ID),"\
                                "FOREIGN KEY (SHOP_ID) REFERENCES shop(ID))"
