from Persona import Persona
from p1_persona import *
class Cliente(person):
    def __init__(self, nombre: str = "Jon", apellido: str = "Doe", mail: str = "my_mail@mail.com", phone:str = "0000000000"):
        person.__init__(self, nombre, apellido)
        self._mail = mail
        self._phone = phone

    @property
    def Mail(self):
        return self._mail
    @Mail.setter
    def Mail(self, mail):
        self._mail = mail

    @property
    def Phone(self):
        return self._phone
    @Phone.setter
    def Phone(self, phone):
        self._phone = phone

    def client_information(self):
        return {
            "Person Information": {
                "Name": self._name,
                "Last": self._last
            },
            "Contact Information": {
                "Mail": self._mail,
                "Phone": self._phone,
            },
        }