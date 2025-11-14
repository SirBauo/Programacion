import sqlite3
from product import Product

class ProductRepo:

    def __init__(self):
        self.__conn = sqlite3.connect("productos.db")
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            proveedor TEXT NOT NULL
        )
        """)
        self.__conn.commit()

    def save(self, product: Product):
        self.__cursor.execute(f"""
        INSERT INTO productos (nombre, categoria, precio, proveedor)
        VALUES ('{product.nombre}', '{product.categoria}', {product.precio}, '{product.proveedor}')
        """)
        self.__conn.commit()

    def find_all(self):
        self.__cursor.execute("SELECT * FROM productos")
        rows = self.__cursor.fetchall()
        return [Product(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]

    def find_by_name(self, name_seq):
        self.__cursor.execute(f"SELECT * FROM productos WHERE nombre LIKE '%{name_seq}%'")
        rows = self.__cursor.fetchall()
        return [Product(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]

    def find_by_price_range(self, minimo, maximo):
        self.__cursor.execute(f"SELECT * FROM productos WHERE precio BETWEEN {minimo} AND {maximo}")
        rows = self.__cursor.fetchall()
        return [Product(row[1], row[2], row[3], row[4], id=row[0]) for row in rows]

    def update(self, id, nuevo_precio, nuevo_proveedor):
        self.__cursor.execute(f"""
        UPDATE productos
        SET precio = {nuevo_precio}, proveedor = '{nuevo_proveedor}'
        WHERE id = {id}
        """)
        self.__conn.commit()

    def delete(self, id):
        self.__cursor.execute(f"DELETE FROM productos WHERE id = {id}")
        self.__conn.commit()
