import traceback
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
#from flask_mysqldb import MySQL
from peewee import MySQLDatabase, Model, CharField, IntegerField, FloatField
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail

from config import config

from .models.ModeloCompra import ModeloCompra
from .models.ModeloLibro import ModeloLibro
from .models.ModeloUsuario import ModeloUsuario

from .models.entities.Usuario import Usuario
from .models.entities.Libro import Libro
from .models.entities.Compra import Compra

from .const import *
from .emails import confirmacion_compra

app = Flask(__name__)



csrf = CSRFProtect()
db = MySQLDatabase(**config['development'].DB_CREDENTIALS)
login_manager_app = LoginManager(app) # administracion de login
mail = Mail()
# Define a model representing a table in the database

#print(db)
#print(db.connection)
#print(db.connection.cursor())
# Le paso la aplicacion como argumento. Esta instancia sirve para realizar conexiones a travez de los modelos
# Los modelos definen las acciones que vamos a hacer sobre las tablas.

#Permite obtener todos los datos del usuario a partir del id del mismo
@login_manager_app.user_loader
def load_user(id_user):
    return ModeloUsuario.obtener_por_id(db, id_user)



@app.route('/password/<password>')
def generar_password(password):
    pass
    

@app.route('/login', methods=['GET', 'POST']) # Aca se indican los metodos permitidos, por defecto solo es GET
def login():
    # NOTE: Con el metodos POST los datos del formaulario van en la URL, lo que no es seguro
    if request.method == 'POST': # Si el metodo es post, entonces los datoss estan presentes y los puedo imprimir
        usuario = Usuario(id_usuario=None, usuario=request.form['usuario'], password=request.form['password'], tipousuario=None)
        usuario_logueado = ModeloUsuario.login(db, usuario)
        if usuario_logueado != None:
            login_user(usuario_logueado) # Usuario que inicio sesion y esta logueado correctamente -> la sesion actual
            flash(LOGIN_EXITOSO, category='success') # Mensaje flash
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALES_INVALIDAS, category='warning') # Mensaje flash
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, category='success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipousuario.id == 1: # usuario admin
            libros_vendidos = ModeloLibro.listar_libros_vendidos(db)
            data = {
                'titulo': 'Libros Vendidos',
                'libros_vendidos': libros_vendidos
            }
        else:
            compras = ModeloCompra.listar_compras_usuario(db, current_user)
            data = {
                'titulo': 'Mis Compras',
                'compras': compras
            }
        return render_template('index.html', data=data)
    else:
        return redirect(url_for('login'))

@app.route('/libros')
@login_required
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'titulo': 'Listado de libros',
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        traceback.print_exc()
        return render_template('errores/error.html', mensaje=format(ex))

@app.route('/comprarLibro', methods=['POST'])
@login_required
def comprar_libro():
    data_request = request.get_json() #recupero el json envisdo como parte de la peticion
    data = {}
    try:
        #libro = Libro(data_request["isbn"], None, None, None, None)
        libro = ModeloLibro.leer_libro(db, data_request['isbn'])
        compra = Compra(None, libro, current_user)
        data['exito']= ModeloCompra.registrar_compra(db, compra)
        confirmacion_compra(app, mail, current_user, libro)
    except Exception as ex:
        data['mensaje']=format(ex)
        data['exito']=False

    #Convierto diccionario a Json utilizando flask
    return jsonify(data)

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404 # El segundo es el codigo de error

def pagina_no_autorizada(error):
    return redirect(url_for('login'))

def inicializar_app(config): # Aca se ingresa como argumento la configuracion definida en config.py
    app.config.from_object(config)
    csrf.init_app(app)
    mail.init_app(app)
    #print(app.config)
    app.register_error_handler(404, pagina_no_encontrada) # El manejador de errores permite redirigir a la vista correcta cuando hay un error 404 en este caso. 
    app.register_error_handler(401, pagina_no_autorizada) # 401 Error de autenticacion, no autorizado
    return app
