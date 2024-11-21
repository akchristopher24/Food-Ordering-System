class Cart:
    def __init__(self,items,Choices):
        self.Choices = Choices
        self.FoodItems = self.__AddtoCart(items)

    def __AddtoCart(self,items):
        foodDic = {}

        for Choice in self.Choices:

            if Choice > len(items):
                raise KeyError
            elif Choice in foodDic:
                foodDic[Choice] += 1
            else:
                foodDic[Choice] = 1
        return foodDic

    def ProcessOrder(self,fooditems):
        Total = 0
        for item in self.FoodItems:
            price = self.FoodItems[item] * fooditems[item-1].Price
            Total += price
            print(f"{fooditems[item-1].Name} x {self.FoodItems[item]} = {price}")
        print(f"Total = {Total}")
        self.ProcessPayment(Total)

    def ProcessPayment(self,amount):
        pass


