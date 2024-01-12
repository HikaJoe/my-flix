
#multi-line comment
"""
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


"""


from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import yaml

app = Flask(__name__)

# Load database configuration from the YAML file
with open('loginconfig.yml', 'r') as yaml_file:
    db_config = yaml.safe_load(yaml_file)

# Establish the database connection
conn = mysql.connector.connect(**db_config)

# Define a cursor for executing SQL queries
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Get user input from the login form
    username = request.form['username']
    password = request.form['password']

    # Execute a query to fetch user details from the database
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        # Authentication successful
        return "Login successful"
    else:
        # Authentication failed
        return "Login failed"

if __name__ == '__main__':
    app.run(debug=True)

