import csv

def get_cities():
    cities = []
    with open("worldcities.csv", mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cities.append(row["city"].lower())
    return cities

def play_game():
    all_cities = get_cities()
    used_cities = set()
    last_letter = ""

    print("Welcome to City Game! Type exit to quit.")

    while True:
        city = input(f"Enter city (starts with {last_letter}): ").lower().strip()
        if city == 'exit':
            break

        if city in used_cities:
            print("Repeated")
            continue

        if last_letter and not city.startswith(last_letter):
            print(f"City should start with {last_letter}!")
            continue

        if city in all_cities:
            used_cities.add(city)
            last_letter = city[-1]

            bot_found = False
            for city in all_cities:
                if city not in used_cities and city.startswith(last_letter):
                    print(f"Bot : {city.capitalize()}")
                    used_cities.add(city)
                    last_letter = city[-1]
                    bot_found = True
                    break

            if not bot_found:
                print("Bot cannot find")
                break
        else:
            print("City not found.")

play_game()