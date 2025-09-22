from p1_cliente import Cliente
from p1_room_reservation import RoomReservation

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
