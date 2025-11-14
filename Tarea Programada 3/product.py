class Product:

    def __init__(self, nombre, categoria, precio, proveedor, id=None):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.proveedor = proveedor

    def __str__(self):
        return f"[{self.id}] {self.nombre} | {self.categoria} | ₡{self.precio} | Prov: {self.proveedor}"
