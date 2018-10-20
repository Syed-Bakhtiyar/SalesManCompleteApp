sqlCreateProductSubTypeTable = "CREATE TABLE IF NOT EXISTS product_sub_type_table(ID INT NOT NULL AUTO_INCREMENT, " \
                                        "PRODUCT_TYPE_ID INT NOT NULL, " \
                                        "TITLE VARCHAR(40) NOT NULL DEFAULT ''," \
                                        "UNIQUE (PRODUCT_TYPE_ID, TITLE)," \
                                        "PRIMARY KEY (ID)," \
                                        "FOREIGN KEY (PRODUCT_TYPE_ID) REFERENCES product_type_table(ID)"\
                                        ")"
