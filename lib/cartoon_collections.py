dwarves_list = ['sneezy', 'sleepy', 'happy', 'doc', 'grumpy', 'dopey', 'bashful']

def roll_call_dwarves(dwarves_list):
    i = 1
    for dwarf in dwarves_list:
        print(f"{i}. {dwarf}")
        i += 1

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    return [f"{call.title()}!" for call in planeteer_calls]


assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(assorted_words):
    for word in assorted_words:
        if len(word) > 4:
            return True
    
    return False


CHEESES = ["camembert", "gouda", "cheddar"]

def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return food
        
    return None
