import general as g
import random
import combatGame

'''basic random encounter'''

#Riddle Encounter
def encCHAD(player): #charStatsC = randomEncounter(charStatsC)
    g.asciiPrint("assets\\OTHER\\CHAD\\ascii.txt")
    print("riddle me this\n when threatened I cry six million\nfrom the pentagon I take billions\nWhat am I?")
    if g.valInput(["jew","gypsy","your mother","i shant answer"]) == "jew":
        print("correct")
        player.health += 64
    else:
        player.health = 1
        print("perish, shill")
        print("you barely escape with your life")

#LORD SHREK Encounter
def encSHREK(player):
    g.asciiPrint("assets\\OTHER\\LORD SHREK\\NORMAL\\ascii.txt")
    print("\nHe stands watching")
    answer = g.valInput(["pray","avoid","challenge"])
    if answer == "pray":
        print("you pray to shrek")
        if player.strength > 7:
            player.health+= 30
            player.maxHealth += 30
            print("your soul feels lighter, you gained 30 HP")
        else:
            player.health += -10
            player.maxHealth += -10
            print("shrek senses your weakness and kicks you in the balls\n you lose 10 HP")
    elif answer == "avoid":
        print("you give shrek a wide berth, his gaze follows you")
    else:
        g.asciiPrint("assets\\OTHER\\LORD SHREK\\BATTLE\\ascii.txt")
        combatGame.combatMini(player,combatGame.enemy(400,20,"Assets\\OTHER\\LORD SHREK\\BATTLE"))
        if player.health > 0:
            player.addSpecific("excalibur")

#FNV Encounter
def encFNV(player):
    g.asciiPrint("assets\\OTHER\\FNV\\ascii.txt")
    print("\nyou find an arcade machine for FALLOUT: New Vegas\n a game costs 19 coins")
    if g.valInput(["play","dont play"]) == "play":
        if player.money < 19:
            print("you are too poor")
        else:
            player.money += -19
            player.health = player.maxHealth
            print("you feel replenished, your HP has been filled")
    else:
        print("you continue your journey the same underdeveloped creature you began it as")
        
#ToryWizard Encounter
def encToryWizard(player):
    g.asciiPrint("assets\\OTHER\\TORYWIZARD\\ascii.txt")
    print("\nyou find a wizard who unfortunately turns out to be a tory")
    print("using sheer incompetency this powerful warlock is capable of unleashing")
    print("economic devestation on the poor")
    answer = g.valInput(["ask for help","challenge","avoid"])
    if answer == "ask for help":
        if player.money > 120:
            print("the wizard offer to upgrade a single permanent stat")
            stat = g.valInput(["strength","intelligence","luck"])
            if stat == "strength":
                print("may you crush many a council house")
                player.strength += 1
            elif stat == "intelligence":
                print("may you found a real politcial party")
                player.intelligence += 1
            else:
                print("BIIIIIIIIIITCOOOOOIIIIIIIIN.......INVEEEEEST")
                player.luck += 1
        else:
            print("the tory bastard takes what is left of you money")
            player.money = 0
    elif answer == "challenge":
        print("you challenge the tory wizard on his off shore bank accounts\n whilst fleeing he drops a large sum of money")
        player.money += random.randint(40,98)
    else:
        print("you avoid eye contact with the demi-human and carry on up the tower") 

#Companion Cube Encounter
def encCUBEY(player):
    g.asciiPrint("assets\\OTHER\\CUBEY\\ascii.txt")
    check = False
    print("\nThe door to the towers next level is locked")
    print("You see a happy looking cube next to an incinerator")
    while True:
        print("Piecing the situation together you:\n")
        if g.valInput(["subjucate the cube in hellfire", "refuse the situation"]) != "refuse the situation":
            if check != True:
                print("\nYou are truly evil, you gain a damage buff with your current weapon\n keep it up killer")
                player.baseAttack += 2
                break
            else:
                print("\nyour moral stance on murder weakened you decide to kill the ever trusting cube\n you feel more numb to pain and suffering, as a result your max HP has increased by 15")
                player.health += 15
                player.maxHealth += 15
                break
        check = True

def encSecretRoom(player):
    doorHealth = 100
    g.asciiPrint("assets\\OTHER\\SECRET\\closed.txt")
    
    while True:
        answer = g.valInput(["unlock the door","kick the door","knock the door","leave"])
        if answer == "kick the door":
            doorHealth += - player.strength**1.6 #uses exponent so strength is very important
            player.health += -30
            print("the door cracks, so does your foot on the door. you lose 30 health")
            if player.health <= 0:
                print("you briefly ponder as to whether you should have done that")
                break
            if doorHealth <= 0:
                g.asciiPrint("assets\\OTHER\\SECRET\\open.txt")
                input("the door opens")
                g.asciiPrint("assets\\OTHER\\CHEST\\ascii.txt")
                if g.valInput(["open","leave"]) == "open":
                    player.addRandom(3)
                else:print("you left the chest")
                break
        elif answer == "knock the door":
            from manageDB import shopListReturn
            g.asciiPrint("assets\\OTHER\\SECRET\\merchant.txt")
            item = random.choice(shopListReturn(4))
            cost = player.appraise(item)[3]
            print("could I interest you in a",item,"to brighten up your day?\n only",str(cost),"coins")
            if g.valInput(["yes","no"]) == "yes":
                if player.money >= cost:
                    player.money += -cost
                    player.addItem(item)
                    print("a pleasure doing business")
                else:print("you are too poor and thus we have nothing left to discuss\n             *slam*")
            else:
                print("then we have nothing else to discuss\n       *slam*")
            break
        #secret boss fight
        elif answer == "unlock the door":
            while True:
                #padlock code
                g.asciiPrint("assets\\OTHER\\SECRET\\padlock.txt")
                print("the door is locked if you decide to employ an item to unlock it")
                item = g.valInput(player.itemList+["leave"])
                if item == "large key":
                    g.asciiPrint("assets\\OTHER\\SECRET\\open.txt")
                    input("you slowly enter the door")
                    #start boss fight
                    g.asciiPrint("assets\\OTHER\\SECRET\\BOSS\\ascii.txt")#boss assets not complete (fix later)
                    combatGame.combatMini(player,combatGame.enemy(1000,50,"Assets\\OTHER\\SECRET\\BOSS"))
                    if player.health > 0:
                        print("you find a strange charm in the palm of your hand")
                        player.addItem("tilde key")
                    return
                elif item == "leave":
                    print("you decide nothing you have will work")
                    break
                else:
                    print("you broke the",item,"by ramming it in the lock")
                    player.itemList.remove(item)
        else:
            print("""as you leave you notice a carving on the door that reads "approximate the integer" """)
            return






    
'''gambing encounter code'''

#gambing room encounter
def encGamblingRoom(player):
    g.asciiPrint("assets\\OTHER\\GAMBLING\\cashier.txt")
    while True:
        print("would you like to play a game")
        answer = g.valInput(["sevens golden minefield","game2","guessing game","rules","leave"])
        #code to get and run bet for sevens golden minefield
        if answer == "sevens golden minefield":
            if player.money > 0:
                #validate input in range of available money
                while True:
                    try:
                        print("how large a bet would you like to place you have",player.money,"coins")
                        bet = int(input(">>> "))
                        if bet > 0 and bet <= player.money:
                            break
                        else:
                            print("number outwith specified range")
                    except:
                        print("please input a number")
                sevensGoldenMinefield(player,bet)
            else:
                print("you need money to gamble")
        #code to get and run bet for game2
        elif answer == "game2":
            print("you play airhockey")
        #code to get and run bet for guessing game
        elif answer == "guessing game":
            if player.money > 100:
                guessingGame(player)
            else:
                print("you must bet 100 coins (you are too poor)")
        #code to get rules for specified game
        elif answer == "rules":
            answer = g.valInput(["sevens golden minefield","game2","guessing game"])
            switchDict = {"sevens golden minefield":"sevensGoldenMinefieldRules.txt",
                          "game2":"othergame.txt",
                          "guessing game":"GuessTheNumberRules.txt"}
            g.asciiPrint("assets\\OTHER\\GAMBLING\\"+switchDict[answer])
        else:
            break

#Gambling room encounter
class card_error(Exception):
    pass

#class for storing each card
class card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        if not suit in ("clubs","diamonds","spades","hearts") or not value in ["ace","jack","queen","king"]+list(range(2,11)):
            raise card_error("irregular card declared >>> "+str(self.value)+" of "+str(self.suit))            
    def __repr__(self):
        return str(self.value)+" of "+self.suit
    def __str__(self):
        return str(self.value)+" of "+self.suit
    def __int__(self):
        valueDict = {"ace":1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"jack":11,"queen":11,"king":11}
        return valueDict[self.value]
    def __eq__(self,notSelf):
        if str(self) == str(notSelf):return True
        return False
    def __lt__(self,notSelf):
        if int(self) < int(notSelf):return True
        return False

#class for declaring new deck
class newDeck:
    def __init__(self):
        cards = []
        for i in ("clubs","diamonds","spades","hearts"):
            cards.append(card(i,"ace"))
            for n in range(2,11):
                cards.append(card(i,n))
            for n in ("jack","queen","king"):
                cards.append(card(i,n))
        self.cards = cards
    #basic deck modifying actions
    def shuffle(self):
        for i in range(len(self)):
            n = random.randint(0,len(self)-1)
            self.cards[i],self.cards[n] = self.cards[n],self.cards[i]
    def split(self,number):
        if len(self) <= number:
            raise card_error("empty card deck")
        else:
            self.cards = self.cards[:number]
    def removeFace(self):
        lst = []
        for i in self.cards:
            if type(i.value) == str:
                lst.append(i)
        if len(lst) > 1:
            self.cards.remove(random.choice(lst))
            return
        print("you are feeling lucky enough")
    #sort cards by value using insertion sort
    def order(self):
        #bubble sort sort here
        for i in range(len(self)):
            for x in range(len(self)-i-1):
                if self.cards[x] > self.cards[x+1]:
                    self.cards[x],self.cards[x+1] = self.cards[x+1],self.cards[x]           
    #useful builtins
    def __iter__(self):
        self.i = -1
        return self
    def __next__(self):
        if self.i < len(self)-1:
            self.i += 1
            return self.cards[self.i]
        raise StopIteration
    def __len__(self):
        return len(self.cards)
    def __add__(self,notSelf):
        self.cards = self.cards + notSelf.cards

#sevens golden minefield game code - low risk game
def sevensGoldenMinefield(player,bet):
    #game setup
    player.money += - bet
    total,mult = 0,bet//20
    deck = newDeck()
    deck.shuffle()
    #remove face cards for player luck
    for i in range(player.luck//3):#balance doesnt work fix later
        deck.removeFace()
    deck.split(7)
    deck.order()

    #game begin
    ui = ["???"]*7
    for i in range(7):
        print(" | ".join(ui),"\n pick a new card?")
        if g.valInput(["yes","no"]) =="no":
            player.money += total
            print("you made",total,"money")#lame fix later
            return
        else:
            x = deck.cards.pop(0)
            if x.value in ("jack","queen","king"):
                player.money += -total+bet
                print("mine struck you lost",total,"money")#lame fix later
                return
            ui[i] = str(x)
            total += mult*int(x)
            print("> you got a",str(x),"your pot is now",total)
    print("very brave")#lame fix later
    player.money += total
    print("you made",total,"money")#lame fix later
    
#guess the number game
def guessingGame(player):
    loss = 0
    while player.money >= 100:
        if loss > 1500-player.luck*50:
            print("congratulations you got a special item")
            player.addItem("large key")
            return
        print("guess the number")
        g.valInput(["1","2","3"])
        print("wrong, play again?")
        player.money += -100
        loss += 100
        if g.valInput(["yes","no"]) == "no":
            break
    print("you lost",loss,"money")
        



