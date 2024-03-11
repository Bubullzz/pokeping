from parser import name_to_id, id_to_name, category_names
from typing import List

pkmn_names: List[str] = [name.lower() for name in name_to_id.keys()]

def get_category(id: int):
    return id // 1000

def get_id(pkmn_name: str):
    return name_to_id[pkmn_name]