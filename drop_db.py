import sqlite3, config

# connect to the database
connection = sqlite3.connect(config.DB_FILE)

# create a cursor
cursor = connection.cursor()

# drop stock_price table
cursor.execute("""
    DROP TABLE stock_price 
""")

# drop stock table
cursor.execute("""
    DROP TABLE stock 
""")


# commit
connection.commit()