from p1_cliente import *
class RoomReservation:
    def __init__(self, days: int = 1, has_beach_view: bool = False, price: float = 500.00 ):
        self._days: int = days
        self._has_beach_view: bool = has_beach_view
        self._price: float = price

    @property
    def days(self):
        return self._days
    @days.setter
    def days(self, value):
        self._days = value
    @property
    def has_beach_view(self):
        return self._has_beach_view
    @has_beach_view.setter
    def has_beach_view(self, value):
        self._has_beach_view = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value