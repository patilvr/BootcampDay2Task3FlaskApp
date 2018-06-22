from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify



app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'bootcamp'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bootcamp'
app.config['MYSQL_DATABASE_DB'] = 'employees'
app.config['MYSQL_DATABASE_HOST'] = '192.168.21.57'
mysql.init_app(app)

@app.route('/')
def someName():
    db = mysql.connect()
    cursor = db.cursor()
    sql = "SELECT * FROM employees limit 10"
    cursor.execute(sql)
    #results = cursor.fetchall()
    return jsonify(cursor.fetchall())

# if __name__ == '__main__':
# app.run(debug=True)
