import sqlite3


# database driver
try:
    db = sqlite3.connect('register.db')
    print("Database created successfully")
    db.execute('''CREATE TABLE REGISTER
             (ID INT PRIMARY KEY     NOT NULL,
             NAME TEXT NOT NULL,
             DATE TEXT NOT NULL,
             TIMESTAMP TIME NOT NULL);''')

    print("Table created successfully")
except sqlite3.Error as er:
    print(f'Sqlite3 encountered an error, {er}')