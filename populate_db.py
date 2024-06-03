import sqlite3

# connect to the database
connection = sqlite3.connect('app.db')

# create a cursor
cursor = connection.cursor()

# # populate the database
# cursor.execute("INSERT INTO stock (symbol, company) VALUES ('ADOBE', 'Adobe INC.')")
# cursor.execute("INSERT INTO stock (symbol, company) VALUES ('VZ', 'Verizon')")
# cursor.execute("INSERT INTO stock (symbol, company) VALUES ('Z', 'Zillow')")

# # delete the database
# cursor.execute("DELETE FROM stock")

# commit
connection.commit()