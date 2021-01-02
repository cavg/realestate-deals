from flask import Flask, render_template
app = Flask(__name__)

from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'realestate'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


@app.route('/')
def hello():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT thumb, link from items")
    return render_template('index.html', results=cursor.fetchall())

if __name__ == '__main__':
    app.run()