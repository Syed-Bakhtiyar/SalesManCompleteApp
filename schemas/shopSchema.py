sqlCreateShopTable = "CREATE TABLE IF NOT EXISTS shop (" \
                        "ID int NOT NULL AUTO_INCREMENT," \
                        "COMPANY_ID INT DEFAULT NULL," \
                        "MANAGER_ID INT DEFAULT NULL," \
                        "AREA_MANAGER_ID INT DEFAULT NULL," \
                        "MERCH_ID INT DEFAULT NULL," \
                        "LOCATION_ID INT DEFAULT NULL," \
                        "SHOP_NAME VARCHAR(255) NOT NULL DEFAULT ''," \
                        "IS_ACTIVE TINYINT(1) DEFAULT 0,"\
                        "PRIMARY KEY (ID),"\
                        "FOREIGN KEY (COMPANY_ID) REFERENCES company(ID),"\
                        "FOREIGN KEY (MANAGER_ID) REFERENCES user(ID),"\
                        "FOREIGN KEY (AREA_MANAGER_ID) REFERENCES user(ID),"\
                        "FOREIGN KEY (MERCH_ID) REFERENCES user(ID),"\
                        "FOREIGN KEY (MERCH_ID) REFERENCES user(ID),"\
                        ")"
