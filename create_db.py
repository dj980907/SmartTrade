import sqlite3, config

# connect to the database
connection = sqlite3.connect(config.DB_FILE)

# create a cursor
cursor = connection.cursor()

# create stock table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        exchange TEXT NOT NULL
    )
""")

# create stock price table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

# commit
connection.commit()