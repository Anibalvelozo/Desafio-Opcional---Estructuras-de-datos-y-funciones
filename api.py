import requests 


response = requests.get("https://reqres.in/api/users")
users_data = response.json()
print("Información de los usuarios:")
print(users_data)


new_user = {
    "name": "Ignacio",
    "job": "Profesor"
}
response = requests.post("https://reqres.in/api/users", json=new_user)
created_user = response.json()
print("\nUsuario creado:")
print(created_user)


updated_user_data = {
    "residence": "zion"
}
response = requests.put("https://reqres.in/api/users/2", json=updated_user_data)
updated_user = response.json()
print("\nUsuario actualizado:")
print(updated_user)


response = requests.delete("https://reqres.in/api/users/3")
print("\nCódigo de respuesta al eliminar usuario Tracey:", response.status_code)