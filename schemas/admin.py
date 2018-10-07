sqlCreateAdminTable = "CREATE TABLE IF NOT EXISTS admin (" \
                                     "ID serial primary key," \
                                     "NAME character varying(255) NOT NULL, " \
                                     "EMAIL character varying(255) NOT NULL UNIQUE," \
                                     "PASSWORD character varying(255) NOT NULL," \
                                     "ISONLINE BOOLEAN DEFAULT FALSE)"
