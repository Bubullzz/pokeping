from finders import parser
from typing import List

pkmn_names: List[str] = [name for name in parser.name_to_id.keys()]
category_names = parser.category_names
name_to_id = parser.name_to_id
id_to_name = parser.id_to_name

def get_category(id: int):
    return id // 1000


def get_id(pkmn_name: str):
    return parser.name_to_id[pkmn_name]