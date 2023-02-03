#from:https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
import os
import psycopg2

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#from medium.com tutorial:
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='UserData',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/db/')
def index2():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Student";')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('db.html', books=books)

if __name__ == "__main__":
    app.run(debug=True)


