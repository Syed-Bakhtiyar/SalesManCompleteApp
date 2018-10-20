sqlCreateCompanyTable = "CREATE TABLE IF NOT EXISTS company (" \
                                     "ID INT NOT NULL AUTO_INCREMENT," \
                                     "ADMIN_ID INT NOT NULL," \
                                     "NAME VARCHAR(255) NOT NULL, " \
                                    #  "UNIQUE (ADMIN_ID, NAME),"\
                                     "DATE_TODAY TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
                                     "PRIMARY KEY (ID), "\
                                     "FOREIGN KEY (ADMIN_ID) REFERENCES user(ID))"
