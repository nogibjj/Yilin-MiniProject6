import mysql.connector
from mylib.query import load_data, get_top_customers

def main():
    # Connect to MySQL
    db_config = {
        "host": "localhost",
        "user": "your_username",
        "password": "your_password",
        "database": "your_database"
    }
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Load CSV data into MySQL
    load_data(cursor, conn)

    # Get the desired output
    result = get_top_customers(cursor)
    
    for row in result:
        print(row)

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
