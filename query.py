import mysql.connector

def complex_query():
    conn = mysql.connector.connect(host='localhost', user='root', password='Welcome1!', database='ecommerce_db')
    cursor = conn.cursor()

    # Read the query from the .sql file
    with open('query.sql', 'r') as f:
        query = f.read()

    cursor.execute(query)
    result = cursor.fetchall()
    
    # Fetch column names
    column_names = [description[0] for description in cursor.description]

    cursor.close()
    conn.close()
    return column_names, result

if __name__ == '__main__':
    columns, results = complex_query()
    print(columns)
    for row in results:
        print(row)
