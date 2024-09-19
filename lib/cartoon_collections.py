def roll_call_dwarves(dwarves):
    [print(f"{i + 1}. {dwarves[i]}") for i in range(len(dwarves))]

def summon_captain_planet(planeteers):
    newlist = [planeteers[i].capitalize() + "!" for i in range(len(planeteers))]
    return newlist

def long_planeteer_calls(planeteers):
    for planeteer in planeteers:
        if len(planeteer) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    for ingredient in ingredients:
        if ingredient in ["camembert", "gouda", "cheddar"]:
            return ingredient
    return None