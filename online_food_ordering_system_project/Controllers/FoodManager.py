from Models.FoodMenu import FoodMenu
from Models.FoodItem import FoodItem
from Models.Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurant = self.__PrepareRestaurant()

    def __PrepareFoodItems(self):

        item1 = FoodItem("Veg Biriyani",4.5,150,"****")
        item2 = FoodItem("Chicken Biriyani",3.7,180,"***")
        item3 = FoodItem("Parota",2.8,100,"*")
        item4 = FoodItem("Dosa",5.0,200,"*****")
        item5 = FoodItem("Noodles",2.9,50,"**")
        return [item1,item2,item3,item4,item5]

    def __PrepareFoodMenus(self):
        FoodItems = self.__PrepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [FoodItems[0],FoodItems[3]]
        menu2 = FoodMenu("Non-veg")
        menu2.FoodItems = [FoodItems[2]]
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [FoodItems[4]]
        return [menu1,menu2,menu3]

    def __PrepareRestaurant(self):
        FoodMenus = self.__PrepareFoodMenus()
        res1 = Restaurant("A2B",4.6,"Nagercoil",50)
        res1.FoodMenus = [FoodMenus[0]]
        res2 = Restaurant("AryaBhavan",3.6,"coimbatore",25)
        res2.FoodMenus = [FoodMenus[0],FoodMenus[1]]
        res3 = Restaurant("Muniyandi vilas",2.7,"Madurai",10)
        res3.FoodMenus = [FoodMenus[1],FoodMenus[2]]
        return [res1,res2,res3]

    def FindRestaurant(self,name):
        for res in self.Restaurant:
            if res.Name == name:
                return res



