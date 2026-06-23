import sqlite3

DB_NAME = 'budget.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT,
        transaction_type TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def add_transaction(category, amount, description, transaction_type):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions (category, amount, description, transaction_type)
    VALUES (?, ?, ?, ?)
    """, (category, amount, description, transaction_type))

    conn.commit()
    conn.close()

def get_transactions(category = None):
    conn = get_connection()
    cursor = conn.cursor()

    if category:
        cursor.execute('''
        SELECT * FROM transactions
        WHERE category = ?
        ''', (category,))
    else:
        cursor.execute('SELECT * FROM transactions')

    rows = cursor.fetchall()
    conn.close()

    return rows

def get_balance(category):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT SUM(amount)
    FROM transactions
    WHERE category = ?
    ''', (category,))

    result = cursor.fetchone()[0]
    conn.close()

    return result if result else 0