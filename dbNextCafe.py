#!/usr/bin/python
import sqlite3

class db():
        # create NextCafe database
        conn = sqlite3.connect('NestCafe.db')
        cur = conn.cursor()
        print("Database created successfully");

        # create Coffee table
        cur.execute('''CREATE TABLE Coffee (
               COFFEE_ID                INTEGER         PRIMARY KEY,
               TYPE                     TEXT                                NOT NULL,
               PRICE                    INTEGER                             NOT NULL,
               COUNTRY                  TEXT,
               FLAVOUR_CONTAIN          TEXT,
               MATERIALS_PACKETS        INTEGER);''')
        print("Coffee Table created successfully");

        # create first row
        cur.execute("INSERT INTO Coffee (COFFEE_ID,TYPE,PRICE,COUNTRY,FLAVOUR_CONTAIN,MATERIALS_PACKETS) \
              VALUES (1, 'Cappuccino', 300, 'Italy', 'Milk Foam', 1)");
        # create second row
        cur.execute("INSERT INTO Coffee (COFFEE_ID,TYPE,PRICE,COUNTRY,FLAVOUR_CONTAIN,MATERIALS_PACKETS) \
              VALUES (2, 'Mocha', 250, 'China', 'Chocolate syrup', 1)");
        # create third row
        cur.execute("INSERT INTO Coffee (COFFEE_ID,TYPE,PRICE,COUNTRY,FLAVOUR_CONTAIN,MATERIALS_PACKETS) \
              VALUES (3, 'Affogato', 200, 'South Africa', 'Water', 2)");
        # create fourth row
        cur.execute("INSERT INTO Coffee (COFFEE_ID,TYPE,PRICE,COUNTRY,FLAVOUR_CONTAIN,MATERIALS_PACKETS) \
                      VALUES (4, 'Espresso', 400, 'Canada', 'Milk', 3)");
        # create fifth row
        cur.execute("INSERT INTO Coffee (COFFEE_ID,TYPE,PRICE,COUNTRY,FLAVOUR_CONTAIN,MATERIALS_PACKETS) \
                      VALUES (5, 'Latte', 450, 'Australia', 'Ice cream with caramel', 1)");
        conn.commit()
        print ("Records created successfully");


        # create Sales table
        cur.execute('''CREATE TABLE Sales (
                SALES_ID            INTEGER        PRIMARY KEY      NOT NULL,
                COFFEE_ID           INTEGER                         NOT NULL,
                TYPE                TEXT                            NOT NULL,
                PRICE               INTEGER,
                MATERIALS_PACKETS   INTEGER);''')
        print("Sales Table created successfully");

        # create first row
        cur.execute("INSERT INTO Sales (SALES_ID,COFFEE_ID,TYPE,PRICE,MATERIALS_PACKETS) \
                VALUES (1, 1, 'Cappuccino', 300, 1)");

        # create second row
        cur.execute("INSERT INTO Sales (SALES_ID,COFFEE_ID,TYPE,PRICE,MATERIALS_PACKETS) \
                VALUES (null, 3, 'Affogato', 200, 2)");

        # create third row
        cur.execute("INSERT INTO Sales (SALES_ID,COFFEE_ID,TYPE,PRICE,MATERIALS_PACKETS) \
                VALUES (null, 5, 'Latte', 450, 1)");
        conn.commit()
        print("Records created successfully");


        # close database connection
        conn.close()
        print("Database closed successfully");
