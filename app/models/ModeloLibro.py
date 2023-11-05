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
            db.close()
            libros = []
            for row in data:
                aut = Autor(0, row[4], row[5])
                lib = Libro(row[0], row[1], aut, row[2], row[3])
                libros.append(lib)
            return libros
        except Exception as ex:
            print(ex)
            raise Exception(ex)
        
    @classmethod
    def listar_libros_vendidos(self, db):
        try:
            
            db.connect()
            sql = """SELECT COM.libro_isbn, LIB.titulo, LIB.precio,
                    COUNT(COM.libro_isbn) AS Unidades_Vendidas 
                    FROM compra COM JOIN libro LIB ON COM.libro_isbn = LIB.ISBN
                    GROUP BY COM.libro_isbn ORDER BY 4 DESC, 2 ASC"""
            cursor = db.execute_sql(sql)
            data = cursor.fetchall()
            db.close()
            libros = []
            for row in data:
                #isbn, titulo, autor, anoedicion, precio)
                lib = Libro(row[0], row[1], None, None, row[2])
                lib.unidades_vendidas = int(row[3])
                libros.append(lib)
            return libros
        except Exception as ex:
            print(ex)
            raise Exception(ex)
            
    
    @classmethod
    def leer_libro(self, db, isbn):
        try:
            db.connect()
            sql = f"""SELECT isbn, titulo, anoedicion, precio
                    FROM libro WHERE isbn = '{isbn}'"""
            cursor = db.execute_sql(sql)
            data = cursor.fetchone()
            db.close()
            libro = Libro(data[0], data[1], None, data[2], data[3])
            return libro
        except Exception as ex:
            print(ex)
            raise Exception(ex)