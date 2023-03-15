from random import randint
class Monster:
    def __init__(self, name = None, hp = None, dmg = None):
        self.name = name
        self.hp = hp
        self.dmg = dmg




monsters = []

Cat =  Monster()

Cat.name = "Cat"
Cat.hp = 150
Cat.dmg = 10


Frog =  Monster()

Frog.name = "Frog"
Frog.hp = 100
Frog.dmg = 10



Dog =  Monster()

Dog.name = "Dog"
Dog.hp = 200
Dog.dmg = 20



monsters.append(Dog)
monsters.append(Cat)
monsters.append(Frog)








### RANDOM GENERATOR








def randomMonster():
    Monsters = {"name":["Frog","Cat","Dog"],"hp":[100,150,200],"dmg":[10,15,20]}
    x =  Monsters["name"][randint(0,len(Monsters["name"])-1)]
    y =  Monsters["hp"][randint(0,len(Monsters["hp"])-1)]
    z =  Monsters["dmg"][randint(0,len(Monsters["dmg"])-1)]
    monst = Monster(x,y,z)
    return monst
x = randomMonster()
print(x.name)




a = dict()
b = {"lol",123}

a[1] = b
print(a[1])




#####
Location dictionary
Monsters at location
Sub divisions of their stats

Location Dict{Location:MonsterDict{name:[],hp:[],dmg:[]}}
