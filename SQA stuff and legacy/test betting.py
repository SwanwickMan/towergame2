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
player = character("name",100,150,10,1000,6,6,6,["excalibur","lesser potion"],5)
enemy = combatGame.enemy(10,10,"Assets//COMBATANTS//a gay cat")

from random import randint
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
            n = randint(0,len(self)-1)
            self.cards[i],self.cards[n] = self.cards[n],self.cards[i]
    def split(self,number):
        if len(self) <= number:
            raise card_error("empty card deck")
        else:
            self.cards = self.cards[:number]
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
#bet = int(input("your bet here \n>>> "))
def sevensGoldenMinefield(player):
    #game setup
    bet = 200
    player.money += - bet
    total,mult = 0,bet//20
    deck = newDeck()
    deck.shuffle()
    deck.split(7)
    deck.order()
    deck.cards

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
                player.money += -total
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







#debug stuff
def add(base,*values):
    total = 0
    for i in values:
        total += base*i
    return total

#average card mult by move num
def averageStuff(num):    
    lst = []
    for i in range(1000):
        x=newDeck()
        x.shuffle()
        x.split(7)
        x.order()
        lst.append(sum([int(i) for i in x.cards][:num]))
    print(sum(lst)/1000)

#average occurence of face card
def averageStuff2():    
    lst = []
    for i in range(1000):
        x=newDeck()
        x.shuffle()
        x.split(7)
        x.order()
        counter = 0
        for n in x:
            if n.value in ("jack","queen","king"):
                lst.append(counter)
                break
            counter += 1
    print(sum(lst)/1000)






