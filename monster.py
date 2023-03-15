#from item import Item
from random import randint
import time
from setVar import var
from tkinter import *
from mana import Mana
#### BUTTONS
interface = Tk()
var = var()
#frame = Frame(interface)
#frame.pack()
m = Mana()
text = Label(text="Placeholder")
text2 = Label(text="I don't know how you saw this.")
text3 = Label(text="Nothing")
button = Button(interface,text="Creator Button",command = lambda:doThis(1))
button2 = Button(interface,text="Placeholder",command = lambda:doThis(2))
interface.geometry('480x320')
interface.withdraw()
def doThis(x):
        var.setVar(x)
        interface.quit()
    #BUTTON SPACE
def window():
    interface.deiconify()
    interface.mainloop()
def deButton():
    button.pack_forget()
    button2.pack_forget()
    interface.update()
def buttons():
    button.configure(text="Attack", command = lambda:doThis(1))
    button2.configure(text="Spell", command= lambda:doThis(2))
    button.grid(row = 0, column = 6, padx = 100, pady = 250)
    button2.grid(row = 0, column = 10, padx = 30,pady = 250)
    
def spellButtons():
    button.configure(text="Fireball", command = lambda:doThis(1))
    button2.configure(text="Back", command= lambda:doThis(2))
    button.grid(row = 0, column = 6, padx = 100, pady = 250)
    button2.grid(row = 0, column = 10, padx = 30,pady = 250)
    
def battleScreen(a,b):
        text.configure(text="Your Health: " + str(a), font=20)
        text2.configure(text="Monster Health: "+ str(b), font=20)
        text.place(x=70,y=100)
        text2.place(x=70,y=40)
def battle():
        text3.configure(text="Battling...")
        text3.place(x=70, y=200)

def clear():
        text3.configure(text=" ")

        
























def monster(a,b):
    if b <= 0:
        interface.destroy()
        print("You were killed")
        quit()
    if a <= 0:
        interface.withdraw()
        print('You killed the monster')
    if a > 0:
        a = a
        b = b    
        time.sleep(2)
        battleScreen(b,a)
        print('Health: ' + str(b) +" Monster Health: " +str(a))
        print()
        turn(a,b)





        
def turn(a, b):
    print("Menu:")
    print()
    print('1. Attack')
    print()
    print('2. Spell')
    print()
    buttons()
    window()
    #try:
    if var.getVar() == 2:
            deButton()
            return spell(a,b)
    if var.getVar() == 1:
            print('You attack.')
            print()
            battle()
            deButton()
            yourMiss(a,b)
            
    #except:
    #    print('Select a valid option.')


#monster(100,100)
def spell(a,b):
    var.setVar(0)
    a = a
    b = b
    print('Spell List: ')
    print()
    print('1. Fireball')
    print()
    spellButtons()
    window()
    if var.getVar() == 1:
        print("You cast Fireball!")
        print()
        misspell = randint(1,100)
        battle()
        deButton()
        if m.canCast == True:
                m.cast()
                if misspell <= 70:
                    time.sleep(2)
                    clear()
                    print("It hit!")
                    print()
                    c = a - 40
                    if c > 0:
                        miss(c,b)
                        
                    else:
                        print(m)
                        monster(c,b)
                
                else:
                    time.sleep(2)
                    clear()
                    print("You missed!")
                    print()
                    miss(a,b)
        else:
                turn(a,b)
    if var.getVar() == 2:
        return turn(a,b)



##### MISS SECTION #####



def yourMiss(a,b):
    miss_chance = randint(1,100)
    your_chance = randint(1,100)
    time.sleep(2)
    if miss_chance <= 5:
            clear()
            print('You miss')
            print()
            #c = a
            #d = b
            return miss(a,b)
    else:
        clear()
        print('Hit!')
        print()
        c = a - 10
        d = b
        if c > 0:
                return miss(c,d)
        if c <= 0:
                return monster(c,b)

def miss(a,b):
    your_chance = randint(1,100)
    time.sleep(1)
    print('The monster attacks!')
    print()
    time.sleep(2)
    if your_chance <= 25:
                print("The monster missed it's attack!")
                print()
                return monster(a,b)
    else:       
                print('You were struck')
                print()
                c = a
                d = b - 10
                return monster(c,d)











#####################################

#ITEM WORKSPACE
#item1 = Item("Silver Sword","shiny")
#item2 = Item("Bow", "sturdy")



