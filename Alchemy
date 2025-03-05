import random

def craft_item(input_text, available_materials, craftable_items, item_recipes):
    """Crafts an item based on player input."""

    parts = input_text.lower().split() #Convert the input to lowercase, and then split it into a list of words.
    if len(parts) < 2:
        return "Invalid crafting command. Use /craft <material1> <material2> ... <item>."

    requested_item = parts[-1]
    used_materials = parts[1:-1]

    if requested_item not in craftable_items:
        return f"Unknown item: {requested_item}."

    recipe = item_recipes.get(requested_item)
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