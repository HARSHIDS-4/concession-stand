#concession stand program
print("WELCOME TO THE CONCESSION STAND!!")
print()
print("-----------MENU📜-------------")
menu={ "Popcorn":300 ,
        "Pizza":500 ,
        "Sandwich" :150 , 
        "Nachos And Cheese":350,
        "Hot Dog":150,
        "Candy":60,
        "Mineral Water":50,
        "Coffee":100,
        "Hot Chocolate":110,
        "Soda":70,
        "Smoothie":170}

def display_menu():
    for key,value in menu.items():
        print(f"{key:<20}  {value:>2}")


def select_item():
    orders=[]  
    value=[]
    quantities=[]
    amounts=[]

    while True:
        item=input("select an item(q to quit)🍽:")
        item=item.title()

        if item=="q" or item=="Q": 
            break

        elif item not in menu:
            print("item not in menu.PLEASE TRY AGAIN")
            menu.update({item:0})

        else:
            qty=int(input(f"enter the quantity of {item} you want:"))
            orders.append(item)
            prices=menu.get(item)
            value.append(prices)
            quantities.append(qty)
            amount = prices * qty
            amounts.append(amount)


    return orders,quantities,amounts,amount

def coupon():
    coupon_ask=input("Do you have coupon?(yes or no)").lower()
    if coupon_ask=="yes":
        coupon_code=input("enter the coupon code:")
        if coupon_code=="SS1967":
            print("valid coupon you can avail discount of 10%😃")
            return True
        else:
            print("invalid coupon code😔")
            return False

    return coupon_code

def receipt(orders,quantities,amounts,amount,has_coupon):
    print(f"{'item':<10} {'quantity':<10} {'price':>10}")
    print('-'*37)

    for ite,quantitie,amt in zip(orders,quantities,amounts): 
        print(f"{ite:<10} {quantitie:<10} {amt:>10}")
    print('-' * 37)
    if has_coupon:
        discount = sum(amounts) * 10/100
        
        total =sum(amounts) - discount
        print(f"{'discount':<10} {'10%':<10} {discount:>10}")
    else:
        total=sum(amounts)
    print(f"{'TOTAL':<10} {total:>20}")

def time_date():
    import datetime 
    print(datetime.date.today())
    now=datetime.datetime.now()
    print(now.time())

    
          
display_menu()
print("----------------------------")  
orders, quantities, amounts,amount = select_item()
has_coupon = coupon()
print()
print("---------YOUR RECEIPT----------------")
receipt(orders,quantities,amounts,amount,has_coupon) 
print("-------------------------------------")
time_date()
