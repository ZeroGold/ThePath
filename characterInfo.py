from item import Item

atk = 10
hp = 100
dfz = 10
magic = 20
carrying = []
def itemCheck(item):
    onHand = True
    for i in range(len(carrying)):
        if str(carrying[i].name) == str(item.name):
                return onHand
def printContents():
    for items in carrying:
        print(items.name)
i = Item("Sword","sturdy",10,20)
carrying.append(i)

itemCheck(i)
printContents()
print(i.name)
print(itemCheck(i))

if itemCheck(i) == True:
    print("Item equipped!")

if itemCheck(i) == True:
    print("Cannot equip item")
