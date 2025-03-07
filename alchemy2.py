import random

def craft_item(input_text): # example modification to adjust to AIDungeon input 
    

    parts = input_text.lower().split() #Convert the input to lowercase, and then split it into a list of words.
    if len(parts) < 2 || len(parts) > 2:  #if the player input is not two parts (the item to craft and a number)
        return "Invalid crafting command. Use /craft <craftItem> <material> <material2> ...  <amountToCraft>"

    number_crafts = parts[-1]
    requested_item = parts[0:-1]
    crafted_item = parts[1]
    # Milly what is the correct syntax here to get the second inputted numeric?

    if requested_item not in recipes:
        return f"Unknown item: {requested_item}."

    recipe = recipes.get(requested_item)
    if not recipe:
        return f"No recipe found for {requested_item}."

    recipe_materials = recipe["materials"]

    # Check if player has the required materials
    if not all(material in used_materials for material in recipe_materials):
        return "You don't have the required materials."

    # Simulate material depletion (optional, update context here in a full implementation)
    #context_update = f"You used {', '.join(recipe_materials)} to craft {requested_item}."

    # Crafting success message
    output = f"You successfully crafted a {requested_item}!"
    return output

# Example data (customize these!)
available_materials = ["wood", "stone", "iron", "leather", "cloth"]
craftable_items = ["sword", "axe", "armor"]
item_recipes = {
    "sword": {"materials": ["wood", "iron"]},
    "axe": {"materials": ["wood", "stone"]},
    "armor": {"materials": ["leather", "cloth"]}
}