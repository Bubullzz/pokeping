import discord
import categories
from typing import Dict, Set


class Player:
    user: discord.User
    enable_categories: Dict[categories.Category, bool]
    bw_per_cat: Dict[categories.Category, Set[categories.Monster]] #black or white list
