sqlCreateOurTable = "CREATE TABLE IF NOT EXISTS activities(ID INT NOT NULL AUTO_INCREMENT," \
                                "SHOP_ID INT NOT NULL," \
                                "PRODUCT_ID INT NOT NULL," \
                                "COMMENTS VARCHAR(255) NOT NULL UNIQUE," \
                                "IMAGE_PATH VARCHAR(400) DEFAULT ''," \
                                "DATE_TODAY TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
                                "ACTIVITY_TYPE enum('OUR','COMPETITOR') default NULL," \
                                "PRIMARY KEY (ID)," \
                                "FOREIGN KEY (SHOP_ID) REFERENCES shop(ID)," \
                                "FOREIGN KEY (PRODUCT_ID) REFERENCES product(ID))"
