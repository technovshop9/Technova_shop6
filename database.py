import sqlite3

conn = sqlite3.connect('technova_store.db')  # This creates the DB file
cursor = conn.cursor()

# Admin table
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Default admin
cursor.execute('''
INSERT OR IGNORE INTO admin (username, password)
VALUES (?, ?)
''', ('admin', 'X+Ud$jpm%CpQ#mJ4'))

# Products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category TEXT,
    image TEXT
)
''')

# Cart table
cursor.execute('''
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id)
)
''')

conn.commit()
conn.close()

print("✅ Database setup complete.")
