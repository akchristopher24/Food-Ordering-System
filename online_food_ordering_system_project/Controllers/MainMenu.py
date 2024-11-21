from Controllers.FoodManager import FoodManager
from Models.cart import Cart

class MainMenu:

    __Options = {1:"Show Restaurants",2:"Show FoodItems",3:"Search Restaurants", 4:"Search FoodItems",5:"Logout"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurants(self):
        for i,res in enumerate(self.__FoodManager.Restaurant,1):
            res.DisplayItem(i)
        Choice = int(input("pls select restaurants: "))
        res = self.__FoodManager.Restaurant[Choice-1]
        self.ShowFoodMenus(res.FoodMenus)

    def ShowFoodItems(self, foodItems = None):
        if foodItems  is not None:
            for i,foodItem in enumerate (foodItems,1):
                foodItem.DisplayItem(i)

            Choices = list(map(int, input("Please choose your food items (eg 1, 2)").split(',')))
            cart= Cart(foodItems, Choices)
            cart.ProcessOrder(foodItems)

        else:
            pass
    def SearchRestaurants(self):
        resName = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(resName)
        if res is not None:
            print(f"{res.Name} => Rating : {res.Rating} ")
            self.ShowFoodMenu(res.FoodMenus)
        else:
            print(f"no restaurant found on this name: {resName}")

    def SearchFoodItems(self):
        pass

    def ShowFoodMenus(self,menus):
        print("\n\n List of menus available:")
        for i,menu in enumerate(menus,1):
            menu.DisplayItem(i)
        Choice = int(input("Please choose menu: "))
        fooditems = menus[Choice-1].FoodItems
        self.ShowFoodItems(fooditems)



    def Start(self):
        while True:
            for option in self.__Options:
                print(f"{option}.{MainMenu.__Options[option]}",end=" ")
            print()

            try:
                Choice = int(input("Please Enter Your Choice:"))
                value = MainMenu.__Options[Choice].replace(" ","")
                getattr(self, value)()

            except (ValueError, KeyError):
                print("Invalid option")