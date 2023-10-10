import unittest
import sqlite3
from main import initialize_database
from query import execute_query

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Create an in-memory database for testing
        self.conn = initialize_database()

    def tearDown(self):
        # Close the database connection after each test
        self.conn.close()

    def test_database_population(self):
        """Test if tables are populated correctly."""
        cursor = self.conn.cursor()

        # Check the number of rows in each table
        cursor.execute("SELECT COUNT(*) FROM Customers")
        self.assertEqual(cursor.fetchone()[0], 6)

        cursor.execute("SELECT COUNT(*) FROM Orders")
        self.assertEqual(cursor.fetchone()[0], 9)

        cursor.execute("SELECT COUNT(*) FROM Products")
        self.assertEqual(cursor.fetchone()[0], 3)

    def test_query_results(self):
        """Test if the complex query returns expected results."""
        cursor = self.conn.cursor()

        # Execute the main query
        results = list(execute_query(self.conn))
        
        # Here, you should specify the expected results based on the sample data
        expected_results = [
            # Replace with expected tuples from the result of the complex query
            # Example: ('Alice', 250, 'Laptop')
        ]

        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()
