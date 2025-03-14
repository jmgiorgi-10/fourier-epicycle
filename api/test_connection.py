import mysql.connector
from mysql.connector import Error

# Define database connection parameters
host = "127.0.0.1"  # e.g., "localhost" or "127.0.0.1"
user = "root"  # e.g., "root"
password = "riverplate10"
database = "complex"

try:
    # Establish connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    if connection.is_connected():
        print("Successfully connected to MySQL")
        db_info = connection.get_server_info()
        print("MySQL Server version:", db_info)

        # Get a cursor
        cur = connection.cursor()
        print("Got a cursor without errror")

        # # Execute a query
        cur.execute("SELECT * FROM drawings2")
        rows = cur.fetchall()  # Fetch all results before executing another query
        print(rows)

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")