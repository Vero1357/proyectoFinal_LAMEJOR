import mysql.connector

class Catalogo:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect (
            host = host,
            user = user,
            password = password,
            database = database

        )
        
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:

            if err.errno == mysql.connector.errocode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
                self.coon.database = database
            else:
                raise err
        
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS productos (
                                codigo INT AUTO_INCREMENT PRIMARY KEY,
                                descripcion VARCHAR(255) NOT NULL,
                                cantidad INT NOT NULL,
                                precio DECIMAL(10, 2) NOT NULL,
                                imagen_url VARCHAR(255),
                                proveedor INT) ''')
        
        self.coon.commit ()

        self.cursor.close ()
        self.cursor = self.coon.cursor(dictionary = True)




    def agregar_producto (self, codigo, descripcion, cantidad, precio, imagen, proveedor):
    
         if self.consultar_producto(codigo):
             return False
    
         nuevo_producto = {
           'codigo' : codigo,
           'descripcion' : descripcion,
           'cantidad' : cantidad,
           'precio' : precio, 
           'imagen' : imagen,
           'proveedor' : proveedor
     }

         self.productos.append(nuevo_producto)
         return True

    def consultar_producto(self, codigo):
         for producto in self.productos:
              if producto['codigo'] == codigo:
                  return producto
         return False

    def modificar_producto (self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
         for producto in self.productos:
              if producto ['codigo'] == codigo:
                 producto ['descripcion'] = nueva_descripcion
                 producto ['cantidad'] = nueva_cantidad
                 producto ['precio'] = nuevo_precio
                 producto ['imagen'] = nueva_imagen
                 producto ['proveedor'] = nuevo_proveedor
              return True
         return False

    def eliminar_producto (self, codigo):
        for producto in self.productos:
            if producto ['codigo'] == codigo:
               self.productos.remove(producto)
               print()
               print("Producto eliminado correctamente")
               return True
               print()
               print ("Producto no encontrado")
        return False
    

    def listar_productos(self):
         for producto in self.productos:
          print("-"*50)
          print(f"Codigo     :{producto['codigo']}")
          print(f"Descripcion:{producto['descripcion']}")
          print(f"Cantidad   :{producto['cantidad']}")
          print(f"Precio     :{producto['precio']}")
          print(f"Imagen     :{producto['imagen']}")
          print(f"Proveedor  :{producto['proveedor']}")
          print ("-"*50)



    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print ("-"*50)
            print(f"Codigo     :{producto['codigo']}")
            print(f"Descripcion:{producto['descripcion']}")
            print(f"Cantidad   :{producto['cantidad']}")
            print(f"Precio     :{producto['precio']}")
            print(f"Imagen     :{producto['imagen']}")
            print(f"Proveedor  :{producto['proveedor']}")
            print ("-"*50)
        else:
            print ("Producto no encotrado.")
     

catalogo = Catalogo(host='localhost', user='root', password='root', database='lamejor')

catalogo.agregar_producto(15 , "Sorrentinos", 10, 1500, "sorrentinos.jpg", 1004)
catalogo.agregar_producto(20 , "Asado", 25, 2500, "asado.jpg", 2003)

catalogo.mostrar_producto(10)



# catalogo.listar_productos()
# print()
# catalogo.eliminar_producto(15)
# print()3
# catalogo.listar_productos()


