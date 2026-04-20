import csv
import random

def get_cities():
    cities = []
    with open('worldcities.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cities.append({'city': row['city'].lower(), 'country': row['country']})
    return cities

def play_game():
    all_cities_data = get_cities()
    used_cities = set()
    last_letter = ''
    
    print("Welcome to City Game! Type 'exit' to quit. Type 'help' for a hint.")
    
    while True:
        prompt = f"Enter city (starts with {last_letter.upper()}): " if last_letter else "Enter city: "
        city = input(prompt).lower().strip()
        
        if city == 'exit':
            break
            
        if city == 'help':
            suggestions = [
                item['city'] for item in all_cities_data 
                if item['city'] not in used_cities and (not last_letter or item['city'].startswith(last_letter))
            ]
            if suggestions:
                print(f"Bot Suggestion: {random.choice(suggestions).capitalize()}")
            else:
                print("No suggestions available!")
            continue
            
        if city in used_cities:
            print("Repeated city!")
            continue
            
        if last_letter and not city.startswith(last_letter):
            print(f"City should start with {last_letter.upper()}!")
            continue
            
        city_entry = next((item for item in all_cities_data if item['city'] == city), None)
        
        if city_entry:
            used_cities.add(city)
            last_letter = city[-1]
            
            bot_found = False
            random.shuffle(all_cities_data)
            
            for item in all_cities_data:
                c = item['city']
                if c not in used_cities and c.startswith(last_letter):
                    print(f"Bot: {c.capitalize()}")
                    used_cities.add(c)
                    last_letter = c[-1]
                    bot_found = True
                    break
            
            if not bot_found:
                print("Bot cannot find a city! You win!")
                break
        else:
            print("City not found in database.")

play_game()