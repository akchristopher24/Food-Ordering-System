from Models.AbstractItem import AbstractItem
from Models.FoodMenu import FoodMenu


class Restaurant(AbstractItem):
    def __init__(self,name,rating,location,offer):
        super().__init__(name, rating)
        self.Location = location
        self.Offer = offer
        self.__FoodMenus = []

    @property
    def FoodMenus(self):
        return self.__FoodMenus

    @FoodMenus.setter
    def FoodMenus(self,items):
        for item in items:
            if not isinstance(item,FoodMenu):
                print("Invalid food menu")
                return
            self.__FoodMenus = items

    def DisplayItem(self,start):
        print(f"{start}=>{self.Name} => Rating : {self.Rating} ")



        