import sqlite3

# database driver for register db
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

# userdata db
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    password text
                )
            ''')
con.commit()

con = sqlite3.connect('userdata.db')
cur = con.cursor()
name, email, contact, gender, country, password = "Rodney", "rodney@gmail.com", "0717405766", "male", "kenya", "12345"
cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
    'name': name,
    'email': email,
    'contact': contact,
    'gender': gender,
    'country': country,
    'password': password

})
con.commit()