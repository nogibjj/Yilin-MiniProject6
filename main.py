import sqlite3
import csv

def initialize_database():
    """Create and populate SQLite database with data from CSV files."""
    # Connect to SQLite database (in memory for demonstration purposes)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE Customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE Orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            order_date DATE,
            amount REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE Products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT
        )
    """)

    # Insert CSV data into tables
    with open('data/customers.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        cursor.executemany('INSERT INTO Customers VALUES (?, ?)', reader)
    
    with open('data/orders.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        cursor.executemany('INSERT INTO Orders VALUES (?, ?, ?, ?, ?)', reader)

    with open('data/products.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        cursor.executemany('INSERT INTO Products VALUES (?, ?)', reader)

    conn.commit()

    return conn

if __name__ == "__main__":
    conn = initialize_database()
    from mylib.query import execute_query
    execute_query(conn)
