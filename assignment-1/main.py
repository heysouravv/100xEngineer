import mysql.connector

def connect_to_rds_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL RDS instance. MySQL server version: {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to the database: {record}")
        return connection
    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Example usage:
host = "supplytrack-test.czz86ijqyvos.us-east-1.rds.amazonaws.com"
user = "admin"
password = "SupplyT123$"
database = "SupplyTrack-Test"

connection = connect_to_rds_mysql(host, user, password, database)

# Don't forget to close the connection when you're done
if connection and connection.is_connected():
    connection.close()
    print("MySQL connection closed.")
