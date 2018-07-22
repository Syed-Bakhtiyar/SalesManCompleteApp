sqlCreateAreaManagerTable = "CREATE TABLE IF NOT EXISTS area_manager(ID serial primary key," \
                                    "MANAGER_ID INTEGER NOT NULL," \
                                    "NAME CHARACTER VARYING(50) NOT NULL," \
                                    "PASSWORD CHARACTER VARYING(50) NOT NULL," \
                                    "DATE_TODAY TIMESTAMP DEFAULT NOW()," \
                                    "LOCATION_ID INTEGER DEFAULT 0)"

