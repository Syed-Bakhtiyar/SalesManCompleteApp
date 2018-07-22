sqlCreateMerchandiserTable = "CREATE TABLE IF NOT EXISTS merchandiser (ID SERIAL PRIMARY KEY," \
                                    "AREA_MANAGER_ID INTEGER NOT NULL," \
                                    "SHOP_ID INTEGER DEFAULT 0," \
                                    "NAME CHARACTER VARYING(50) NOT NULL," \
                                    "EMAIL CHARACTER VARYING(50) NOT NULL UNIQUE," \
                                    "PASSWORD CHARACTER VARYING(50) NOT NULL," \
                                    "COMPANYNAME CHARACTER VARYING(50) NOT NULL UNIQUE," \
                                    "ISONLINE BOOLEAN DEFAULT FALSE," \
                                    "DATETODAY TIMESTAMP DEFAULT NOW())"
