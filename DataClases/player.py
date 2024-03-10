import discord
from typing import Dict, Set
from finders import data

class Player:
    user: discord.User
    enable_categories: Dict[int, bool]
    bw_per_cat: Dict[int, Set[int]]  # black or white list

    def interested(self, pkmn_id: int) -> bool:
        category = data.get_category(pkmn_id)
        if self.enable_categories.get(category):
            return pkmn_id in self.bw_per_cat.get(category)
        else:
            return pkmn_id not in self.bw_per_cat.get(category)