class Autor:
    def __init__(self, id_autor,apellidos, nombres, fechanacimiento=None):
        self.id = id_autor
        self.apellidos = apellidos
        self.nombres = nombres
        self.fechanacimiento = fechanacimiento

    def nombre_completo(self):
        return f"{self.apellidos}, {self.nombres}"