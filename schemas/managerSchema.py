sqlCreateManagerTable = "CREATE TABLE IF NOT EXISTS manager (" \
                                     "ID serial primary key," \
                                     "NAME character varying(255) NOT NULL, " \
                                     "EMAIL character varying(255) NOT NULL UNIQUE," \
                                     "PASSWORD character varying(255) NOT NULL," \
                                     "COMPANYNAME CHARACTER VARYING(50) NOT NULL UNIQUE," \
                                     "ISONLINE BOOLEAN DEFAULT FALSE)"
