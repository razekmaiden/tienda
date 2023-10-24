from flask_mysqldb import MySQL
from flask import Flask, request
app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tienda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db = MySQL(app)
#cur = mysql.connection.cursor()



@app.route('/')
def hello():
    try:
        cursor = db.connection.cursor()
        sql = """SELECT LIB.isbn, LIB.titulo, LIB.anoedicion, LIB.precio,
            AUT.apellidos, AUT.nombres
            FROM libro LIB JOIN autor AUT ON LIB.autor_id = AUT.id
            ORDER BY LIB.titulo ASC"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        return data
    except Exception as ex:
        raise Exception(ex)

if __name__=='__main__':
    app.run(debug=True)