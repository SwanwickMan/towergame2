from random import choice
import general as g

class enemy:
    def __init__(self,health,attack,path):
        with open(path + "\\info.txt","r") as f:
            modifier = f.readline().strip().split(":")
        #modify values by character specific traits
        self.health=int(health*float(modifier[0]))
        self.attack=int(attack*float(modifier[1]))
        self.path=path
    enraged = False

#code for combat mini game
def combatMini(player,enemy):
    from random import randint
    name = enemy.path.split("\\")[-1]
    bideMult,dodgeMult = 1,1
    maxHP = enemy.health
    dodge = False
    critTurns = 0

    #try get taunt list
    try:
        with open(enemy.path+"\\info.txt","r") as f:
            tauntList = f.read().splitlines()[1:]
    except Exception as e:
        print(e)
        tauntList = []
    
    while True:
        #critTurn generation
        if critTurns == 0:
            critTurns = randint(0,4)
            print("crit in", critTurns+1,"turns")
        else:
            critTurns += -1
        #choose next move
        answer = g.valInput(["attack","dodge","bide","item","flee"])
        if answer == "attack":
            #calculate whether attack hits and damage
            if randint(0,13) != 0:
                attackDamage = int((player.baseAttack * (player.strength/3))*bideMult*dodgeMult)
                enemy.health += -attackDamage#attack dam with modifiers
                if dodgeMult*bideMult > 1:
                    print(bideMult*dodgeMult,"X damage bonus")
                print("you dealt",attackDamage, "damage to",name)
            else:
                print("you missed")
            bideMult = 1
        elif answer == "dodge":
            if randint(0,10) < 70 + player.intelligence:
                dodge = True #dodge 100 acc fix later #fix fixed but fix note not removed -fix later
            else:
                print("you fail to dodge")
        elif answer == "bide":
            bideMult = 2
            print("you focus on your next attack")
        elif answer =="item":
            player.useItem(enemy=enemy)
        elif answer == "flee":
            healthLost =  (randint(int(0.2*player.health),int(0.5*player.health)))
            print(healthLost,"damage taken whilst fleeing")
            player.health += -healthLost
            return
        dodgeMult = 1
        
        #enemy response
        if dodge == True:
            if critTurns == 0:
                dodgeMult = 1.5
            dodge = False
            print("dodged attack")
        else:#enemy can attack while player alive fix later
            if critTurns == 0:
                player.health += -enemy.attack * 2
                print("critical hit: enemy dealt",enemy.attack*2,"damage")
            else:
                player.health += -enemy.attack
                print("enemy dealt",enemy.attack,"damage")

        #check for dead characters
        if enemy.health <= 0:
            print(name,"has been slain")#prints file path fix later
            player.health += int((maxHP +enemy.attack)/10)
            player.maxHealth += int((maxHP +enemy.attack)/10)
            x =randint(0,30+2*player.luck)
            player.money += x
            print("\nHP increased by", int((maxHP +enemy.attack)/10))
            print(x,"money found")
            return
        elif player.health <= 0:
            print("you have died to", name)
            return

        #try print taunt
        if tauntList != []:
            print(tauntList[0], "\n    ", choice(tauntList[1:]))

        #Print stats
        print("your health: ",player.health, "/" ,player.maxHealth)
        print("enemy Health: ", enemy.health)
