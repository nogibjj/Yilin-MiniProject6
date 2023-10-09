import pandas as pd

def load_data(cursor, conn):
    # Read CSV files
    customers = pd.read_csv("customers.csv")
    products = pd.read_csv("products.csv")
    orders = pd.read_csv("orders.csv")
    
    # Load into MySQL
    for index, row in customers.iterrows():
        cursor.execute("INSERT INTO Customers (customer_id, customer_name) VALUES (%s, %s)", 
                       (row['customer_id'], row['customer_name']))
    for index, row in products.iterrows():
        cursor.execute("INSERT INTO Products (product_id, product_name) VALUES (%s, %s)", 
                       (row['product_id'], row['product_name']))
    for index, row in orders.iterrows():
        cursor.execute("INSERT INTO Orders (order_id, customer_id, product_id, order_date, amount) VALUES (%s, %s, %s, %s, %s)", 
                       (row['order_id'], row['customer_id'], row['product_id'], row['order_date'], row['amount']))
    
    conn.commit()

def get_top_customers(cursor):
    query = """
    -- The complex SQL query goes here as described above --
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result
