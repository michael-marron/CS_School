# CS_School
In the command line, type the following commands:

python3 -m venv ./env
source env/bin/activate
$env:FLASK_APP = "run.py"
pip install flask
pip install flask_sqlalchemy
pip install flask_mail
pip install flask_wtf
pip install psycopg2
pip install flask_admin
python run.py

To make a local copy of the database:
Add your IP address to the access control on Render
Add external connection using DATABASE_URI link into your IDE of choice (we used pg-admin4)
Paste the PSQL code (written in psql.txt) into a blank query under your Database >> Schemas >> Public >> Tables >> (right click) Query Tool

To run, type into command line:
flask run




# Testing
pip install pytest
pytest --version
To run: pytest

packages:
pip install flask-session
