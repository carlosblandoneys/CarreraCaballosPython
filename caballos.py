import random
import os
import time
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    return random.choice(colors)

def draw_race(horses_positions, track_length, tribuna_lines):
    clear_console()
    animate_title()
    print("")
    for line in tribuna_lines:
        print(line)
    print("")
    print("====================================================")
    for pos in horses_positions:
        print("|" + " " * pos + "🐎" + " " * (track_length - pos) + "|" + "____🚩")
    print("=" * (track_length + 2))

def animate_title():
    title = "C  A  R  R  E  R  A     D  E     C  A  B  A  L  L  O  S"
    colors = [Fore.YELLOW, Fore.WHITE]
    color_index = int(time.time() * 2) % len(colors)
    print(colors[color_index] + title)

def get_bet():
    while True:
        bet = input("¿Por cuál caballo quieres apostar? (1-6): ")
        if bet.isdigit() and 1 <= int(bet) <= 6:
            return int(bet) - 1
        else:
            print("Entrada no válida. Por favor, introduce un número del 1 al 6.")

def fireworks_animation(tribuna_lines):
    frames = [
        [
            "        ",
            "   *    ",
            "        ",
            "        "
        ],
        [
            "        ",
            "  ***   ",
            "        ",
            "        "
        ],
        [
            "        ",
            " ** **  ",
            "  ***   ",
            "        "
        ],
        [
            "        ",
            "*** *** ",
            " ** **  ",
            "  ***   "
        ],
        [
            "  ***   ",
            "** * ** ",
            "*** *** ",
            " ** **  "
        ]
    ]
    
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    start_time = time.time()
    
    while time.time() - start_time < 3:
        for color in colors:
            for frame in frames:
                clear_console()
                animate_title()
                print("")
                for line in tribuna_lines:
                    print(line)
                print("")
                print("====================================================")
                for line in frame:
                    print(color + line + " ¡Ganaste!")
                time.sleep(0.1)


def generate_tribuna():
    tribuna_lines = [
        "|_________|  |__________|  |_________|  |__________|  🚩",
        "|_____o__o|  |o_o_oo_o__|  |____o_oo_|  |_o_o__o_o_|  |",
        "|o__o__o__|  |o__o_o_o_o|  |_o__o_o__|  |o_________|  |"
    ]
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for i in range(len(tribuna_lines)):
        line = ""
        for char in tribuna_lines[i]:
            if char in ['_', '|', '=']:
                line += Fore.WHITE + char
            elif char == 'o':
                line += get_random_color() + char
            else:
                line += char
        tribuna_lines[i] = line
    return tribuna_lines

def race():
    num_horses = 6
    track_length = 50
    horses = ["Caballo 1", "Caballo 2", "Caballo 3", "Caballo 4", "Caballo 5", "Caballo 6"]
    horses_positions = [0] * num_horses
    
    print("Bienvenido a la carrera de caballos!")
    for i, horse in enumerate(horses, 1):
        print(f"{i}. {horse}")
    
    bet = get_bet()
    tribuna_lines = generate_tribuna()

    while True:
        for i in range(num_horses):
            horses_positions[i] += random.randint(1, 3)
            if horses_positions[i] >= track_length:
                draw_race(horses_positions, track_length, tribuna_lines)
                winner = i
                print(f"¡{horses[winner]} ha ganado la carrera!")
                if winner == bet:
                    print("¡Felicidades! Tu caballo ha ganado.")
                    fireworks_animation(tribuna_lines) 
                else:
                    print(f"Lo siento, apostaste por {horses[bet]}.")
                return
        draw_race(horses_positions, track_length, tribuna_lines)
        time.sleep(0.2)

def main():
    while True:
        race()
        while True:
            restart = input("¿Deseas iniciar una nueva carrera? (s/n): ").lower()
            if restart in ['s', 'n']:
                break
            else:
                print("Entrada no válida. Por favor, introduce 's' para sí o 'n' para no.")
        if restart == 'n':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
