catalogo_path = "productos.json"
import json
from lar_help_functions import *

res = retrieve_json_information(catalogo_path)
for producto in res:
    if producto["ID"] == 7001:
        name = producto["Name"]
        price = producto["Precio"]
        print(name, price)

