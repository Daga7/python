import datetime

# Crear un diccionario para almacenar los puntajes
puntajes = {}

# Función para obtener la edad a partir de la fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Función para ingresar un nuevo puntaje con juego de adivinanza
def ingresar_puntaje():
    nombre = input("Ingresa tu nombre completo: ")
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    
    edad = calcular_edad(fecha_nacimiento)
    
    if edad >= 18:
        print("¡Bienvenido al juego de adivinanza!")
        print("Adivina el número secreto entre 1 y 10.")
        numero_secreto = 7  
        intentos = 0
        
        while True:
            intento = int(input("Escribe tu respuesta : "))
            intentos += 1
            
            if intento == numero_secreto:
                puntaje = 10 - intentos + 1
                print(f"¡Correcto! Tu puntaje es {puntaje}.")
                break
            elif intentos >= 3:
                print("Lo siento, has agotado tus intentos. El número secreto era 7.")
                puntaje = 0
                break
            else:
                print("¡Incorrecto! Inténtalo de nuevo.")
        
        puntajes[nombre] = puntaje
        print(f"Puntaje de {nombre} registrado con éxito.")
    else:
        print("Lo siento, debes ser mayor de 18 años para jugar.")

# Función para mostrar los puntajes ordenados de mayor a menor
def mostrar_puntajes():
    if puntajes:
        ordenar_puntajes = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
        print("Puntajes ordenados de mayor a menor:")
        for nombre, puntaje in ordenar_puntajes:
            print(f"{nombre}: {puntaje}")
    else:
        print("No hay puntajes registrados.")

# Función principal
def main():
    while True:
        print("\n1. Ingresar puntaje")
        print("2. Mostrar puntajes")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            ingresar_puntaje()
        elif opcion == "2":
            mostrar_puntajes()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
