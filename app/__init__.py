from flask import Flask, render_template, request, url_for, redirect
#from flask_mysqldb import MySQL
from peewee import MySQLDatabase, Model, CharField, IntegerField, FloatField
from flask_wtf.csrf import CSRFProtect

from config import config


from .models.ModeloLibro import ModeloLibro

app = Flask(__name__)



csrf = CSRFProtect()
db = MySQLDatabase(**config['development'].DB_CREDENTIALS)

# Define a model representing a table in the database

#print(db)
#print(db.connection)
#print(db.connection.cursor())
# Le paso la aplicacion como argumento. Esta instancia sirve para realizar conexiones a travez de los modelos
# Los modelos definen las acciones que vamos a hacer sobre las tablas.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) # Aca se indican los metodos permitidos, por defecto solo es GET
def login():
    # print(request.method)
    # print(request.form['usuario'])
    # print(request.form['password'])
    # NOTE: COn el metodos POST los datos del formaulario van en la URL, lo que no es seguro
    if request.method == 'POST': # Si el metodo es post, entonces los datoss estan presentes y los puedo imprimir
        # print(request.form['usuario'])
        # print(request.form['password'])
        if request.form['usuario'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/libros')
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        print(ex)


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404 # El segundo es el codigo de error

def inicializar_app(config): # Aca se ingresa como argumento la configuracion definida en config.py
    app.config.from_object(config)
    csrf.init_app(app)
    #print(app.config)
    app.register_error_handler(404, pagina_no_encontrada) # El manejador de errores permite redirigir a la vista correcta cuando hay un error 404 en este caso. 
    return app
