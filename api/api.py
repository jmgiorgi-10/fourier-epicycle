# // Chaining:
# 	// a common necessity is to executre one or more asynchronous operations back-to-back, so that each subsequent operation starts once the last operation suceeds
# 	// using results from the last step. This can be established with a promise chain.

# //const promise = doSomething();
# //const promise2 = promise.then(successCallback, failureCallback);

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
	jsonResp = {'jack': 4098, 'sape': 4139}
	print(jsonify(jsonResp))
	return jsonify(jsonResp)

if __name__ == '__main__':
	app.run()