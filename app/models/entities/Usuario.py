from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Heredar de la clase UserMixin permite que la clase Usuario sea compatible con el control de sesiones (error de atributo 'is_active')
class Usuario(UserMixin):
    def __init__(self, id_usuario, usuario, password, tipousuario):
        self.id = id_usuario
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    def encriptar_password(self, password):
        encriptado = generate_password_hash(password, salt_length=8) # len 94
        coincide = check_password_hash(encriptado, password)
        return coincide