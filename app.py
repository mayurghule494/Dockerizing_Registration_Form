import os
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_host = os.environ.get('DB_HOST', 'db')
db_port = int(os.environ.get('DB_PORT', 3306))
db_name = os.environ.get('DB_NAME', 'registration_db')
db_user = os.environ.get('DB_USER', 'admin')
db_password = os.environ.get('DB_PASSWORD', 'admin')
# Establish database connection
db = mysql.connector.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Create the users table if it doesn't exist
cursor = db.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)
cursor.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']

    cursor = db.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()

    return 'Registered successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
