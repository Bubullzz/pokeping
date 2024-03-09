import discord
from AlertType import categories
from typing import Dict, Set


class Player:
    user: discord.User
    enable_categories: Dict[categories.Category, bool]
    bw_per_cat: Dict[categories.Category, int]  # black or white list
