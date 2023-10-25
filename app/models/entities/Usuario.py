from werkzeug.security import generate_password_hash, check_password_hash

class Usuario:
    def __init__(self, id_autor, usuario, password, tipousuario):
        self.id = id_autor
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    def encriptar_password(self, password):
        encriptado = generate_password_hash(password, salt_length=8) # len 94
        coincide = check_password_hash(encriptado, password)
        return coincide