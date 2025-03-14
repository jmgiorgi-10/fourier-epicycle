from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'riverplate10',
    'database': 'complex'
}

@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        return jsonify({"message": "Connection successful!"})
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)