from Medico import Medico
import json

medico_lar0001 = Medico(name="Hector", last="Lara"
                        ,especialidad="Neurologia"
                        ,telefono="+528140207393"
                        ,email="hectorlaras.18@gmail.com")
print(medico_lar0001.dict_medico())

with open("data.json", "w") as file:
    json.dump(medico_lar0001.dict_medico(), file)