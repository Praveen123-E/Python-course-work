class Redbus:
    busno='cg001'
    driver_name='xyz'
    driver_pno=9988776655

    seats={}
    for i in range(1,11):
        if i%2==0:
            seats[i]='Available'
        else:
            seats[i]='Booked'
            
    def __init__(self,name,pno,age):
        self._name=name
        self._pno=pno
        self._age = age
        print(f"Welcome to the Redbus {self._name}. Book your bus")
    

    @classmethod
    def showseats(cls):
        for i in cls.seats:
            print(i,cls.seats[i])

    def booking(self,seatno):
        if Redbus.seats[seatno] =='Available':
            Redbus.seats[seatno]='Booked'
            print(f'{seatno} is successfully booked')
            Redbus.driverinfo()
        else:
            print(f'{seatno} is already booked')

    @staticmethod
    def driverinfo():
        print("Driver INFO: ")
        print("Bus no",Redbus.busno)
        print("Driver Name",Redbus.driver_name)
        print("Driver_pno",Redbus.driver_pno)

        
praveen=Redbus('praveen',9988776655,21)
praveen.showseats()
praveen.booking(2)
praveen.showseats()



'''
Welcome to the Redbus praveen. Book your bus
1 Booked
2 Available
3 Booked
4 Available
5 Booked
6 Available
7 Booked
8 Available
9 Booked
10 Available
2 is successfully booked
Driver INFO: 
Bus no cg001
Driver Name xyz
Driver_pno 9988776655
1 Booked
2 Booked
3 Booked
4 Available
5 Booked
6 Available
7 Booked
8 Available
9 Booked
10 Available
'''
