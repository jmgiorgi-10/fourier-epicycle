// Basics of HTTP request methods: //

// HTTP = hyper-text transfer protocol - used to enable communications between client and servers. Client sends HTTP request to the server; server returns response to the client. 
// the response itself has status information relating to the request, as well as the requested content. 

	// GET: used for getting data from a specific source
	// POST: used to send data o server to create/update resource

// fetch('/test')
// 	.then(function response {
// 		return response.json()
// 	}).then(function (text) {
// 		console.log('GET response: ');
// 		console.log(text.greeting)
// 	})

setInterval(updateFunction, 3000);

function updateFunction() {
	alert("Heyy duude");
}