import sys
import json

def clean_amount(amt):
    # If its a list this implies a range of possible amounts
    if type(amt) == list:
        # Iterate over the list and clean the individual amounts
        for i in range(len(amt)):
            amt[i] = clean_amount(amt[i])
        # Join the amounts by a dash (this will work but look weird if len > 2)
        return "-".join(a for a in amt)
    else:
        # If there is no decimal
        if int(amt) == amt:
            # Drop the decimal in the string
            return str(int(amt))
        # Can we convert it to a fraction? -- Do it later
        else:
            return str(amt)

def parse_ingredient(ingredient):
    # Zero some stuff
    amount = None
    units = None
    
    # Iterate over the amounts and get the non-null entry
    for unit in ingredient["Amount"].keys():
        if ingredient["Amount"][unit] is not None:
            amount = ingredient["Amount"][unit]
            units = unit
    
    # If malformed 
    if amount is None or units is None:
        return None

    # Attach units to th eamount
    amount_str = clean_amount(amount) + f" {units}"
    # Return as a tuple so we can adjust spacing later
    return (amount_str,  ingredient['Ingredient'])

if __name__ == "__main__":
    # Load recipe
    with open(sys.argv[1], "r") as f:
        recipe = json.load(f)

    # Extract the ingredients as a list
    ingredients = list()
    for ingredient in recipe["ingredients"]:
        ingredients.append(parse_ingredient(ingredient))

    # Get the W I D E S T amount string
    max_amt_width = max([len(x[0]) for x in ingredients])

    print("\nIngredients:")
    for ingredient in ingredients:
        # Indent the amount
        print("  " + ingredient[0], end="")
        # Add spacing to line up all ingredients
        print("".join(" " for _ in range(max_amt_width - len(ingredient[0]))) + "  ", end="")
        # Print the ingredient
        print(ingredient[1])

