Important: in order to run the Flask application file, either fun it with "flask app.py", or first set the Environmental Variable FLASK_APP to app.py, with "export FLASK_APP=app.py", prior to running "python3 app.py".

`export FLASK_APP=app.py`

With this application, you can create an arbitrary smooth curve, and have a bunch of rotating circles draw the exact curve. In order to access your favorite previously saved drawings, these are stored in a MySQL database.

The implementation of the curves is done with Bezier curves, and the circles are generated with an Inverse Fourier Transform (IFT).
