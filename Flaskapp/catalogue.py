from flask import Flask, render_template, send_from_directory
import mysql.connector
import yaml

app = Flask(__name__)

# Load database configuration from the YAML file
with open('catalogueconfig.yml', 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

# Establish the database connection
conn = mysql.connector.connect(**config)

@app.route('/')
def render_frontend():
    try:
        # Create a cursor to interact with the database
        cursor = conn.cursor(dictionary=True)

        # Fetch video data from the 'videos' table
        cursor.execute("SELECT * FROM videos")
        videos = cursor.fetchall()

        return render_template('index2.html', videos=videos)

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return "Error fetching data from the database."

    finally:
        # Close the cursor and connection in the finally block to ensure they're always closed
        if 'cursor' in locals():
            try:
                if cursor.is_open:
                    cursor.close()
            except AttributeError:
                pass

@app.route('/videos/<path:title>')
def serve_video(title):
    # Serve videos from the specified directory
    return send_from_directory('/home/ec2-user/my-flix/mp4', title)

if __name__ == '__main__':
    app.run(debug=True)