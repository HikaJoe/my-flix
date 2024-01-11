import mysql.connector
import yaml

# Load database configuration from the YAML file
with open('loginconfig.yml', 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

try:
    # Establish the database connection
    conn = mysql.connector.connect(**config)

    # Print a message indicating successful connection
    print("Connected to the database!")

except mysql.connector.Error as e:
    # Print an error message if connection fails
    print(f"Error: {e}")

finally:
    # Close the connection in the finally block to ensure it's always closed
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")
