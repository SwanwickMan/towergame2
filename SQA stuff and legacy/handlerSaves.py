import manageDB
from general import valInput

#For reading in data from save file
def read():
    #Read in data to relevant variables and format
    data = manageDB.getAllSaves()
    while True:
        print("name: ")
        for i in data:
            print(" ",i[0])
        answer = valInput(list(list(zip(*data))[0]))
         #Displayer <==nice english dip shit
        for i in range(len(data)):
            if data[i][0]==answer:
                x = i
        print("\n  ---===CHARACTER STATS===---\n")
        print("\nName: ", data[x][0])
        print("Strength: ",data[x][5])
        print("Intelligence: ",data[x][6])
        print("Luck",data[x][7])
        print("HP: ", data[x][1],"/",data[x][2])
        print("RawDamage: ",data[x][3])
        print("Money: ",data[x][4])
        print("Items: ", data[x][8])#items incomplete
        print("Floor: ", data[x][9])
        if valInput(["continue","return"]) == "continue":
            return data[x]
        
#For creating new Character
def create():
    print("welcome to your character creation")
    print(" first select your primary stats you have 12 points\n to spend on your strength, intelligence and luck\n a single stat may not exceed 10")

    #Get and validate player input
    statNames = ("strength","intelligence","luck") #use tuple cause im already upset at having to declare a list with only one purpose
    statsV,statsP,total = [input("whats your name")],[],12
    for i in statNames:
        while True:
            try:
                answer = int(input("input value for your "+i+" stat"))
                if total == 0: #punish players for being mathematically inept
                    print("gg you cannot count so some stats have been defaulted to 1\n you may have to select one for your next stat")
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
        statsV.append(20+(15*statsP[0])) #Max HP
    statsV.append(2) #Atk Dam
    statsV.append(10*statsP[1]) #Money
    playerItems = []
    return statsV+statsP+[1]

#save data from current game to DB
def updateSaveData(saveData):
    connection=cc()
    cursor = connection.cursor()
    createPlayer = """
    Insert INTO
        SaveData (name, health,maxHealth)
    VALUES
        {};    """.format(saveData)
    updatePlayer = """
    UPDATE SaveData
    SET health=1,
    maxHealth=2
    WHERE name='test';    """
    try:
        cursor.execute(createPlayer)
        connection.commit()
        print("Query executed successfully")
    except:
        cursor.execute(updatePlayer)
        connection.commit()
        print("Query executed successfully")     
    connection.close()
    


















