from enum import Enum, auto
from typing import Set, List

rawCats = []
class RawCategories:
    name: str
    mons: List[str]

    def __init__(self, name, mons):
        self.name = name
        self.mons = mons
        rawCats.append[self]

RawCategories("lvl4",
              [
                "M_GENGAR",
                "M_GARDEVOIR",
                "M_CHARIZARD_X", ])

    




class Lvl4(Enum):
    M_GENGAR = auto(),
    M_GARDEVOIR = auto(),
    M_CHARIZARD_X = auto(),

class Lvl5(Enum):
    GIRATINA = auto(),
    RESHIRAM = auto(),
    PALKIA = auto(),
    DIALGA = auto(),
    ZEKROM = auto(),
    HEATRAN = auto(),

class Lvl6(Monster):
    P_GROUDON = auto(),
    M_RAYQUAZA = auto(),
    P_KYOGRE = auto(),
    M_LATIOS = auto(),
    M_LATIAS = auto()

class Monster(Enum):
    pass

#puts all the monsters from all the classes in Monster
types = {Lvl4, Lvl5, Lvl6}
for type in types:
    for mon in type:
        setattr(Monster, f"{mon.name}", auto())

class CategoryName(Enum):
    LVL4 = 4,
    LVL5 = 5,
    LVL6 = 6,
    OTHER = 7

class Category:
    name: CategoryName
    monster: Set[Monster]

level_4_category = 