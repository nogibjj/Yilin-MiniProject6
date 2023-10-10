import unittest
import mysql.connector
from main import create_database, connect_to_database, print_complex_query

class TestMainFunctions(unittest.TestCase):
    
    def setUp(self):
        # Database configuration for tests
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Welcome1!",
            "dbname": "ecommerce_db_test"  
            # Use a different DB name for testing purposes
        }

        # Establish a connection without specifying a database
        self.conn = mysql.connector.connect(host=self.db_config["host"], 
                                            user=self.db_config["user"], 
                                            password=self.db_config["password"])
        self.cursor = self.conn.cursor()

        # Ensure the test database exists before all tests
        create_database(self.conn, self.db_config["dbname"])

    def test_create_database(self):
        # Recreate the test database to verify the creation process
        self.cursor.execute(f"DROP DATABASE {self.db_config['dbname']}")
        create_database(self.conn, self.db_config["dbname"])
        
        # Check if the database is created
        self.cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in self.cursor.fetchall()]
        self.assertIn(self.db_config["dbname"], databases)

    def test_table_creation(self):
        conn = connect_to_database(**self.db_config)
        cursor = conn.cursor()

        # Drop the tables if they exist
        cursor.execute("DROP TABLE IF EXISTS Orders")
        cursor.execute("DROP TABLE IF EXISTS Customers")
        cursor.execute("DROP TABLE IF EXISTS Products")

        # Create tables
        cursor.execute("CREATE TABLE Customers (customer_id INT PRIMARY KEY, "
                       "customer_name VARCHAR(255))")
        cursor.execute("CREATE TABLE Products (product_id INT PRIMARY KEY, "
                       "product_name VARCHAR(255))")
        cursor.execute("""CREATE TABLE Orders (order_id INT PRIMARY KEY, 
                       customer_id INT, product_id INT, 
                    order_date DATE, amount DECIMAL(10, 2), 
                    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
                    FOREIGN KEY(product_id) REFERENCES Products(product_id))""")

        # Check if tables exist
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        self.assertIn('Customers', tables)
        self.assertIn('Products', tables)
        self.assertIn('Orders', tables)

        cursor.close()
        conn.close()


    def test_print_complex_query(self):
        # Just testing if the function runs without errors, actual data verification 
        # would require seeding the database with known data and then validating results
        try:
            print_complex_query()
            success = True
        except Exception as e:
            success = False
            print(f"Error during complex query: {e}")
        self.assertTrue(success)

    def tearDown(self):
        # Cleanup after tests
        self.cursor.execute(f"DROP DATABASE IF EXISTS {self.db_config['dbname']}")
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    unittest.main()
