sqlCreateProductTypeTable = "CREATE TABLE IF NOT EXISTS product_type_table(ID INT NOT NULL AUTO_INCREMENT, " \
                                        "COMPANY_ID INT NOT NULL," \
                                        "TITLE VARCHAR(40) NOT NULL," \
                                        "UNIQUE (COMPANY_ID, TITLE),"\
                                        "PRIMARY KEY (ID)," \
                                        "FOREIGN KEY (COMPANY_ID) REFERENCES company(ID)"\
                                        ")";
