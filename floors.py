import random
import general as g
import manageDB
import combatGame
import randomEncounters

#free loot floor
def genFreeLoot(player):
    g.asciiPrint("assets\\OTHER\\CHEST\\ascii.txt")
    print("you see a chest do you open it?")
    if g.valInput(["open", "leave"]) == "open":
        if 5 > random.randint(0,12):
            lootMoney = random.randint(1+player.floorNo,10+player.floorNo)
            print("you found", lootMoney, "money")
            player.money += lootMoney
        else:
            player.addRandom(random.randint(1,4))#no luck fix later

#basic combat encounter event
def combat(player):
    from os import listdir
    combatant = random.choice(listdir("assets\\COMBATANTS"))
    #generate base enemy stats
    mod = int(player.floorNo/player.luck)
    health = random.randint(20+mod*4, 50+mod*4)
    attack = random.randint(1+mod*2, 10+mod*2)
    #start combat game
    g.asciiPrint("assets\\COMBATANTS\\"+combatant+"\\ascii.txt")
    print("\n",combatant, "blocks your ascension")
    combatGame.combatMini(player,combatGame.enemy(health,attack,"assets\\COMBATANTS\\"+combatant))

#mimic encounter
def chestMimic(player):
    g.asciiPrint("Assets\\OTHER\\CHEST\\ascii.txt")
    print("you see a chest do you open it?")
    if g.valInput(["open","leave"]) == "open":
        g.asciiPrint("assets\\OTHER\\MIMIC\\ascii.txt")
        #generate base enemy stats
        mod = player.floorNo//(player.luck/2)
        health = random.randint(20, 50+mod*4)
        attack = random.randint(1, 10+mod*2)
        #start combat game
        combatGame.combatMini(player,combatGame.enemy(health,attack,"assets\\OTHER\\MIMIC"))
        if player.health > 0:
            player.addRandom(3)
    else:
        print("you left the chest")

#random encounter fetching and running
def randomEncounter(player):
    #fetch encounters
    encList = []
    for i in dir(randomEncounters):
        if i[:3] == "enc":
            encList.append(i)
    #run random room from encList
    getattr(randomEncounters,random.choice(encList))(player)

#shop encounter
def shop(player):
    g.asciiPrint("assets\\OTHER\\SHOP\\ascii.txt")
    #CREATE BUY LIST
    itemList = manageDB.shopListReturn(3)
    buyList = [random.choice(itemList),
                   random.choice(itemList),
                   random.choice(itemList)]
    
    #begin shopping options
    while True:
        print("\nthe merchant looks at you with anticipation")
        print(" you have ", player.money, "coins on you yes? oh? I can tell from the sound")
        print(" my prices are as follows:\n")
        for i in buyList:
            print(i + ":", player.appraise(i)[3],"coins")
        print("")
        answer = g.valInput(buyList + ["sell","leave"])
        if answer == "leave":
            return
        #functions for selling items
        elif answer == "sell":
            print("\nWhich item do you wish to sell?")
            for i in player.itemList:
                print(i+": "+ str(player.appraise(i)[3]) + " coins")
            print("")
            soldItem = g.valInput(player.itemList+["none"])
            if soldItem != "none":
                if player.appraise(i)[3] == 0:
                    print("This item cannot be sold")
                else:
                    player.money += player.appraise(soldItem)[3]
                    player.itemList.remove(soldItem)
                    print("item sold for " + str(player.appraise(soldItem)[3]) + " coins")
        else:
            if player.appraise(answer)[3] <= player.money: #repeatedly calls function wont work with stat based prices fix later
                player.addItem(answer)
                player.money += -player.appraise(answer)[3]
                buyList.remove(answer)
            else:
                print("not enough money")
