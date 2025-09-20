import json
name = "Hector Lara"
age = 32
country = "Mexico"
full_info = f"{name}, {age}, {country}"
print(full_info)
is_married = True

file_path = "data.json"
try:
    with open(file_path, "r") as file:
        data = json.load(file)
        print(data["Person Information"]["Name"])
except FileNotFoundError:
    print("File not found")