from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'riverplate10'
app.config['MYSQL_DB'] = 'complex'

mysql = MySQL(app)

@app.route('/')
def index():
    try:
        # Attempting to create a cursor from the MySQL instance
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")  # Simple query to test connection
        return jsonify({"message": "Connection successful!"})
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
	app.run(debug=True)