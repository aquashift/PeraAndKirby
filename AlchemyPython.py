

class Recipes:
    def __init__(self, ingredients, crafted_item):
        self.ingredients = ingredients 
        self.crafted_item = crafted_item

class Ingredient:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        # add any other relevant attributes, like rarity or cost

    def __str__(self):
        return f"{self.name}: {self.description}"
    def __repr__(self):
        return f"{self.name}"





# create an ingredient instance
mandrake_root = Ingredient(
    "mandrake root", "A rare and powerful herb with magical properties.")
phoenix_feather = Ingredient("phoenix feather",
                             "Taken from the plumage of the Fire Bird.")
coal = Ingredient(
    "coal",
    "Slow-burned wood - contains a lot of potential combustible energy.")
burnt_wood = Ingredient("burnt wood", "An inferior product compared to coal.")
basilisk_talon = Ingredient(
    "basilisk talon",
    "A claw that was harvested from a perished Basilisk creature.")
water = Ingredient(
    "water",
    "The most basic composite of life.  Can be obtained anywhere there is life."
)
elemental_leaf = Ingredient(
    "elemental leaf",
    "An otherwise ordinary leaf, imbued with a unique type of magic.")
oil = Ingredient("oil",
                 "Rendered fat from an animal, usually a mammal or bird.")
red_herb = Ingredient(
    "red herb",
    "Any herb that is pigmented dark red, and native to the high-elevation plateau in the North continent."
)
chimera_claw = Ingredient("chimera claw", "Hardened keratin product obtained fromh harvesting the paw of a chimera monster.")
#next ingredient us both ingredient and finished crafted item
dragons_breath = Ingredient("Dragon's Breath", "A common way to preserve the attributes of an elemental leaf; by soaking it in oil immediately after imbued with elemental magic, an alchemist can expect a week more of potency versus no oil treatment.")
dandelion_milk = Ingredient("dandelion milk", "Procured by macerating the thicker roots of the dandelion plant.")

# Define items and recipes
inventory = {}
recipes = {
    "phoenix ashes": {
        "phoenix feather": 4,
        "alternative ingredients": [{
            "coal": 1
        }, {
            "burnt wood": 2
        }]
    },
    "Basilisk Blood": {
        "basilisk talon": 3,
        "water": 1
    },
    "Dragon's Breath": {
        "elemental leaf": 1,
        "oil": 1
    },
    "Health_Potion": {
        "red herb": 3,
        "water": 1
    },
    "Imbued Chimera Claw": {
        "chimera claw": 1,
        "Dragon's Breath": 1,
        "dandelion milk": 1
    }
}


# Check player inventory for item (in general)
def has_item(item):
    return item in inventory


# Function to add items to the player's inventory
def add_item(item):
    if has_item(item):
        inventory[item] += 1
    else:
        inventory[item] = 1


# Function to remove items from inventory
def remove_items(item):
    if has_item(item):
        inventory[item] -= item


# Check if player has required items in correct amounts for crafting
def has_recipe_items(required_items):
    for item, amount in required_items.items():
        if item not in inventory or inventory[item] < amount:
            return False
    return True


# Function to craft an item
def craft_item(craftable_item):
    if craftable_item in recipes and has_recipe_items(recipes[craftable_item]):
        # If the recipe exists and the player has the required recipe items
        # Remove the used items from inventory
        for material, amount in recipes[craftable_item].items():
            if material != "alternative_ingredients":
                remove_items(amount)
