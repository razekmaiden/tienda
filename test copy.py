from peewee import *

# Set up a MySQL database connection
db = MySQLDatabase('tienda', host='localhost', user='root', password='')

# Define a model representing a table in the database
class Libro(Model):
    isbn = CharField(primary_key=True)
    titulo = CharField()
    autor_id = IntegerField()
    anoedicion = CharField()
    precio = FloatField()

    class Meta:
        database = db

# Connect to the database
db.connect()

# Create tables if they don't exist
#db.create_tables([Libro])

# Example usage: insert a new product
#product = Product(name='Keyboard', price=29.99)
#product.save()

# Example usage: query products
products = Libro.select()
for product in products:
#    print(f"Name: {product.isbn}, Titulo: {product.titulo}")
    print(product)

# Close the database connection
db.close()
