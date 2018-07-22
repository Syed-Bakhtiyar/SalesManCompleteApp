sqlCreateShopTable = "CREATE TABLE IF NOT EXISTS shop(ID SERIAL PRIMARY KEY," \
                            "MANAGER_ID INTEGER DEFAULT 0," \
                            "MERCH_ID INTEGER DEFAULT 0," \
                            "SHOP_NAME CHARACTER VARYING(255) NOT NULL DEFAULT '', " \
                            "IS_ACTIVE BOOLEAN DEFAULT FALSE)"
