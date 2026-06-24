class Instagram:
    def __init__(self,username,password): #constactor
        self.username=username
        self.__password=password
        self.followers=[]
        print(f"Welcome to the Instagram, {self.username}")

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password=newpassword
        


praveen=Instagram("Praveen","praveen@123")

print("Before username",praveen.username)
praveen.username='Kumar'
print("after username",praveen.username)

print("Before Password",praveen.getpassword())
praveen.setpassword("Kumar@123")
print("After Password",praveen.getpassword())

'''
Welcome to the Instagram, Praveen
Before username Praveen
after username Kumar
Before Password praveen@123
After Password Kumar@123
'''
