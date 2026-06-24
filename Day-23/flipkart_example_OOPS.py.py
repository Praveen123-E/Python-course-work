
#OOPS concept

class flipkart:
    discount=10 #class attribute
    products=['laptop','phone','mouse','charger']
    
    @classmethod
    def showProducts(cls):
        print(cls.products)

    def login(self,username,password): #object attribute
        self.username=username
        self.password=password
        print(f"Welcome to the flipkart {self.username}")

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now")

    
        


praveen= flipkart()

praveen.login('praveen','praveen@123')
praveen.banner()
praveen.showProducts()

#Welcome to the flipkart praveen
#10% discount is going on flipkart, shop now
#['laptop', 'phone', 'mouse', 'charger']


flipkart.banner() #class name with only class method or static method not instance method
flipkart.showProducts()

Welcome to the flipkart praveen
10% discount is going on flipkart, shop now
['laptop', 'phone', 'mouse', 'charger']
10% discount is going on flipkart, shop now
['laptop', 'phone', 'mouse', 'charger']


