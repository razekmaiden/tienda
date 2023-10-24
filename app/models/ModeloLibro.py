from peewee import MySQLDatabase, Model, CharField, IntegerField, FloatField
from .entities.Autor import Autor
from .entities.Libro import Libro

# class Libro(Model):
#     isbn = CharField(primary_key=True)
#     titulo = CharField()
#     autor_id = IntegerField()
#     anoedicion = CharField()
#     precio = FloatField()

#     #class Meta:
#     #    database = db

class ModeloLibro():
    @classmethod
    def listar_libros(self, db):
        try:
            db.connect()
            sql = """SELECT LIB.isbn, LIB.titulo, LIB.anoedicion, LIB.precio,
                    AUT.apellidos, AUT.nombres
                    FROM libro LIB JOIN autor AUT ON LIB.autor_id = AUT.id
                    ORDER BY LIB.titulo ASC"""
            cursor = db.execute_sql(sql)
            data = cursor.fetchall()
            libros = []
            for row in data:
                aut = Autor(0, row[4], row[5])
                lib = Libro(row[0], row[1], aut, row[2], row[3])
                libros.append(lib)
            return libros
        except Exception as ex:
            print(ex)
            raise Exception(ex)
            