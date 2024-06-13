# defino lista de productos

class Catalogo:

    productos = []

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
     

catalogo = Catalogo()

catalogo.agregar_producto(15 , "Sorrentinos", 10, 1500, "sorrentinos.jpg", 1004)
catalogo.agregar_producto(20 , "Asado", 25, 2500, "asado.jpg", 2003)

catalogo.mostrar_producto(10)



#catalogo.listar_productos()
#print()
#catalogo.eliminar_producto(15)
#print()3
#catalogo.listar_productos()


