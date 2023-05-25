import random
import string


from palabras import palabras
from vidasDiccionarioVisual import vidasDiccionarioVisual


def obtenerPalabraValida(listaDePalabras):
    #Seleccionaremos una palabra al azar
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("===========================")
    print("Bienvenido(a) a el ahorcado")
    print("===========================")

    palabra = obtenerPalabraValida(palabras)

    letrasPorAdivinar = set(palabra)
    letrasAdivinadas = set() 
    abc = set(string.ascii_uppercase)

    vidas = 7 

    while len(letrasPorAdivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letrasAdivinadas)}")

        #Mostrar el estado actual de la palabra
        palabraLista = [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        #Mostrar el estado de la horca
        print(vidasDiccionarioVisual[vidas])
        #Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabraLista)}")

        letraUsuario = input("Escoge una letra: ").upper()

        #Si la letra esta e el abecedario y no esta en el conjunto de letras que ya se ingresaron, se añade la letra al conjunto de letras ya ingresadas.
        if letraUsuario in abc - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)

            #La letra está en la palbra, o no?
            #Si está, quitar la letra del conjunto letrasPorAdivinar
            #Pero si no está, quitar una vida.
            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print(' ')
            else:
                vidas -= 1
                print(f"\n Tu letra, {letraUsuario} no está en la palabra a adivinar. \n Te quedan {vidas} vidas. \n Usalas bien")
        #Si la letra escogida por el usuario ya fue ingresada
        elif letraUsuario in letrasAdivinadas:
            print("\n Ya has escogido esta letra. Por favor escoge una nueva letra")
        else:
            print("\n Esta letra no es valida. ")

    #El juego llega hasta esta linea, cuando se adivinan las letras de la palabra ó cuando se agotan las vidas.
    if vidas == 0:
        print(vidasDiccionarioVisual[vidas])
        print(f"Ahorcado!! perdiste!. Esfuerzate más. la palabra era: {palabra}")
    else:
        print(f"Excelente trabajo!! Has adivinado la palabra! {palabra}")

ahorcado()