import discord
from typing import Dict, Set

import finders.data
from finders import data

class Player:
    user: discord.User
    enable_categories: Dict[int, bool]
    bw_per_cat: Dict[int, Set[int]]  # black or white list

    def __init__(self, user: discord.User, all: bool):
        self.user = user
        for i in range(len(data.category_names)):
            self.enable_categories[i] = all
            self.bw_per_cat[i] = set()

    def interested(self, pkmn_id: int) -> bool:
        category = data.get_category(pkmn_id)
        if self.enable_categories.get(category):
            return pkmn_id not in self.bw_per_cat.get(category)
        else:
            return pkmn_id in self.bw_per_cat.get(category)

    def set_preference(self, argument: str, enable: bool) -> bool:
        changed = False
        if argument == 'all':
            if (not enable) in self.enable_categories.values() or not all(not s for s in self.bw_per_cat.values()):
                changed = True
            for k in self.enable_categories.keys():
                self.enable_categories[k] = enable
            for k in self.bw_per_cat.keys():
                self.bw_per_cat[k] = set()
            return changed

        try:
            index = data.category_names.index(argument)
            if self.enable_categories[index] != enable or self.bw_per_cat[index]:
                changed = True
            self.enable_categories[index] = enable
            self.bw_per_cat[index] = set()
            return changed

        except ValueError:
            pkmn_id = finders.data.name_to_id(argument)
            pkmn_cat = finders.data.get_category(pkmn_id)
            if self.enable_categories.get(pkmn_cat) == enable:
                if pkmn_id in self.bw_per_cat[pkmn_cat]:
                    return False
                else:
                    self.bw_per_cat[pkmn_cat].add(pkmn_id)
                    return True
            else:
                if pkmn_id not in self.bw_per_cat[pkmn_cat]:
                    return False
                else:
                    self.bw_per_cat[pkmn_cat].remove(pkmn_id)
                    return True
