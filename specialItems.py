#code for special items enemy is sometimes passed when not necessary as it is simpler
def SPItilde_key(player,enemy):
    print("input break to exit")
    answer = ""
    while answer != "break":#proper bodeged solution fix later (maybe)
        try:
            exec(answer)
            answer = input(">>> ")
        except Exception as e:
            print(e)

def SPIhealth_swap_scroll(player,enemy):
    player.health,enemy.health = enemy.health,player.health
    print("health swapped")

def SPImaxhp_up(player,enemy):
    boost = int(player.maxHealth * 0.3)
    player.maxHealth += boost
    player.Health += boost
    print("your maxHP has been increased by 30%")

def SPIcoin_sacrifice(player,enemy):#unknown side effects fix later
    if player.money == 0:
        print("you have no money to sacrifice")
        return
    while True:
        try:
            answer = int(input("you have "+str(player.money)+" coins\nhow much are you willing to lose?\n>>> "))
            if answer > player.money:
                print("you do not have enough money")
            else:
                enemy.health += -answer
                player.money += -answer
                print("your wealth and enemy wither in unison")
                break
        except ValueError:
            print("answer with a number")

def SPIitem_cloner(player,enemy): # doesnt work fix later
    from general import valInput
    print("select item to be copied")
    player.itemList.remove("item cloner")#item needs to not show up in item choice
    player.itemList.append(valInput(player.itemList))
    player.itemList.append("item cloner")#item needs to be present to be removed in later script

#build dictionary to associate properly formatted item names with functions
nameDict ={}
for i in dir():
    if i[:3] =="SPI":
        nameDict[i[3:].replace("_"," ")] = i

