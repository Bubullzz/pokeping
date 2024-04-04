import discord
from typing import Dict, Set
import finders.data
from finders import data

class Player:
    def __init__(self, user_id: int, user_mention: str, all: bool):
        self.user_id: int = user_id
        self.mention: str = user_mention
        self.enable_categories: Dict[int, bool] = {}
        self.bw_per_cat: Dict[int, Set[int]] = {}
        self.guild_to_chans: Dict[int, Set[int]] = {}

        for i in range(len(data.category_names)):
            self.enable_categories[i] = all
            self.bw_per_cat[i] = set()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "mention": self.mention,
            "enable_categories": self.enable_categories,
            "bw_per_cat": {str(cat): list(channels) for cat, channels in self.bw_per_cat.items()},
            "guild_to_chans": {str(guild): list(channels) for guild, channels in self.guild_to_chans.items()}
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['user_id'], data['mention'], False)  # Here, you might need additional data for initialization
        player.mention = data['mention']
        player.enable_categories = {int(k): v for k, v in data['enable_categories'].items()}
        player.bw_per_cat = {int(cat): set(channels) for cat, channels in data['bw_per_cat'].items()}
        player.guild_to_chans = {int(guild): set(channels) for guild, channels in data['guild_to_chans'].items()}
        return player

    def interested(self, pkmn_id: int, interaction: discord.Interaction) -> bool:
        category = data.get_category(pkmn_id)

        if interaction.channel.id not in self.guild_to_chans[interaction.guild.id]:
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
