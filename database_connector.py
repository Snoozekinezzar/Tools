#!/usr/bin/env python3
import pyodbc

# Common database drivers help function
def list_common_drivers():
    print("Here are some common drivers you might use:")
    print("For SQL Server: '{ODBC Driver 17 for SQL Server}'")
    print("For MySQL: '{MySQL ODBC 8.0 Driver}'")
    print("For Oracle: '{Oracle in OraClient}'")
    print("For PostgreSQL: '{PostgreSQL Unicode}'")
    print("You can use 'odbcinst -q -d' to list all available drivers on your system.")

# Function to create database connection
def create_connection(server, database, username, password, driver):
    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    try:
        conn = pyodbc.connect(conn_str, timeout=10)
        return conn
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

# Function to execute a query and print results
def execute_query(cursor, query):
    try:
        cursor.execute(query)
        if cursor.description is not None:  # If there is something to fetch
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            return columns, rows
        else:  # If it is an update/insert/delete query
            return None, None
    except Exception as e:
        print(f"An error occurred while executing the query: {e}")
        return None, None

# Interactive shell for database exploration
def explore_database():
    server = input("Enter server name: ")
    database = input("Enter database name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Enter driver (type 'help' to list common drivers):")
    driver = input("Enter driver: ")
    
    if driver.lower() == 'help':
        list_common_drivers()
        driver = input("Enter driver: ")

    conn = create_connection(server, database, username, password, driver)
    if conn is not None:
        cursor = conn.cursor()
        print("Connected to the database. Type 'exit' to quit.")
        while True:
            query = input("Enter SQL command: ")
            if query.lower() == 'exit':
                break
            elif query.lower() == 'help':
                list_common_drivers()
                continue
            columns, rows = execute_query(cursor, query)
            if columns is not None and rows is not None:
                print(columns)
                for row in rows:
                    print(row)
        cursor.close()
        conn.close()
    else:
        print("Failed to create database connection.")

# Run the interactive database exploration
if __name__ == "__main__":
    explore_database()
