#modules
import general as g
import manageSaves
import combatGame
import randomEncounters
import manageDB

#classes
import items

#build character class
class character(items.items):
    valInput = g.valInput
    def __init__(self,name,health,maxHealth,baseAttack,money,
                 strength,intelligence,luck,
                 itemList,floorNo):
        self.name,self.health,self.maxHealth,self.baseAttack,self.money=name,health,maxHealth,baseAttack,money
        self.strength,self.intelligence,self.luck=strength,intelligence,luck
        self.itemList,self.floorNo=itemList,floorNo
    def getPlayerInfo(self):
        return(self.name,self.health,self.maxHealth,self.baseAttack,self.money,
               self.strength,self.intelligence,self.luck,
               self.itemList,self.floorNo)
playerL = character("name",31,50,5,4,5,5,5,["a large rock"],5)
playerM = character("name",100,150,10,123,7,7,7,["regular potion","bomb"],15)
playerH = character("name",1000,1500,100,10000,9,9,9,["item cloner","coin sacrifice","large key"],30)
enemy = combatGame.enemy(10,10,"Assets//COMBATANTS//a gay cat")

#average card mult by move num
def averageStuff(num,player):    
    lst = []
    for i in range(10000):
        x=randomEncounters.newDeck()
        x.shuffle()
        x.split(7)
        x.order()
        lst.append(sum([int(i) for i in x.cards][:num]))
    print(sum(lst)/10000)

#average occurence of face card
def averageStuff2(player):    
    lst = []
    for i in range(10000):
        x=randomEncounters.newDeck()
        x.shuffle()
        x.split(7)
        x.order()
        counter = 0
        for n in x:
            if n.value in ("jack","queen","king"):
                lst.append(counter)
                break
            counter += 1
    print(sum(lst)/10000)






