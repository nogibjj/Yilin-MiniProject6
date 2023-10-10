import mysql.connector
from prettytable import PrettyTable
from query import complex_query  # Ensure query.py is in the same directory or in the PYTHONPATH

def create_database(conn, dbname):
    """Creates the database if it doesn't exist."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
        conn.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error creating database: {e}")
        raise

def connect_to_database(host, user, password, dbname):
    """Establishes a connection to a specific database."""
    try:
        return mysql.connector.connect(
            host=host, user=user, password=password, database=dbname)
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def print_complex_query():
    column_names, results = complex_query()

    # Using PrettyTable to format the output
    table = PrettyTable(column_names)
    for row in results:
        table.add_row(row)

    print("\nResults of the complex query:")
    print(table)

def main():
    # Database configuration
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Welcome1!",
        "dbname": "ecommerce_db"
    }

    # Connect to MySQL without specifying a database
    try:
        initial_conn = mysql.connector.connect(
            host=db_config["host"], user=db_config["user"], password=db_config["password"])

        # Ensure the database exists
        create_database(initial_conn, db_config["dbname"])
        initial_conn.close()

        # Connect to the specific database
        conn = connect_to_database(**db_config)
        cursor = conn.cursor()

        # Create tables and capture SQL output
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Existing tables:", tables)

        # Avoid creating tables if they already exist
        if not any('Customers' in table for table in tables):
            cursor.execute("CREATE TABLE Customers "
                           "(customer_id INT PRIMARY KEY, customer_name VARCHAR(255))")
        if not any('Products' in table for table in tables):
            cursor.execute("CREATE TABLE Products "
                           "(product_id INT PRIMARY KEY, product_name VARCHAR(255))")
        if not any('Orders' in table for table in tables):
            cursor.execute("""CREATE TABLE Orders (order_id INT PRIMARY KEY,
                             customer_id INT, product_id INT, 
                              order_date DATE, amount DECIMAL(10, 2), 
                              FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
                              FOREIGN KEY(product_id) REFERENCES Products(product_id))""")

        # Show tables after creation
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables after creation:", tables)

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")

    # Print the complex query results
    print_complex_query()

if __name__ == "__main__":
    main()
