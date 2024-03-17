import random

def jugar_piedra_papel_tijera(jugador, computadora):
    opciones = ["piedra", "papel", "tijera"]

    if jugador == computadora:
        return "Empate"

    if jugador == "piedra":
        if computadora == "papel":
            return "Computadora gana"
        else:
            return "Jugador gana"

    if jugador == "papel":
        if computadora == "tijera":
            return "Computadora gana"
        else:
            return "Jugador gana"

    if jugador == "tijera":
        if computadora == "piedra":
            return "Computadora gana"
        else:
            return "Jugador gana"

def main():
    print("Bienvenido a Piedra, Papel o Tijera!")
    jugador = input("Elige: piedra, papel o tijera: ").lower()
    computadora = random.choice(["piedra", "papel", "tijera"])
    resultado = jugar_piedra_papel_tijera(jugador, computadora)
    print(f"Jugador elige {jugador}")
    print(f"Computadora elige {computadora}")
    print(resultado)

if __name__ == '__main__':
    main()
