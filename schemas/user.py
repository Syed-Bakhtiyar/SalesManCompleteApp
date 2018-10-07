# admin id means if role is manager means which admin have this manager
# manager id means if role is area manager which manager he assigned
# 
sqlCreateUser = "CREATE TABLE IF NOT EXISTS user (" \
                                     "ID int NOT NULL AUTO_INCREMENT," \
                                     "ADMIN_ID int DEFAULT NULL," \
                                     "MANAGER_ID int DEFAULT NULL," \
                                     "AREA_MANAGER_ID int DEFAULT NULL," \
                                     "FIRST_NAME VARCHAR(255) NOT NULL, " \
                                     "LAST_NAME VARCHAR(255) NOT NULL, " \
                                     "EMAIL VARCHAR(255) NOT NULL UNIQUE," \
                                     "PASSWORD VARCHAR(255) NOT NULL," \
                                     "ISONLINE TINYINT(1) DEFAULT 0," \
                                     "ROLE enum('ADMIN','MANAGER', 'AREAMANAGER', 'MERCHANDISER') default NULL," \
                                     "PRIMARY KEY (ID)," \
                                     "FOREIGN KEY (ADMIN_ID) REFERENCES user(ID),"\
                                     "FOREIGN KEY (MANAGER_ID) REFERENCES user(ID)," \
                                     "FOREIGN KEY (AREA_MANAGER_ID) REFERENCES user(ID),)"
