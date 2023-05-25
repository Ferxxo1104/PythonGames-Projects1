import random

def jugar():
    user = input(f"Escoge un objeto: (pi) piedra, (pa) papel, (ti) tijera. \n").lower()

    computadora = random.choice(["pi","pa","ti"])

    if user == computadora:
        print(f"La computadora escogió: {computadora}")
        return "EMPATE!"

    if jugadorGano(user,computadora):
        print(f"La computadora escogió: {computadora}")
        return "GANASTE!"
    
    print(f"La computadora escogió: {computadora}")
    return "PERDISTE!"

def jugadorGano(jugador, oponente):
    #Retornara True si el jugador gana
    #Piedra gana tijera (pi > ti)
    #tijera gana papel (ti > pa)
    #papel gana piedra (pa > pi)

    if ((jugador == "pi" and oponente == "ti")
        or (jugador == "ti" and oponente == "pa")
        or (jugador == "pa" and oponente == "pi")):
        return True
    else:
        return False
    

print(jugar())