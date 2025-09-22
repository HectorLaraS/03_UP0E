class Producto:
    def __init__(self,nombre: str = "None",precio: float = 0.0, id_producto: int = 7001):
        self._nombre = nombre
        self._precio = precio
        self._id_producto = id_producto

    def __str__(self):
        return f"Nombre: {self._nombre}, Precio: {self._precio}"
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def id_producto(self,id_producto):
        self._id_producto = id_producto

    def product_information_dict(self):
        return {
            "ID": self._id_producto,
            "Name": self._nombre,
            "Price": self._precio
        }

if __name__ == "__main__":
    producto = Producto()
    producto.nombre = "Coca Cola"
    producto.precio = 1
    producto.id_producto = 7010
    print(producto)