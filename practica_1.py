#TBD - crear un sistema de reserva de hotel donde se incluya el nombre, dias, tarifa y si la habitacion tiene vista al mar
from p1_cliente import *
from p1_room_reservation import *
from lar_help_functions import *

print("Ingrese los datos a como son Solicitados: ")
input_name:str = input("Ingrese Nombre: ")
input_last:str = input("Ingrese Apellido: ")
input_mail:str = input("Ingrese Correo: ")
input_phone:str = input("Ingrese Telefono: ")
input_dias: int = int(input("Ingrese Dias: "))
input_beach_view = validate_input_vista_playa()
costo = 0
if input_beach_view:
    costo = 750
else:
    costo = 500


client = Cliente()
client.Name = input_name
client.LastName = input_last
client.Mail = input_mail
client.Phone = input_phone

room = RoomReservation()
room.days = input_dias
room.Reservation = costo

ticket = print_ticket(client, room)
print(ticket)
