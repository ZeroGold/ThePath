from monster import monster
from random import randint
from shop import Shop
import gold
from inventory import Inventory
s = Shop()
def shortChance(i):
    chance = randint(1,100)
    shopChance = randint(1,100)
    #calculate chances
    if shopChance <= 50:
        print("You run into a wandering salesman.")
        print("Do you want to look at his wares?  (Press y to Shop)")
        this = input()
        if this == "y":
            s.main(gold.gold,i)
        else:
            s.exit()
            
    if chance <= 25:
        print('! ! ! ENCOUNTER ! ! !')
        monster(100,100)

  
def medChance(i):
    chance = randint(1,100)
    if chance <= 50:
        print('! ! ! ENCOUNTER ! ! !')
        monster(100,100)


def longChance(i):
        print('! ! ! ENCOUNTER ! ! !')
        monster(100,100)



