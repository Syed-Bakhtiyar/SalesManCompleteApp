sqlCreateManagerTable = "CREATE TABLE IF NOT EXISTS manager (" \
                                     "ID serial primary key," \
                                     "ADMIN_ID INTEGER NOT NULL,"\
                                     "NAME character varying(255) NOT NULL, " \
                                     "EMAIL character varying(255) NOT NULL UNIQUE," \
                                     "PASSWORD character varying(255) NOT NULL," \
                                     "COMPANYID INTEGER DEFAULT NULL," \
                                     "ISONLINE BOOLEAN DEFAULT FALSE)"
