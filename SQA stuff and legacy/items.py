import manageDB
import specialItems
import general as g


class items:
    #get item info
    def appraise(self,itemName):
        return manageDB.queryField("ItemTable",itemName)[0]
    #add item by name
    def addItem(self,itemName):
        if len(self.itemList) < 3:
            self.itemList.append(itemName)
        else:
            print("remove an item?")
            answer = g.valInput(self.itemList+["none"])
            if answer == "none":
                return
            else:
                self.itemList[self.itemList.index(answer)] = itemName
    #add item at random according to list
    def addRandom(self, lootLevel): #1 to 4
        from random import choice
        self.addItem(choice(manageDB.lootListReturn(lootLevel)))

        'might wanna merge'
    #player use item
    def useItem(self,itemName,enemy=False):
        itemData = manageDB.queryField("ItemTable", itemName)[0]
        #
        if enemy == False:
            if itemData[1][0] != "p":
                print("This item is not for use outside combat")
            elif itemData[1] == "pSpecial":
                 useSpecial(self,itemData)
            else:
                useSelf(self,itemData)
        #for combat items
        else: #inefficient statement but neater
            if itemData[1][0]  == "eSpecial":
                useSpecial(self,itemData,enemy)
            else:
                useEnemy(self,itemData,enemy)
                             
    #for different item types
    def useSelf(self,itemData):
        if itemData[1] == "pHealth":#add static value
            self.health += itemData[2]
        elif itemData[1] == "pRelHealth":#add percent of maxHealth
            self.health += int(self.maxHealth*(itemData[2]/100))
        elif itemData[1] == "pAttack":#set attack to new value
            self.baseAttack = itemData[2]
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        self.itemList.remove(itemData[0])
        
    def useEnemy(self,itemData,enemy):
        if itemData[1] == "eInstDmg":
            enemy.health += -itemData[2]
        elif itemData == "eDamDebuff":
            enemy.damage += -itemData[2]
            
    def useSpecial(self,itemData,enemy=False):
        pass
