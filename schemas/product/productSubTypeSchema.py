sqlCreateProductSubTypeTable = "CREATE TABLE IF NOT EXISTS product_sub_type_table(ID SERIAL PRIMARY KEY, " \
                                        "PRODUCT_TYPE_ID INTEGER NOT NULL, " \
                                        "TITLE CHARACTER VARYING(40) NOT NULL DEFAULT '')"
