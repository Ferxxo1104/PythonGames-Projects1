import random

# El usuario adivina el número aleatorio generado por la computadora.
def adivina_el_número(x):

    print("============================")
    print("  ¡Bienvenido(a) al Juego!  ")
    print("============================")
    print("Tu meta es adivinar el número generado por la computadora.")

    número_aleatorio = random.randint(1, x) # número aleatorio entre 1 y x.
    #usaremos la funcion randint del modulo random, que es para lograr generar un entero aleatorio

    # La predicción es 0 inicialmente para que no coincida con el número aleatorio. 
    predicción = 0

    # Continuar prediciendo el número hasta que la predicción sea correcta.
    while predicción != número_aleatorio:
        # El usuario ingresa un número.
        predicción = int(input(f"Adivina un número entre 1 y {x}: "))
        # Si el número es menor que el número aleatorio, se 
        # muestra un mensaje.
        if predicción < número_aleatorio:
            print("El número a adivinar es mayor. Intenta otra vez.")
        # Si el número es mayor que el número aleatorio, se
        # muestra un mensaje.
        elif predicción > número_aleatorio:
            print("El númeror a adivinar es menor. Intenta otra vez.")
            
    # El ciclo o bucle se detiene cuando el usuario adivina el número
    # correctamente y se muestra un mensaje final.
    print(f"¡Felicitaciones! Has adivinado el número {número_aleatorio} correctamente.")

# Llamar a la función
adivina_el_número(10)