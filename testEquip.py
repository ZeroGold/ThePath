import testInventory
from item import Item


item1 = Item("Sword","sturdy",10,20)

a = "lol"
b = "this and that"
testInventory.inventory.append(a)
testInventory.inventory.append(b)
testInventory.inventory.append(item1)
for items in testInventory.inventory:
    print(items)
