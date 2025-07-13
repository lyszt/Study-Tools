import collections
from typing import Optional, List, Any


class Inventory:
    def __init__(self, inventory_size: Optional[int] = 0):
        self.inventory: List[Optional[Any]] = [None for _ in range(inventory_size)]

    def __getitem__(self, index):
        return self.inventory[index]

    def add(self, item):
        self.inventory.append(item)

    def __setitem__(self, index, value):
        if index >= len(self.inventory):
            raise IndexError
        self.inventory[index] = value