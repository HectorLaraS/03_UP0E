from p1_cliente import Cliente
from p1_room_reservation import RoomReservation
import json
from p2_producto import Producto
import json
catalogo_path = "productos.json"

def retrieve_json_information(file_path: str) -> list:
    res:list = []
    with open(file_path) as json_file:
        catalog: dict = json.load(json_file)
        res = catalog.get("Productos")
    return res

def product_validation_exist(product: Producto) -> bool:
    product_exist = False
    product_list = retrieve_json_information(catalogo_path)
    for producto in product_list:
        if producto["ID"] == product.id_producto:
            product_exist = True
    return product_exist

def retrieve_product_information(product: Producto) -> dict:
    is_valid_product = product_validation_exist(product)
    list_product = retrieve_json_information(catalogo_path)
    result = {
        "id": 0000,
        "nombre": "None",
        "precio":0.0,
        "Message": "product not found"
    }
    if is_valid_product:
        for producto in list_product:
            if producto["ID"] == product.id_producto:
                product.nombre = producto["Name"]
                product.precio = producto["Precio"]
        result = {
            "id":product.id_producto,
            "nombre":product.nombre,
            "precio":product.precio,
            "Message": f"{product.nombre} - {product.precio}"
        }
    return result

def product_available(product: Producto, cantidad) -> bool:
    is_product_available = False
    list_product = retrieve_json_information(catalogo_path)
    for producto in list_product:
        if producto["ID"] == product.id_producto:
            if producto["Cantidad"] > cantidad:
                is_product_available = True
    return is_product_available


def print_ticket(cliente: Cliente, room: RoomReservation):
    total = room.days * room.price
    return f"""
    ********* TICKET *********
    Client....................
    Name: {cliente.Name} {cliente.Last}
    Mail: {cliente.Mail}
    Phone: {cliente.Phone}
    Room Information.........
    Days: {room.days}
    price: {room.price}
    Total: {total}
    **************************
    """

def print_ticket_purchase(producto: Producto, cantidad: int):
    total = producto.precio * cantidad
    return f"""
    ********* TICKET *********
    Product Information.........
    Nombre: {producto.nombre}
    Precio: {producto.precio}
    Cantidad: {cantidad}
    Total: {total}
    **************************
    """
def validate_input_vista_playa():
    tmp = input("Vista a la playa? (YES or NO): ")
    tmp_Upper = tmp.upper()
    if tmp_Upper == "YES":
        return True
    elif tmp_Upper == "NO":
        return False
    else:
        return validate_input_vista_playa()


def test():
    print("Is Connected")
