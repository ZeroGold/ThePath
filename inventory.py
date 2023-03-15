from item import Item
class Inventory:
    def __init__(self):
        self.inventory = []
    def add(self, a):
        self.inventory.append(a)
    def equipItem(self):
        for item in self.inventory:
            item.equip()
            self.inventory.remove(item)
            return item
    def unequipItem(self):
        for item in item.carry:
            item.unequip()
            self.inventory.append(item)
    def printItems(self):
        for items in self.inventory:
            print(items.name)
    




#i = Inventory()

#print(i.inventory)

#item = Item("sword","sturdy",13,20)

#i.add(item)
#i.printItems()

#i.equipItem()
#print(i.inventory)
#print(item.carry)
#print(item.equipped)
#i.unequipItem(item)
#print(i.inventory)
#print(item.equipped)
#print(item.carry)
