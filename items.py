import manageDB
import specialItems
import general as g

class items:
    #get item info
    def appraise(self,itemName):
        return manageDB.queryField("ItemTable",itemName)[0]
    #add item by name
    def addItem(self,itemName):
        print("you found an "+itemName)
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

    #player use item
    def useItem(self,enemy=False):
        #get item and item information
        if self.itemList == []:
            input("you have no items")
            return
        else:
            answer = g.valInput(self.itemList+["none"])
            if answer == "none":
                return
        itemData = manageDB.queryField("ItemTable",answer)[0]
        #for non combat items
        print(itemData)
        if itemData[1][0] == "p":
            if itemData[1] == "pSpecial":
                self.useSpecial(self,itemData)
            else:
                #for different item types
                if itemData[1] == "pHealth":#add static value
                    self.health += itemData[2]
                elif itemData[1] == "pRelHealth":#add percent of maxHealth
                    self.health += int(self.maxHealth*(itemData[2]/100))
                elif itemData[1] == "pAttack":#set attack to new value
                    self.baseAttack = itemData[2]
                if self.health > self.maxHealth:
                    self.health = self.maxHealth
        #check if item is usable
        elif enemy == False and itemData[1][0] != "p":
            print("This item is not for use outside combat")
            return
        #for combat items
        else:
            if itemData[1]  == "eSpecial":
                print("eSpecial")
                self.useSpecial(itemData,enemy)
            else:
                print("eNotSpecial")
                #for normal enemy items
                if itemData[1] == "eInstDmg":
                    enemy.health += -itemData[2]
                elif itemData == "eDamDebuff":
                    enemy.damage += -itemData[2]
        self.itemList.remove(itemData[0])
            
    def useSpecial(self,itemData,enemy=False):
        import specialItems
        getattr(specialItems,specialItems.nameDict[itemData[0]])(self,enemy)
