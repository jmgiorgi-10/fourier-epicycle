
The implementation of the curves is done with Bezier curves, and the circles are generated with the Discrete Fourier Transform (DFT).


To run the web app, we need to first setup the MySQL database, named 'complex', with a TABLE 'drawings2':

```sudo systemctl start mysql```
```mysql -u root -p```

Then once logged in, we can run:

```CREATE DATABASE complex;```
```USE complex;```

And create the appropriate table:

`CREATE TABLE DRAWINGS2 (
	id INT NOT NULL AUTO_INCREMENT,
	x_points INT DEFAULT NULL,
	y_points INT DEFAULT NULL,
	PRIMARY KEY (id)
);`

Next, from within the api folder, we can configure the Flask Environmental variable, and run the Flask application file.

```export FLASK_APP=app.py```

```python3 app.py```

With this application, you can create an arbitrary smooth curve, and have a bunch of rotating circles draw the exact curve. In order to access your favorite previously saved drawings, these are stored in a MySQL database.


