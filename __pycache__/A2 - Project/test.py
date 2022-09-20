import unittest as u
import computer as c
import oo_resale_shop as rs
#import means we can use the functions and the classes from the file -
#so like importing computer.py and oo_resale_shop file


class TestComputer(u.TestCase):
    def test_at(self):
        computer = c.Computer("Lenovo", 2010, 1000, "Intel", 512, 16, "Windows 10")
        self.assertEqual(computer.description, "Lenovo")
        self.assertEqual(computer.year_made, 2010)
        self.assertEqual(computer.price, 1000)
        self.assertEqual(computer.processor_type, "Intel")
        self.assertEqual(computer.hard_drive_capacity, 512)
        self.assertEqual(computer.memory, 16)
        self.assertEqual(computer.operating_system, "Windows 10")

class TestShop(u.TestCase):
    def create_computer(self):
        computer = c.Computer("Lenovo", 2010, 1000, "Intel", 512, 16, "Windows 10")
        #have to list in order that you listed up above/in the shop
        return computer
    def test_buy(self):
        pc = self.create_computer()
        shop = rs.ResaleShop()
        shop.buy(pc)
        self.assertEqual(len(shop.inventory), 1)
        self.assertEqual(shop.inventory[0], pc)
    def test_sell(self):
        pc = self.create_computer()
        #had to define this as create_computer because it's easier - 
        # easier to define as a class item than doing computer = c.computer every time we call it
        shop = rs.ResaleShop()
        shop.buy(pc)
        shop.sell(0)
        #it's zero because we want the id of the thing we're trying tosell
        self.assertEqual(len(shop.inventory), 0)
        #this makes sure nothin is in the inventory after it's been sold
    def test_updatePrice(self):
        #put update price 'cause you wanna be specific about what test you are running
        pc = self.create_computer()
        shop = rs.ResaleShop()
        #this creates an instance of the resale shop class
        shop.buy(pc)
        shop.updatePrice(0, 500)
        #0 is the id of the computer and 500 is the price we wanna update
        self.assertEqual(shop.inventory[0].price, 500)
    def test_updateOS(self):
        #put update price 'cause you wanna be specific about what test you are running
        pc = self.create_computer()
        shop = rs.ResaleShop()
        #this creates an instance of the resale shop class
        shop.buy(pc)
        shop.updateOS(0, "IOS")
        #0 is the id of the computer and 500 is the price we wanna update
        self.assertEqual(shop.inventory[0].operating_system, "IOS")
    def test_Refurbish(self):
        pc = self.create_computer()
        shop = rs.ResaleShop()
        shop.buy(pc)
        shop.Refurbish(0, "IOS")
        self.assertEqual(shop.inventory[0].operating_system, "IOS")
        self.assertEqual(shop.inventory[0].price, 250)

    def test_errors(self):
        shop = rs.ResaleShop()
        shop.Refurbish(1)
        shop.sell(2)
        shop.updateOS(2,"IOS")
        shop.updatePrice (2, 200)


if __name__ == "__main__":
    u.main()


        


    

