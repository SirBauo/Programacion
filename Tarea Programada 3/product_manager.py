from product import Product
from product_repo import ProductRepo

repo = ProductRepo()

def store(data):
    nuevo = Product(data[0], data[1], data[2], data[3])
    repo.save(nuevo)

def get_all():
    return repo.find_all()

def find_by_name(seq):
    return repo.find_by_name(seq)

def find_by_price(minimo, maximo):
    return repo.find_by_price_range(minimo, maximo)

def update_product(id, precio, proveedor):
    repo.update(id, precio, proveedor)

def delete_product(id):
    repo.delete(id)
