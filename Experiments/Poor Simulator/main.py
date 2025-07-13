from Methods.Inventory import Inventory


if __name__ == '__main__':
    my_inventory = Inventory(5)
    my_inventory.add("Pipoca")
    print(my_inventory[0])