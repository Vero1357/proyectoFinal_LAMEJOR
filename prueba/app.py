import mysql.connector

from flask import Flask, request, jsonify, render_template
from flask import request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__)
CORS(app) 

class Catalogo:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
        
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:

            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")                 
                self.conn.database = database
            else:
                raise err  
            
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT(4) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(3))''') 
             
        self.conn.commit()

        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

        # -------------------------------------------------------------------
        #Método para agregar un producto       
        # -------------------------------------------------------------------
    def agregar_producto(self, descripcion, cantidad, precio, imagen_url, proveedor):

        sql = "INSERT INTO productos (descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s)"   
        # Los valores se pasan como parámetros separados a la consulta, lo que asegura que sean tratados como datos y no como parte del código SQL. Los marcadores de posición %s son reemplazados por los valores reales de los parámetros cuando se ejecuta la consulta.
        
        valores = (descripcion, cantidad, precio, imagen_url, proveedor)        
    
        self.cursor.execute(sql, valores) 
        self.conn.commit() 
        return self.cursor.lastrowid #proporciona el valor de la clave primaria generada automáticamente por la base de datos para la fila recién insertada.

   
    # -------------------------------------------------------------------
    # Método para consultar un producto a partir de su código 
    # -------------------------------------------------------------------
    def consultar_producto(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()  #fetchone devuelve un sólo registro




    # -------------------------------------------------------------------
    # Método para modificar los datos de un producto a partir de su código 
    # -------------------------------------------------------------------
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):

        sql = "UPDATE productos SET descripcion=%s, cantidad=%s, precio=%s, imagen_url=%s, proveedor=%s WHERE codigo=%s"

        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit() 
        return self.cursor.rowcount > 0
        #rowCount() se utiliza para comprobar si una operación SQL ha afectado a alguna fila en la base de datos. Es una comparación que verifica si este número es mayor que cero, indica que al menos una fila fue afectada.    

    
    
    # -------------------------------------------------------------------
    # Método para obtener un listado de los productos en pantalla 
    # -------------------------------------------------------------------
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall() #devuelve todas las filas en una consulta SQL
        return productos



    # -------------------------------------------------------------------
    # Método para eliminar un producto a partir de su código 
    # -------------------------------------------------------------------
    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        producto_eliminado = producto['descripcion']
        print(f"Producto {producto_eliminado} eliminado.")

        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit() 
        return self.cursor.rowcount > 0
        #rowCount() se utiliza para comprobar si una operación SQL ha afectado a alguna fila en la base de datos. Es una comparación que verifica si este número es mayor que cero, indica que al menos una fila fue afectada.  
                


    def mostrar_producto (self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 50)
            print(f"Codigo     :{producto['codigo']}")
            print(f"Descripcion:{producto['descripcion']}")
            print(f"Cantidad   :{producto['cantidad']}")
            print(f"Precio     :{producto['precio']}")
            print(f"Imagen     :{producto['imagen']}")
            print(f"Proveedor  :{producto['proveedor']}")
            print("-"*50)  
        else:
            print("Producto no encontrado.")

#Programa principal
catalogo = Catalogo(host='localhost', user='root', password='root', database='lamejor')


#Agregamos productos

catalogo.agregar_producto("Sorrentinos", 10, 1500, "sorrentinos.jpeg", 1004)
catalogo.agregar_producto("Asado", 25, 2500, "asado_tira.jpeg", 2003)
catalogo.agregar_producto("Bife", 15, 6700, "bife.jpg", 2003)
catalogo.agregar_producto("Chorizo", 30, 1200, "chorizo.jpeg", 2003)
catalogo.agregar_producto("Empanadas", 43, 700, "empanadas.jpeg", 3001)
catalogo.agregar_producto("locro", 8, 9800, "locro.jpeg", 1004)
print()
# print("listado de productos:")
# productos = catalogo.listar_productos()
# print()
# print("datos de un producto:")
# catalogo.mostrar_producto(20)
# catalogo.eliminar_producto(20)
# print()
# print("listado de productos:")



#--------------------------------------------------------------------
# Listar todos los productos
#--------------------------------------------------------------------
@app.route("/productos", methods=["GET"]) #GET: método para obtener respuestas a nuestras peticiones
def listar_productos():
    productos = catalogo.listar_productos()
    return jsonify(productos)


#--------------------------------------------------------------------
# Mostrar un sólo producto según su código
#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["GET"])
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto), 201
    else:
        return "Producto no encontrado.", 404



# #Eliminamos un producto
# catalogo.eliminar_producto(4)

# #Listado de productos
# print("-"*30)
# print("Listado de productos:")
# productos = catalogo.listar_productos()
# for producto in productos:
#     print(producto)


# ----------------------- FLASK -------------------------
if __name__ == "__main__":
    app.run(debug=True)


