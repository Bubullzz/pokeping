import discord
from typing import Dict, Set
import finders.data
from finders import data

class Player:
    def __init__(self, user: discord.User, all: bool):
        self.user = user
        self.enable_categories: Dict[int, bool] = {}
        self.bw_per_cat: Dict[int, Set[int]] = {}
        self.guild_to_chans: Dict[int, Set[discord.TextChannel]] = {}

        for i in range(len(data.category_names)):
            self.enable_categories[i] = all
            self.bw_per_cat[i] = set()

    def to_dict(self):
        # Convert instance attributes to a dictionary
        return {
            'user_id': self.user.id,
            'enable_categories': self.enable_categories,
            'bw_per_cat': {key: list(value) for key, value in self.bw_per_cat.items()},
            'guild_to_chans': {key: [chan.id for chan in value] for key, value in self.guild_to_chans.items()}
        }

    @classmethod
    def from_dict(cls, user, data):
        # Create a new Player instance from a dictionary
        player = cls(user)
        player.enable_categories = data['enable_categories']
        player.bw_per_cat = {key: set(value) for key, value in data['bw_per_cat'].items()}
        player.guild_to_chans = {key: {discord.TextChannel(id=chan_id) for chan_id in value} for key, value in data['guild_to_chans'].items()}
        return player


    def interested(self, pkmn_id: int, interaction: discord.Interaction) -> bool:
        category = data.get_category(pkmn_id)

        if interaction.channel not in self.guild_to_chans[interaction.guild.id]:
            return False
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
            if argument not in data.lower_to_id:
                print(f"Unexpected argument: {argument}")
                return False
            pkmn_id = finders.data.lower_to_id[argument]
            pkmn_cat = finders.data.get_category(pkmn_id)
            if self.enable_categories.get(pkmn_cat) != enable:
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
