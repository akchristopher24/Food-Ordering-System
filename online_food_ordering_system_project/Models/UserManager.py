from Models.User import User
class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls, userObj):
        if isinstance(userObj,User):
            cls.__Users.append(userObj)
            print("You have successfully added to the Users list")
        else:
            print("Invalid User")

    @classmethod
    def FindUser(cls, mailid,pwd):
        for user in cls.__Users:
            if user.Mail == mailid and user.Password == pwd:
                return user
