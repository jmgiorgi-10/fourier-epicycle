from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
from mysql.connector import Error
import logging

# Define database connection parameters
host = "127.0.0.1"  # e.g., "localhost" or "127.0.0.1"
user = "root"  # e.g., "root"
password = "riverplate10"
database = "complex"

# # Configure the Flask application
app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'riverplate10'
# app.config['MYSQL_DB'] = 'complex'

# # Create the MySQL Database
# mysql = MySQL(app)

logging.basicConfig(level=logging.DEBUG)

circles = [
{
	'id': 1,
	'position': 3
},
{
	'id': 2,
	'position': 4
}
]

def update_position(timestep):
	timestep += 0.1


@app.route('/test_connection')
def test_connection():
    try:
        # Attempting to create a cursor from the MySQL instance
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")  # Simple query to test connection
        return jsonify({"message": "Connection successful!"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/')
def index():
	return render_template('Index4.html') # index4 version of html file used.

@app.route('/circles', methods=['GET'])
def get_tasks():
	circle = {'greeting' : 'hey there'}
	response = jsonify(circles)
	#response.headers.add("Access-Control-Allow-Origin", "*")
	return response

# GET cubic Bezier points from the MySQL database
@app.route('/drawing', methods=['GET'])
def get_drawing():
	# Confirm if connection with MySQL database has been established.
	try:
		 # Establish connection
		connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
		if connection.is_connected():
			cur = connection.cursor()
			cur.execute('''SELECT x_points, y_points FROM DRAWINGS2 ORDER BY id DESC LIMIT 4''')	# Select the last four points added to database (Cubic Bezier)
			rv = cur.fetchall()
			# convert response to JSON before returning
			row_headers = [x[0] for x in cur.description]
			json_data = []
			for result in rv:
				json_data.append(dict(zip(row_headers, result)))
			print("hello from /drawing get route")
			response = jsonify(json_data)
			cur.close()
			return response

	except Error as e:
		print("Error while connecting to MySQL:", e)

	# Close the connection
	if 'connection' in locals() and connection.is_connected():
		connection.close()
		print("MySQL connection closed.")
    

	
# POST cubic Bezier points to the MySQL database
@app.route('/drawing', methods=['POST'])
def post_drawing():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            cur = connection.cursor()
            data = request.get_json()
            cur.execute('''INSERT INTO DRAWINGS2(x_points, y_points) VALUES (%s, %s)''', 
                        (data['x_points'], data['y_points']))
            connection.commit()
            cur.close()
            return jsonify({"message": "Success"})
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return jsonify({"error": str(e)})
    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")



if __name__ == "__main__":
	app.run(debug=True)
