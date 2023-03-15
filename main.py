from tkinter import *
import distance
import boss
import time
from setVar import var
from chances import shortChance
from chances import medChance
from chances import longChance
import gold
from inventory import Inventory
interface = Tk()
boss_distance = 60
trvl = 0
var = var()
i = Inventory()
a = 0

#### print("Type what you want here, put {} <-- here. then .format the object").format("this")

#######
game = True      
#DEEP FUTURE: ADD WEAPONS, ADD DIFFERENT PATHS, ADD CLASSES
#THESE THINGS CAN BECOME DLC
#Pass the fight info into a pop-up menu
#Add buttons for each selection
#Add player name
#Adding a gold system???#
#time.sleep(2)
print("You're on the path.")
#time.sleep(3)
print('What do you do?')
#time.sleep(2)
print("1. Walk: Safest")
#time.sleep(2)
print('2. Jog: 50/50')
#time.sleep(2)
print("3. Run: Dangerous")
print()



#Intergrate carried items into battle system
frame = Frame(interface)
frame.pack()
button = Button(interface,text="Walk",command = lambda:doThis(1))
button2 = Button(interface,text="Jog",command = lambda:doThis(2))
button3 = Button(interface,text="Run",command = lambda:doThis(3))
button.pack()
button2.pack()
button3.pack()



def buttons():
        button.configure()

def doThis(x):
        var.setVar(x)
        interface.quit()
    #BUTTON SPACE
def window():
    interface.deiconify()
    interface.mainloop()
if __name__ == "__main__":        
        while game:
        ## BUTTON ON THE INSIDE?
            window()
            if trvl < boss_distance:
                if var.getVar() == 1:
                    trvl = distance.distance.short(trvl)
                    interface.withdraw()
                    shortChance(i)
                    gold.gold = int(gold.gold) + 20
                    i.printItems()
                    
                if var.getVar() == 2:
                    trvl = distance.distance.med(trvl)
                    interface.withdraw()
                    medChance(i)
                    gold.gold = int(gold.gold) + 25
                    
                if var.getVar() == 3:
                    interface.withdraw()
                    longChance(i)
                    trvl = distance.distance.long(trvl)
                    gold.gold = int(gold.gold) + 30
                print('Distance Traveled: ' + str(trvl))
                
            if trvl >= boss_distance:
                    time.sleep(2)
                    print('You near the end of the path.')
                    time.sleep(2)
                    print('Up ahead there is a figure in the darkness')
                    time.sleep(2)
                    print("IT'S A WEREWOLF!")
                    time.sleep(1)
                    print()
                    time.sleep(1)
                    print('! ! ! ENCOUNTER ! ! !')
                    boss.boss(250,100)
                    trvl = 0
                    
                    game = False
    

#print('You encountered the boss: The Werewolf')
# Make an encounter book for the various monsters you can meet.
        
