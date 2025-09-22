import json

# Example dictionary
data = {
    "tienda": "Mi Tienda Online",
    "productos": [
        {"id": 1, "nombre": "Camiseta", "precio": 199.99, "stock": 50},
        {"id": 2, "nombre": "Pantalón", "precio": 499.00, "stock": 30}
    ]
}

# File path for saving JSON
file_name = "test.json"

# Write dictionary to JSON file
with open(file_name, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Archivo guardado como {file_name}")
