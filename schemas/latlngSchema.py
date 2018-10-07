sqlCreateLatLongTable = "CREATE TABLE IF NOT EXISTS location(ID INT NOT NULL AUTO_INCREMENT, " \
                                "USER_ID INT DEFAULT NULL, " \
                                "LATITUDE VARCHAR(80) NOT NULL, " \
                                "LONGITUDE VARCHAR(80) NOT NULL,"\
                                "PRIMARY KEY (ID),"\
                                "FOREIGN KEY (USER_ID) REFERENCES user(ID)"\
                                ")"
