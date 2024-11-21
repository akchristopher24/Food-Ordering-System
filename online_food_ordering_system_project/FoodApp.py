#online food ordering system
from Models.User import User
from Models.UserManager import UserManager
from Controllers.MainMenu import MainMenu
from Controllers.FoodManager import FoodManager

class LoginSystem:
    def Login(self):
        Email = input("Enter your email address: ")
        Password = input("Enter your password: ")

        user = UserManager.FindUser(Email, Password)
        if user is not None:
            print("Login Successful")
            menu = MainMenu()
            menu.Start()

        else:
            print("login failed")

    def Register(self):
        Name = input("Enter your name: ")
        Mobile = int(input("Enter your mobile number: "))
        Email = input("Enter your email address: ")
        Password = input("Enter your password: ")

        user = User(Name, Mobile, Email, Password)
        UserManager.AddUser(user)

    def GuestLogin(self):
        pass

    def Exit(self):
        print("Thank you for using our application")
        exit()

    def ValidateOption(self,option):
        getattr(self,option)()




class FoodApp():
    LoginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}
    @staticmethod
    def Init(): #Initial method
        print("Welcome to Food Ordering System")

        menu = MainMenu()
        menu.Start()

        """
        loginSystem = LoginSystem()

        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}",end="  ")
            print()
            try:
                Choice = int(input("Please Enter Your Choice:"))
                loginSystem.ValidateOption(FoodApp.LoginOptions[Choice])
            except (ValueError,KeyError):
                print("Invalid option")
        """



FoodApp.Init()







