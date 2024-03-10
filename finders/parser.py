import yaml

with open('pokemons.yaml', 'r') as file:
    pokemon_data = yaml.safe_load(file)

category_ranges = {}

# Iterate over each category in the YAML data
for category, pokemons in pokemon_data.items():
    # Generate a category range dynamically based on the number of categories
    start = len(category_ranges) * 1000
    end = (len(category_ranges) + 1) * 1000 - 1
    category_ranges[category] = range(start, end)

category_names = list(pokemon_data.keys())

name_to_id = {}

for category, pokemons in pokemon_data.items():
    category_range = category_ranges.get(category)
    name_to_id.update({pokemon: i for i, pokemon in zip(category_range, pokemons)})

id_to_name = {i: pokemon for pokemon, i in name_to_id.items()}

