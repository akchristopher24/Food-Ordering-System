from Models.AbstractItem import AbstractItem
from Models.FoodItem import FoodItem

class FoodMenu(AbstractItem):
    def __init__(self,name):
        super().__init__(name)
        self.__FoodItems = []

    def DisplayItem(self, start):
        print(f"{start}=>{self.Name}")

@property
def FoodItems(self):
    return self.__FoodItems

@FoodItems.setter
def FoodItems(self,items):
    for item in items:
        if not isinstance(item, FoodItem):
            print("invalid food item")
            return
    self.__FoodItems = items

