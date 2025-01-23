import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gwl"
    )
# Test Connection
try:
    conn = get_db_connection()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)