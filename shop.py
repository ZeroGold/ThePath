from item import Item
import testInventory
import gold
class Shop:
    def __init__(self):
        self.contents = []
    def populateStore(self):
        item1 = Item("Sword","1H",10,20)
        item2 = Item("Longsword","1H",15,40)
        item3 = Item("Silver Sword","1H",20,50)
        item4 = Item("Hero Sword","1H",25,100)
        add = [item1,item2,item3,item4]
        self.contents = add
    def buy(self, a, b, inventory):
        if gold.gold <= 0:
            print("Cant Buy. Not enough gold")
        else:
            c = gold.gold - int(a.value)
            print("YOU BOUGHT: " + a.name)
            inventory.add(a)
            gold.gold = c
    def main(self,a,b):
        self.populateStore()
        print("What would you like to buy?")
        for i in range(len(self.contents)):
            print(str(i+1) +": "+ self.contents[i].name)
        #while gold.gold > 0:
        this = input()
        if int(this) >= 0:
            self.buy(self.contents[int(this)-1],a,b)
    def exit(self):
        print("You go about your way.")

#i = Inventory()
#gold.gold = 100
#s = Shop()
#s.main(gold.gold,i)
#i.printItems()
#print(gold.gold)



#####
#g = Gold()
#i =  Inventory()
#store = Shop()
#g.setGold(100)
#store.populateStore()
#for items in store.contents:
#    print(items.name)
#print(store.contents[3].name)
#print(store.buy(store.contents[3],g,i))
#print(g.getGold())
#i.printItems()
#if i.inventory[0].name == "Hero Sword":
#    print("CRIT!")



        
### Implement Gems.
