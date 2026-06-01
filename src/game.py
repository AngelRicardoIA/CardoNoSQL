import os
import random
from cartas import obtener_cartas

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_jugador(numero):
    nombre = input(f"Ingrese el nombre del jugador {numero}: ")
    print(f"\n¡Bienvenido, {nombre}!")
    print("Pulse Enter para continuar...")
    input()
    limpiar()
    return nombre

def pedir_rondas():
    print("¿Cuántas rondas desean jugar (mínimo 3, máximo 10)? ")
    entrada = input()

    if entrada.isdigit():
        rondas = int(entrada)
    else:
        rondas = -1
    if rondas < 3 or rondas > 10:
        print("Valor inválido. Se establecerá en 5 por defecto.")
        rondas = 5

    return rondas

def pedir_carta():
    while True:
        entrada = input("Elige una carta (1-3): ")
        if entrada.isdigit():
            carta = int(entrada)
            if 1 <= carta <= 3:
                return carta

        print("Carta inválida.")

def crear_partida():
    limpiar()
    print("¡Bienvenido a Cardo!")

    jugador1 = pedir_jugador(1)
    jugador2 = pedir_jugador(2)

    rondas = pedir_rondas()

    print(f"\n¡Genial! Jugarán {rondas} rondas.")
    print("Pulse Enter para comenzar el juego...")
    input()
    limpiar()

    partida = {
        "jugador1": jugador1,
        "jugador2": jugador2,
        "rondas": rondas,
        "rondas_jugadas": [],
        "puntos_jugador1": 0,
        "puntos_jugador2": 0
    }

    return partida

def juego(partida):
    jugador1 = partida["jugador1"]
    jugador2 = partida["jugador2"]
    jugadores = [jugador1, jugador2]

    cardoelector = random.choice(jugadores)

    if cardoelector == jugador1:
        cardomante = jugador2
    else:
        cardomante = jugador1

    for ronda in range(partida["rondas"]):
        limpiar()

        print(f"===== RONDA {ronda + 1} =====\n")
        print(f"Cardoelector: {cardoelector}")
        print(f"Cardomante: {cardomante}")
        print("\nPulse Enter para continuar...")
        input()

        cartas = obtener_cartas()

        print("Cartas del cardoelector:")
        for carta in cartas:
            indice = cartas.index(carta) + 1
            print(f"{indice}) {carta['descripcion']} - {carta['puntaje']}pts")

        carta_cardoelector = pedir_carta()
        carta_elegida = cartas[carta_cardoelector - 1]
        print(f"\nCarta elegida: {carta_elegida['descripcion']}")
        print("\nPulse Enter para pasar el turno al cardomante...")
        input()
        limpiar()

        print(f"Turno de {cardomante}")
        print("Hora de adivinar la carta del cardoelector...")
        for carta in cartas:
            indice = cartas.index(carta) + 1
            print(f"{indice}) {carta['descripcion']} - {carta['puntaje']}pts")

        carta_cardomante = pedir_carta()

        if carta_cardoelector == carta_cardomante:
            print("\n¡Adivinó!")
            puntos = carta_elegida["puntaje"]
            if puntos  == 1:
                puntos_ganados = 1
            elif puntos == 2:
                puntos_ganados = 1
            elif puntos == 3:
                puntos_ganados = 2

            if cardomante == jugador1:
                partida["puntos_jugador1"] += puntos_ganados
            else:
                partida["puntos_jugador2"] += puntos_ganados
            print(f"{cardomante} gana {puntos_ganados} puntos.")
        else:
            print("\nNo adivinó.")
            puntos_ganados = carta_elegida["puntaje"]
            if cardoelector == jugador1:
                partida["puntos_jugador1"] += puntos_ganados
            else:
                partida["puntos_jugador2"] += puntos_ganados
        
        partida["rondas_jugadas"].append({
            "ronda": ronda + 1,
            "cardoelector": cardoelector,
            "cardomante": cardomante,
            "carta_elegida": carta_elegida["descripcion"],
            "carta_cardomante": cartas[carta_cardomante - 1]["descripcion"],
            "puntos_ganados": puntos_ganados,
            "ganador": cardomante if carta_cardoelector == carta_cardomante else None
        })

        print(f"\nPuntaje actual: {jugador1} - {partida['puntos_jugador1']} pts | {jugador2} - {partida['puntos_jugador2']} pts")

        print("\nPulse Enter para continuar...")
        input()

        cardoelector, cardomante = cardomante, cardoelector

    if partida["puntos_jugador1"] > partida["puntos_jugador2"]:
        print(f"\n¡{jugador1} gana la partida con {partida['puntos_jugador1']} puntos!")
    elif partida["puntos_jugador2"] > partida["puntos_jugador1"]:
        print(f"\n¡{jugador2} gana la partida con {partida['puntos_jugador2']} puntos!")
    else:
        print("\n¡Es un empate!")
        print(f"\n{jugador1} - {partida['puntos_jugador1']} pts | {jugador2} - {partida['puntos_jugador2']} pts")
    print("\nFin de la partida.")

partida = crear_partida()
juego(partida)