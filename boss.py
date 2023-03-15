from random import randint
import time
def boss(a,b):
    if b <= 0:
        print("You were killed")
        time.sleep(2)
        print('You lost. Run the Module to play again.')
        quit()
    if a <= 0:
        print('You killed the Werewolf!')
        time.sleep(4)
        print()
        print('With the end of the path in sight.')
        time.sleep(2)
        print()
        print('You trek on to the neighboring village.')
        time.sleep(2)
        print()
        print('You won the Demo!')
        quit()
    if a and b > 0:
        a = a
        b = b    
        time.sleep(2)
        print('You: ' + str(b) +" Werewolf: " +str(a))
        turn(a,b)   
def turn(a, b):
    print("Menu:")
    print('1. Attack')
    print('2. Spell')
    miss_chance = randint(1,100)
    this = input()
    try:
        if int(this) == 2:
            return spell(a,b)
        if int(this) == 1:
            print('You attack.')
            yourMiss(a,b)
    except:
        print('Select a valid option.')


#monster(100,100)
def spell(a,b):
    a = a
    b = b
    print('Spell List: ')
    print('1. Fireball')
    this = input()
    if int(this) == 1:
        print("You cast Fireball!")
        misspell = randint(1,100)
        if misspell <= 100:
            time.sleep(2)
            print("It hit!")
            time.sleep(2)
            print('The Werewolf is set ablaze!')
            c = a - 50
            miss(c,b)
        else:
            time.sleep(2)
            print("You missed!")
            miss(a,b)




##### MISS SECTION #####



def yourMiss(a,b):
    miss_chance = randint(1,100)
    your_chance = randint(1,100)
    if miss_chance <= 5:
            print('You miss')
            #c = a
            #d = b
            return miss(a,b)
    else:
        c = a - 10
        d = b
        return miss(c,d)

def miss(a,b):
    your_chance = randint(1,100)
    time.sleep(1)
    print('The Werewolf lunges at you.')
    time.sleep(2)
    if your_chance <= 25:
                print("The Werewolf missed!")
                return boss(a,b)
    else:       
                print('You were struck')
                c = a
                d = b - 15
                return boss(c,d)

#####################################
