from finders import parser
from typing import List, Dict

pkmn_names: List[str] = [name for name in parser.name_to_id.keys()]
category_names = parser.category_names
pretty_to_id = parser.name_to_id
lower_to_id = {key.lower(): value for key, value in pretty_to_id.items()}
id_to_lower: Dict[int, str] = {i: pokemon for pokemon, i in lower_to_id.items()}

xable_list = pkmn_names + category_names + ["all"]
def get_category(id: int):
    return id // 1000


def get_id(pkmn_name: str):
    return lower_to_id[pkmn_name]