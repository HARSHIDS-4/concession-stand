#concession stand program
print("WELCOME TO THE CONCESSION STAND!!")
print()
print("-----------MENU-------------")
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
        item=input("select an item(q to quit):")
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


def receipt(orders,quantities,amounts,amount):
    print(f"{'item':<10} {'quantity':<10} {'price':>10}")
    print('-'*37)

    for ite,quantitie,amt in zip(orders,quantities,amounts): 
        print(f"{ite:<10} {quantitie:<10} {amt:>10}")
    print('-' * 37)
    total = sum(amounts)
    print(f"{'TOTAL':<10} {total:>20}")

def time_date():
    import datetime 
    print(datetime.date.today())
    now=datetime.datetime.now()
    print(now.time())

    
          
display_menu()
print("----------------------------")  
orders, quantities, amounts,amount = select_item()
print()
print("---------YOUR RECEIPT----------------")
receipt(orders,quantities,amounts,amount) 
print("-------------------------------------")
time_date()
