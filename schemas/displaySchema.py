sqlCreateDisplayTable = "CREATE TABLE IF NOT EXISTS display(ID INT NOT NULL AUTO_INCREMENT," \
                                "SHOP_ID INT NOT NULL, " \
                                "PRODUCT_ID INT NOT NULL," \
                                "COMMENTS VARCHAR(255) NOT NULL UNIQUE, " \
                                "IMAGE_PATH VARCHAR(400) DEFAULT '', " \
                                "DATE_TODAY TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
                                "PRIMARY KEY (ID)," \
                                "FOREIGN KEY (SHOP_ID) REFERENCES shop(ID), " \
                                "FOREIGN KEY (PRODUCT_ID) REFERENCES product(ID))"
