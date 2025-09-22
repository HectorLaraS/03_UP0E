catalogo_path = "productos.json"
import json
from lar_help_functions import *

res = retrieve_json_information(catalogo_path)
for producto in res:
    if producto["ID"] == 7001:
        name = producto["Name"]
        price = producto["Precio"]
        print(name, price)
producto = Producto()
producto.id_producto = 7004
res_2 = product_validation_exist(producto)
print(res_2)
product_info:dict = retrieve_product_information(producto)
final_product = Producto()
final_product.id_producto = product_info["id"]
final_product.nombre = product_info["nombre"]
final_product.precio = product_info["precio"]
print("**********************")
#print(f"Nombre: {final_product._nombre}, {final_product.nombre}")
print(final_product.product_information_dict())
is_product_available = product_available(final_product)

print("**********************")
print(product_info)
print("**********************")
print(final_product.nombre)
print(final_product.precio)
print(final_product.product_information_dict())
print(is_product_available)