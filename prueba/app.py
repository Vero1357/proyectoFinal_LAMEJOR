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

    


    def listar_productos(self):
        print("-"*50)
        for producto in self.productos:
          print(f"Codigo     :{producto['codigo']}")
          print(f"Descripcion:{producto['descripcion']}")
          print(f"Cantidad   :{producto['cantidad']}")
          print(f"Precio     :{producto['precio']}")
          print(f"Imagen     :{producto['imagen']}")
          print(f"Proveedor  :{producto['proveedor']}")
          print("-"*50)   

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
    

catalogo = Catalogo()

catalogo.agregar_producto(15, "Sorrentinos", 10, 1500, "sorrentinos.jpeg", 1004)
catalogo.agregar_producto(20, "Asado", 25, 2500, "asado_tira.jpeg", 2003)
catalogo.agregar_producto(11,"Bife", 15, 6700, "bife.jpg", 2003)
catalogo.agregar_producto(12, "Chorizo", 30, 1200, "chorizo.jpeg", 2003)
catalogo.agregar_producto(13, "Empanadas", 43, 700, "empanadas.jpeg", 3001)
catalogo.agregar_producto(14, "locro", 8, 9800, "locro.jpeg", 1004)
print()
print("listado de productos:")
catalogo.listar_productos()
print()
print("datos de un producto:")
catalogo.mostrar_producto(20)
catalogo.eliminar_producto(20)
print()
print("listado de productos:")
catalogo.listar_productos()
