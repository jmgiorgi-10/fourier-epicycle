from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import logging

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'riverplate10'
app.config['MYSQL_DB'] = 'complex'
mysql = MySQL(app)

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

@app.route('/')
def index():
	return render_template('Index4.html')

@app.route('/circles', methods=['GET'])
def get_tasks():
	circle = {'greeting' : 'hey there'}
	response = jsonify(circles)
	#response.headers.add("Access-Control-Allow-Origin", "*")
	return response

# GET cubic Bezier points from the MySQL database
@app.route('/drawing', methods=['GET'])
def get_drawing():
	cursor = mysql.connection.cursor()
	cursor.execute('''SELECT x_points, y_points FROM DRAWINGS2 ORDER BY id DESC LIMIT 4''')	# Select the last four points added to database (Cubic Bezier)
	rv = cursor.fetchall()
	# convert response to JSON before returning
	row_headers = [x[0] for x in cursor.description]
	json_data = []
	for result in rv:
		json_data.append(dict(zip(row_headers, result)))
	print("hello from /drawing get route")
	response = jsonify(json_data)
	cursor.close()
	return response
# POST cubic Bezier points to the MySQL database 
@app.route('/drawing', methods=['POST'])
def post_drawing():
	app.logger.info(request.data)
	cursor = mysql.connection.cursor()
	data = request.get_json()
	cursor.execute('''INSERT INTO DRAWINGS2(x_points, y_points) VALUES (%s, %s)''', (data['x_points'], data['y_points']))
	mysql.connection.commit()
	cursor.close()
	return 'sucess'

if __name__ == "__main__":
	app.run(debug=True)
