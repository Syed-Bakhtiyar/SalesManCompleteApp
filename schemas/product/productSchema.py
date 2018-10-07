sqlCreateProductTable = "CREATE TABLE IF NOT EXISTS product " \
                                   "(ID INT NOT NULL AUTO_INCREMENT, " \
                                    "PRODUCT_SUB_TYPE_ID INT NOT NULL, " \
                                    "TITLE VARCHAR(40) DEFAULT '', " \
                                    "IMAGE_PATH VARCHAR(80) DEFAULT '',"\
                                    "ISAVAILABLEPRODUCT TINYINT(1) DEFAULT 0," \
                                    "PRIMARY KEY (ID)," \
                                    "FOREIGN KEY (PRODUCT_SUB_TYPE_ID) REFERENCES product_sub_type_table(ID)"\
                                    ")"
