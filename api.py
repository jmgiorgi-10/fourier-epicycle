from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.run(debug=True)

@app.route('/test', methods=['GET', 'POST'])
def testfn():

	#GET request
	if request.method == 'GET':
		message = {'hey man'}
		return jsonify(message)

	if (request.method == 'POST'):
		print(request.get_json())
		return'Successs', 200