catalogo_path = "productos.json"
import json
from lar_help_functions import *

producto = Producto()
producto.id_producto = 7001
product_on_db = product_validation_exist(producto)
if not product_on_db:
    print("Producto no existe")
else:
    cantidad = 10
    product_info:dict = retrieve_product_information(producto)
    final_product = Producto()
    final_product.id_producto = product_info["id"]
    final_product.nombre = product_info["nombre"]
    final_product.precio = product_info["precio"]
    is_product_available = product_available(final_product,cantidad)
    if is_product_available:
        print("Product available")
        print(print_ticket_purchase(final_product,cantidad))
    else:
        print("Product not available")
