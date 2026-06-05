products={
    'laptops':0,
    'mouse':10,
    'charger':5,
    'phones':30,
    'keyboard':0
    }
product=input("enter the product")

if product in products:
    if products[product]!=0:
        print(f"you can buy {product}")
    else:
        print(f'{product} out of stock')
else:
    print(f'{product} is not available')
