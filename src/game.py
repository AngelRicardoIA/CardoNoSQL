import os
import random

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_jugador(numero):
    nombre = input(f"Ingrese el nombre del jugador {numero}: ")
    print(f"\n¡Bienvenido, {nombre}!")
    print("Pulse Enter para continuar...")
    input()
    limpiar()
    return nombre

limpiar()

print("¡Bienvenido a Cardo: Juego de cartas")

jugador1 = pedir_jugador(1)
jugador2 = pedir_jugador(2)

print("¿Cuántas rondas desean jugar (mínimo 3, máximo 10)? ")
entrada = input()

if entrada.isdigit():
    rondas = int(entrada)
else:
    rondas = -1 

if rondas < 3 or rondas > 10:
    print("Valor inválido. Se establecerá en 5 por defecto.")
    rondas = 5

print(f"¡Genial! Jugarán {rondas} rondas.")
print("Pulse Enter para comenzar el juego...")
input()
limpiar()

partida = {
    "jugador1": jugador1,
    "jugador2": jugador2,
    "rondas": rondas,
    "rondas_jugadas": []
}

def juego():
    jugadores = [jugador1, jugador2]
    cardoelector = random.choice(jugadores)
    if cardoelector == jugador1:
        cardomante = jugador2
    elif cardoelector == jugador2:
        cardomante = jugador1
    
    print(f"¡{cardoelector} comienza la partida!\n")
    



juego()
    


