import random

# El computador va a adivinar tu número.
def adivinaElNumeroComputadora(x):
    
    print("=========================")
    print(" Bienvenido(a) al juego! ")
    print("=========================")
    print(f"Igresa el rango entre 1 y {x} que la computadora va a adivinar.")

    #Intervalo de los valores validos
    limiteInferior = 1
    limiteSuperior = x
    respuesta = ""

    while respuesta != "c":
        # Generar prediccion.
        if limiteInferior != limiteSuperior:
            prediccion = random.randint(limiteInferior,limiteSuperior)
        else:
            prediccion = limiteInferior
        
        respuesta = input(f"Mi  prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta ingresa (C) ").lower()

        if respuesta == "a":
            limiteSuperior = prediccion - 1
        elif respuesta == "b":
            limiteInferior = prediccion + 1

    print(f"Geniaal!  La computadora ha adivinado tu número: {prediccion}")


adivinaElNumeroComputadora(15)