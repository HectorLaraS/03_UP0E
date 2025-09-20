import json
from Persona import Persona
class Medico(Persona):
    def __init__(self, name:str ="Jon", last:str ="Doe", especialidad:str ="Especialidad", telefono:str ="Telefono", email:str ="Email"):
        Persona.__init__(self, name, last)
        self._especialidad = especialidad
        self._telefono = telefono
        self._email = email

    def dict_medico(self):
        return {
            "Person Information": {
                "Name": self._name,
                "Last": self._last
            },"Profesional Information": {
                "Especialidad": self._especialidad,
            },
            "Contact Information": {
                "Mail": self._email,
                "Phone": self._telefono,
            },
        }