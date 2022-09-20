import computer 
class ResaleShop:

    # What attributes will it need?
    """
needs the stuff about buying a computer
price updates
selling info 
removing the stuff you sold
what happens if you need to refurbish a computer
inventory
"""
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
  
    # What methods will you need?

    def __init__ (self):
        self.inventory={}
        self.id = 0
    #only need one def init per class

    def updatePrice(self, id, newPrice):
        if id in self.inventory:
            self.inventory[id].price = newPrice
        else:
            print("Item", id, "not found. Cannot update price.")

    def updateOS(self, id, newOS):
        if id in self.inventory:
            self.inventory[id].operating_system = newOS
        else:
            print("Item", id, "not found. Cannot update operating system.")

    def Refurbish(self, id, newOS = None):
        #optional perameter - doesn't always
        #have to update OS if you just want to
        #refurbish something
        if id in self.inventory:
            computer = self.inventory[id] #locate the computer
            if computer.year_made < 2000:
                self.updatePrice(id, 0) # too old to sell, donation only
            elif computer.year_made < 2012:
                self.updatePrice(id, 250) # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                self.updatePrice(0, 550) # discounted price on machines 4-to-10 year old machines
            else:
                self.updatePrice(0,1000) # recent stuff
            if newOS is not None:
                self.updateOS(id, newOS) # update details after installing new OS
        else:
            print("Item", id, "not found. Please select another item to refurbish.")

    def buy(self, computer):
        self.inventory[self.id] = computer
        self.id += 1
        #this will increment/add 1 to each id for each computer

        #checks if the id is in the inventory
        #id is the ID of the computer that's 
        #associated with in the shop
    def sell(self, id):
        if id in self.inventory:
            del self.inventory[id]
            print("Item", id, "sold!")
        else:
            print("Item", id, "not found. PLease select another item to sell.")



    #anytime you do a new function inside a class
    #put "Self" but if you're not in a class
    #you don't have to do self like for a general script


    


        #this is storing info for the computer
        #dictionary:
            #holds key value pairs - it will return
            #values associated with that key

    