import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_race(horses_positions, track_length):
    
    clear_console()
    print("C  A  R  R  E  R  A     D  E     C  A  B  A  L  L  O  S")
    print("")
    print("|_________|  |__________|  |_________|  |__________|  🚩")
    print("|_____o__o|  |o_o_oo_o__|  |____o_oo_|  |_o_o__o_o_|  |")
    print("|o__o__o__|  |o__o_o_o_o|  |_o__o_o__|  |o_________|  |")
    print("_______________________________________________________")
    print("")
    
    print("====================================================")
    for pos in horses_positions:
        print("|" + " " * pos + "🐎" + " " * (track_length - pos) + "|" + "____🚩")
    print("=" * (track_length + 2))
    

def race():
    num_horses = 6
    track_length = 50
    horses = ["Caballo 1", "Caballo 2", "Caballo 3", "Caballo 4", "Caballo 5", "Caballo 6"]
    horses_positions = [0] * num_horses
    
    print("Bienvenido a la carrera de caballos!")
    for i, horse in enumerate(horses, 1):
        print(f"{i}. {horse}")
    bet = int(input("¿Por cuál caballo quieres apostar? (1-6): ")) - 1

    while True:
        for i in range(num_horses):
            horses_positions[i] += random.randint(1, 3)
            if horses_positions[i] >= track_length:
                draw_race(horses_positions, track_length)
                winner = i
                print(f"¡{horses[winner]} ha ganado la carrera!")
                if winner == bet:
                    print("¡Felicidades! Tu caballo ha ganado.")
                else:
                    print(f"Lo siento, apostaste por {horses[bet]}.")
                return
        draw_race(horses_positions, track_length)
        time.sleep(0.2)

if __name__ == "__main__":
    race()
