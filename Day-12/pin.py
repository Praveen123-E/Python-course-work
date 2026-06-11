pin=1234

for i in range(5):
    e_pin=int(input("Enetr the pin:"))
    
    if e_pin == pin:
        print("Unlock your phone")
        break
    else:
        print("Incorrect pin")
else:
    print("Try again, after 60 seconds")
    
