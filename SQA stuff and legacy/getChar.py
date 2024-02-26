#For reading in data from save file
def read():
    #Read in data to relevant variables and format
    f = open("Assets\\save.txt","r")
    statsB,statsP,playerItems,floorNo  = f.readlines()
    f.close()
    statsB,statsP,playerItems= statsB[:-1].split(","), statsP[:-1].split(","), playerItems[:-1].split(",")
    
    for i in range(3):
        statsP[i] = int(statsP[i])
        statsB[i+1] = int(statsB[i+1])
    statsB[4] = int(statsB[4])
    floorNo = int(floorNo)

    #Populate empty list to prevent crashes
    if playerItems == ['']:
        playerItems = []

    #DisplayerStats <==nice english dip shit
    print("\n  ---===CHARACTER STATS===---\n")
    print("\nName: ", statsB[0])
    print("Strength: ",statsP[0])
    print("Intelligence: ",statsP[1])
    print("Luck",statsP[2])
    print("HP: ", statsB[1],"/",statsB[2])
    print("RawDamage: ",statsB[3])
    print("Money: ",statsB[4])
    print("Items: ", playerItems)
    print("Floor: ", floorNo)
    input("Press enter to continue")
    return statsB,statsP,playerItems,floorNo

#For creating new Character
def create():
    print("welcome to your character creation")
    print(" first select your primary stats you have 12 points\n to spend on your strength, intelligence and luck\n a single stat may not exceed 10")

    #Get and validate player input
    statNames = ("strength","intelligence","luck") #use tuple cause im already upset at having to declare a list with only one purpose
    statsB,statsP,total = [input("whats your name")],[],12
    for i in range(len(statNames)):
        while True:
            try:
                answer = int(input("input value for your "+statNames[i]+" stat"))
                if sum(statsP) >= 10 or total == 0: #punish players for being mathematically inept
                    print("gg you cannot count so some stats have been defaulted to 1")
                    for x in range(len(statsP)) :
                        statsP[x] = 1
                        total = 1
                if answer > 10 or answer < 1:
                    print("stat must be between 10 and 1:")
                elif answer <= total:
                    statsP.append(answer)
                    total += -answer
                    print("points left to distribute:",total)
                    break
                else:
                    print("You dont have enough points")
            except:
                print("stat must be between 10 and 1:")

    #assign other values based on p type stats
    for i in range(2):
        statsB.append(20+(15*statsP[0])) #Max HP
    statsB.append(2) #Atk Dam
    statsB.append(10*statsP[1]) #Money
    print(statsB)
    playerItems = []
    floorNo = 1
    
    return(statsB,statsP,playerItems,floorNo)
    
                
    

















