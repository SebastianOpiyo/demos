import sqlite3

# database driver
db = sqlite3.connect('register.db')
try:
    db_cursor = db.cursor()
    print("Database created successfully")
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS REGISTER
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAME TEXT NOT NULL,
             DATE TEXT NOT NULL,
             TIMESTAMP TIME NOT NULL);''')

    db_cursor.close()
    print("Table created successfully")
except sqlite3.Error as er:
    print(f'Sqlite3 encountered an error, {er}')
    pass
