#modules
import general as g
import manageSaves
import combatGame
import floors
import random

#classes
import items

#build character class
class character(items.items):
    def __init__(self,name,health,maxHealth,baseAttack,money,strength,intelligence,luck,itemList,floorNo):
        self.name,self.health,self.maxHealth,self.baseAttack,self.money=name,health,maxHealth,baseAttack,money
        self.strength,self.intelligence,self.luck=strength,intelligence,luck
        self.itemList,self.floorNo=itemList,floorNo
    #between room break code
    def reflect(self):
        #output player data
        g.asciiPrint("assets\\OTHER\\FIRE\\ascii.txt")
        print("\nBefore you reach the next level you reflect on your progress")
        print("\n HP:", self.health , "/", self.maxHealth)
        print(" DamageOutput:", self.baseAttack)
        print(" Money:", self.money)
        print(" Items:", self.itemList)
        print(" strength:",self.strength)
        print(" intelligence:",self.intelligence)
        print(" luck:",self.luck)
        print(" Floor:", self.floorNo,"\ncontinue on your journey?")
        #get player input
        while True:
            if g.valInput(["continue","use items"]) == "use items":
                self.useItem()
            else:
                break

#read/create instance of character
if g.valInput(["load save","new game"]) == "load save":
    try:
        player = character(*manageSaves.read())
    except Exception as e:
        print(e)
        print("no save game found, creating new game\n")
        player = character(*manageSaves.create())
else:
    player = character(*manageSaves.create())
g.asciiPrint("assets\\OTHER\\TOWER\\ascii.txt")
input("\nYou approach the tower and enter the first floor")

#Generate next floors
def genFloors(luck):
    mod = int(luck/2)
    floorTypes = [floors.genFreeLoot, floors.randomEncounter,
                  floors.combat, floors.chestMimic]
    floorOdds = [10+mod, 35+mod, 85+mod, 100]
    nextFloors = []
    for x in range(4):
        floorRNG = random.randint(0,100)
        for i in range(len(floorOdds)):
            if floorRNG <= floorOdds[i]:
                nextFloors.append(floorTypes[i])
                break
    return(nextFloors)

    
                    #GAME BEGIN

while True:
    #gen and print enxt 4 floors
    nextFloors = genFloors(player.luck)
    #print floors (debug code)
    print("next floors:")
    for i in nextFloors: 
        print("   ",str(i))

    #run all generated floors
    for runFloor in nextFloors:
        runFloor(player)

        #check if player is dead
        if player.health <= 0:
            print("\nyou are dead congratulations:\n")
            #print Obituary
            print(" You made it to floor number",player.floorNo)
            print(" you amassed ", player.money, "coins")
            input("press enter to exit")
            #exit game
            from sys import exit
            exit()
            
        #reflect and enumerate floorNo
        input("\nPress enter to continue")
        player.reflect()
        player.floorNo += 1

    #Shop Checkpoint
    floors.shop(player)
    player.reflect()
    print("due to racial discrimination you are unable to use the shop")#message no longer needed remove -fix later 
    player.floorNo += 1

    #save or continue game
    if g.valInput(["save and exit","continue game"]) == "save and exit":
        manageSaves.updateSaveData([*player.getData()])
        break

