data={
    123456:{'pin':1234,'balance':5000,'history':[]},
    234567:{'pin':2345,'balance':7000,'history':[]},
    345678:{'pin':3456,'balance':4000,'history':[]},
    456789:{'pin':4567,'balance':9000,'history':[]},
    }

def login():
    global acc_num
    acc_num=int(input("Enter the account number: "))
    pin=int(input("Enter the pin number: "))
    if acc_num in data and data[acc_num]['pin']==pin:
        print("Login Successful")
        return True
    else:
        print("Invaild Login")
        return False

def menu():
    print('[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')

def checkBalance():
    print("Current Balance:",data[acc_num]['balance'])

def deposit():
    amount=int(input("Enter the amount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} - Deposit ++++++')
    print("Deposit Successful")

    
def withdraw():
    amount=int(input("Enter the amount: "))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f'{amount} - Withdraw -----')
        print("Withdraw Successful")
    else:
        print("Insufficient Balance")

def viewTransactions():
    if data[acc_num]['history']:
        print("------Transactions------")
        for i in data[acc_num]['history']:
            print(i)
        print('------ END -------')
    else:
        print("No Transaction History")


























        

    

