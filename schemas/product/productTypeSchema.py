sqlCreateProductTypeTable = "CREATE TABLE IF NOT EXISTS product_type_table(ID SERIAL PRIMARY KEY, " \
                                        "MANAGER_ID INTEGER NOT NULL," \
                                        "TITLE CHARACTER VARYING(40) NOT NULL DEFAULT '')";
