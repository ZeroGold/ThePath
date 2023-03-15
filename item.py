from carry import carry
class Item:
        #run in item type
        #carry needs to go on a character class
        def __init__(self, name, iType, damage, value):
                self.name = name
                self.iType = iType
                self.damage = damage
                self.equipped = bool()
                self.value = value
        def summon(self):
                print("You summoned a " + self.name + " and it is " + self.attribute)
        def equip(self):
                self.equipped = True
                print("Equipped "+self.name)
                for items in carry:
                        if items.iType == self.iType:
                                print("Unequipped "+ items.name)
                                items.unequip()
                carry.append(self)
                #if another item.equipped = True
                #return cannot equip
        def unequip(self):
                self.equipped = False
                carry.remove(self)

        def attack(self, a):
                #check item type
                #if item is weapon
                #calculate damage
                if self.equipped == True:
                        b = a + self.damage
                        return b
                else:
                        print("No Item Equipped")
                        return a


item1 = Item("sword1","1H",20,20)
item2 = Item("sword2","1H",25,20)

item1.equip()
item2.equip()
for items in carry:
        print(items.name)

for items in carry:
        print(items.attack(10))
        







                


