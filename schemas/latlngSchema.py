sqlCreateLatLongTable = "CREATE TABLE IF NOT EXISTS merch_location(ID SERIAL PRIMARY KEY, " \
                                "MERCH_ID INTEGER DEFAULT 0, " \
                                "LATITUDE CHARACTER VARYING(80) NOT NULL, " \
                                "LONGITUDE CHARACTER VARYING(80) NOT NULL)"
