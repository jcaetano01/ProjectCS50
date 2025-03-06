from blessed import Terminal
term = Terminal()

def main():
    maps = ["de_heaven", "de_underpass", "de_dusty", "de_engine", "de_nuclear", "de_inca", "de_cxchz"]
    weapons = {
        "Ph4Mthon-S": "Medium accuracy and ideal for medium-range combat.",
        "Vankal-k7": "High power and damage but less accurate over long distances.",
        "Bullmas": "A balanced option between firepower and control.",
        "Umpectre": "Good for short distances and quick shootouts.",
        "AWperator": "Ideal for long distances with devastating power in one shot."
    }

    chosen_map = choose_map(maps)
    chosen_weapon = choose_weapon(weapons)
    chosen_side = choose_side()

    print(term.bold(term.cyan(f"Summary: Map - {chosen_map}, Weapon - {chosen_weapon}, Side - {chosen_side}")))


def choose_map(maps):
    while True:
        print(term.bold("Choose a map from the following options:"))
        for idx, map_name in enumerate(maps, start=1):
            print(f"{term.green}{idx}. {map_name}{term.normal}")

        choice = input(term.yellow("Enter the number of your choice: "))

        if choice.isdigit() and 1 <= int(choice) <= len(maps):
            selected_map = maps[int(choice) - 1]
            print(term.yellow(f"You have chosen the map: {selected_map}"))
            return selected_map
        else:
            print(term.red("Invalid choice. Please select a valid number."))

def choose_weapon(weapons):
    while True:
        print(term.bold("Choose a primary weapon from the following options:"))
        for idx, (weapon, description) in enumerate(weapons.items(), start=1):
            print(f"{term.green}{idx}. {weapon} - {description}{term.normal}")

        choice = input(term.yellow("Enter the number of your choice: "))

        if choice.isdigit() and 1 <= int(choice) <= len(weapons):
            selected_weapon = list(weapons.keys())[int(choice) - 1]
            print(term.yellow(f"You have chosen the weapon: {selected_weapon}"))
            return selected_weapon
        else:
            print(term.red("Invalid choice. Please select a valid number."))

def choose_side():
    while True:
        print(term.bold("Choose your side:"))
        print(f"{term.green}1. Attacking{term.normal}")
        print(f"{term.green}2. Defending{term.normal}")

        choice = input(term.yellow("Enter 1 for Attacking or 2 for Defending: "))

        if choice == '1':
            print(term.yellow("You have chosen to attack."))
            return "Attacking"
        elif choice == '2':
            print(term.yellow("You have chosen to defend."))
            return "Defending"
        else:
            print(term.red("Invalid choice. Please enter 1 or 2."))



if __name__ == "__main__":
    main()






