from enum import Enum

class CategoryName(Enum):
    LVL4 = 4,
    LVL5 = 5,
    LVL6 = 6,
    OTHER = 7

class Category:
    name: CategoryName