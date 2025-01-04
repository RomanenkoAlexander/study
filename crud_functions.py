import sqlite3
connection = sqlite3.connect('base_products.db')
cursor = connection.cursor()


def initiate_db(title, description, price):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')

    cursor.execute(' CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')
    cursor.execute(' CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
    check_product = cursor.execute('SELECT * FROM Products WHERE title =?', (title,))
    if check_product.fetchone() is None:
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))
    
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    get_products = cursor.fetchall()
    return get_products
    connection.commit()

def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username,email, age, 1000))
    connection.commit()

def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True
    connection.commit()
