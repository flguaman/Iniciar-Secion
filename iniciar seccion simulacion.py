# Diccionario de usuarios y contraseñas
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}

# Función para crear un nuevo usuario
def crear_usuario():
    nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ")
    nueva_contraseña = input("Ingrese una nueva contraseña: ")
    
    # Verificar si el usuario ya existe
    if nuevo_usuario in usuarios:
        print("El nombre de usuario ya está en uso. Por favor, elige otro.")
    else:
        usuarios[nuevo_usuario] = nueva_contraseña
        print(f"Usuario '{nuevo_usuario}' creado exitosamente.")

# Función para iniciar sesión
def iniciar_sesion():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    # Verificar si el usuario existe en el diccionario
    if username in usuarios:
        # Verificar si la contraseña es correcta
        if usuarios[username] == password:
            print(f"Bienvenido, {username}!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

# Menú principal
while True:
    print("\nMenú principal:")
    print("1. Crear nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")