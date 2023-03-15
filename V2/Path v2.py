#Path ReWrite Door to Tomorrow


### Monster Lists
villageSpawn = {"Slime":{"hp":100,"def":0, "atk":10},"Thief":{"hp":100,"def":0, "atk":10}}


class Path:
    travel = 0



####


### Path Objects
## In Path Object, Boss Monster/Monsters/Completion Point
##Boss drops and item upon defeat and appends it to the inventory



    def __init__(self, name, boss, monsters, length):
        self.name = name
        self.boss = boss
        self.monsters = monsters
        self.length = length
   

village = Path("village","Werewolf",villageSpawn,100)

print(village.monsters.get("Slime"))
travel = village.travel + 10
print(travel)
## Consider making a DAO for easy updating.


##Google the mechanics behind DLC


##Main Menu
## Include ability to add in name, and have base stats, and classes.


## Items
##Item Types
##Inventory and Carried items

###Carried Items, only one item type can be equipped at a certain time
##Offensive, Defensive, Helmet,Gauntlet, Boot, Torso, Pants


##Shop appends to inventory, and subtracts from gold
##Upon Instantiation it populates with different weapon types


#Combat takes from mana and hp and item damage
## Implement defense calculations. Make a math equation for that
##Item damage does flat damage based on item

###Possible idea is weapons having a damage multiplier against the base attack damage


##Unequip damage scales with level for novelty sake


##Navigation

##Select one of three doorways/paths and go toward a maximum distance
##Upon reaching maximum distance you encounter the boss
##Boss drops an item
