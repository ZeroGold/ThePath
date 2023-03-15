from random import randint
monsters = {"Slime":{"hp":110,"atk":10,"mana":0},"Thief":{"hp":120,"atk":20},"Wild Dog":{"hp":120,"atk":15}}
randMonster = randint(0,3)
#print(randMonster)
#print(monsters["Slime"])
#print(monsters.get("Slime"))
#print(monsters.keys())
#print(sorted(monsters))
game = False
hp = 0
chosen = ""
if randMonster == 1:
    chosen = "Slime"
if randMonster == 2:
    chosen = "Thief"
if randMonster == 3:
    chosen = "Wild Dog"
for items in monsters:
    if items == chosen:
        hp += monsters[items]["hp"]
        print(chosen +" was summoned!")
        game = True




while game:
    
    this = input()
    if this == "1":
        hp -= 10
        print(str(hp)+" hp is left!")

