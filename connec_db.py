import sqlite3

def create_db():
    conn = sqlite3.connect('bank_system.db')
    c = conn.cursor()

        # Create the users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    
    # Create the accounts table
    c.execute('''CREATE TABLE IF NOT EXISTS accounts (
                    user_id INTEGER,
                    balance REAL NOT NULL DEFAULT 0.0,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')

    # Create the transactions table
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    type TEXT,
                    amount REAL,
                    date TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()
create_db()