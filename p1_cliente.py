from Persona import Persona
from p1_persona import *
class Cliente(person):
    def __init__(self, nombre: str = "Jon", apellido: str = "Doe", mail: str = "my_mail@mail.com", phone:str = "0000000000"):
        person.__init__(self, nombre, apellido)
        self.__mail = mail
        self.__phone = phone

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail):
        self.__mail = mail

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        self.__phone = phone