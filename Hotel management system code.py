import sys,random
def details():
    while True:
        username=input("Enter the username: ")
        if username=='Admin123':
            break
    for i in range(3):
        password=input("Enter the password: ")
        if password=='CorrectPassword':
            print("User verified")
            break
        else:
            continue
            print("Attempts exceeded")
def display_menu():
    global menu
    menu={'Breakfast':{'Idly':'₹20','Dosa':'₹30','Poha':'₹25'},'Lunch':{'Dal Chawal':'₹50','Roti Curry':'₹45','Lunch Combo':'₹100'},'Dinner':{'Paratha':'₹60','Fried Rice':'₹100','Veg Briyani':'₹150'}}
    print('Menu'.center(50))
    for time, items in menu.items():
        print(time.center(50))
        for food, price in items.items():
            print(food.ljust(25) + ":" + price.rjust(25))
    
def edit():
    menu={'Breakfast':{'Idly':'₹20','Dosa':'₹30','Poha':'₹25'},'Lunch':{'Dal Chawal':'₹50','Roti Curry':'₹45','Lunch Combo':'₹100'},'Dinner':{'Paratha':'₹60','Fried Rice':'₹100','Veg Briyani':'₹150'}}
    ownChoice = input("1. Add 2. Delete 3. Update 4.Exit")
#this is for add
    if ownChoice == '1':
        mealChoice = input('Enter meal type b/l/d for beakrfast/luch/dinner:')
    
        if mealChoice == "b":
            bdish = input("Dishname:")
            bdprice = input("Dishprice:")
        #nested dictionar  = brekfast
            menu['Breakfast'][bdish]='₹'+bdprice
    
        elif mealChoice == "l":
            ldish = input("Dishname:")
            ldprice = input("Dishprice:")
            menu['Lunch'][ldish]='₹'+ldprice
        
        elif mealChoice == "d":
            ddish = input("Dishname:")
            ddprice = input("Dishprice:")
            menu['Dinner'][ddish]='₹'+ddprice
        else:
            print("Incorrect Choice")
        
#this for delete
    elif ownChoice == '2':
        mealChoice = input('Enter meal type b/l/d for beakrfast/luch/dinner:')
        if mealChoice == "b":
            bdish = input("Dishname:")
            menu['Breakfast'].pop(bdish)
        
        elif mealChoice == "l":
            ldish = input("Dishname:")
            menu['Lunch'].pop(ldish)
        
        elif mealChoice == "d":
            ddish = input("Dishname:")
            menu['Dinner'].pop(ddish)
        else:
            print("Incorrect Choice")
    
#this for update
    elif ownChoice=='3':
        mealChoice = input('Enter meal type b/l/d for beakrfast/luch/dinner:')
        if mealChoice == "b":
            bdish = input("Dishname:")
            new_price=input("Enter new price: ")
            menu['Breakfast'][bdish]='₹'+new_price
            
        elif mealChoice == "l":
            ldish = input("Dishname:")
            new_price=input("Enter new price: ")
            menu['Lunch'][ldish]='₹'+new_price
            
        elif mealChoice == "d":
            ddish = input("Dishname:")
            new_price=input("Enter new price: ")
            menu['Dinner'][ddish]='₹'+new_price
        else:
            print("Incorrect Choice")

#exit
    else:
        print("No edits")
        sys.exit(0)
    print('Menu'.center(50))
    for time, items in menu.items():
        print(time.center(50))
        for food, price in items.items():
            print(food.ljust(25) + ":" + price.rjust(25))
  
    
def owner():
    details()
    display_menu()
    while True:
        edit()
    #updated_menu()

def billing():
    menu={'Breakfast':{'Idly':20,'Dosa':30,'Poha':25},'Lunch':{'Dal Chawal':50,'Roti Curry':45,'Lunch Combo':100},'Dinner':{'Paratha':60,'Fried Rice':100,'Veg Briyani':150}}
    menuc=['Breakfast','Lunch','Dinner']
    itemsl=[]
    display_menu()
    for i,j in menu.items():
        for k in j.keys():
            itemsl.append(k)
    quantity=[]
    order=[]
    cn=input("enter name of customer: ")
    print("enter dates in DDMMYYYY: ")
    dob= input("enter dob: ")
    curr=input("enter current date: ")
    day= input("enter today\'s day: ")
    menu1=input("enter 1st two letters of meal type\nBreakfast\nLunch\nDinner")
    c=int(input("how many items would you like to order"))
    for i in range(c):
        print("Enter item[please enter 1st two letters of the item]")
        item=input()
        for j in range(len(itemsl)):
            if item in itemsl[j]:
                order.append(itemsl[j])
        print("Enter quantity of item")
        q=int(input())
        quantity.append(q)
    totalsi={}
    for i in range (3):
        if menu1 in menuc[i]:
            menu2=menuc[i]
            for i in range(c):
                for item in order:
                        total=0
                        a=menu[menu2][item]
                        b=order.index(item)
                        total = a*(quantity[b])
                        totalsi[item]=total
                               
    def discount(t,td):
        cr=int(curr[5::])
        yob=int(dob[5: :])
        if dob==curr:
            disc=(30/100)*t
        elif (cr-yob)>=60:
            disc=(20/100)*t
        elif(cn[0]==day[0]):
            disc=0
        else:
            disc=0
        return disc
    d=discount(total,day)
    print("Would you like to give a tip?(Y or N)")
    a=input()
    if a=='Y':
     print("How much?")
     tip=int(input())
    else:
     tip=0
    gst= (18/100)*(float(total))
    gt=0
    for val in totalsi.values():
        gt+=val
    gt+=tip
    gt+=gst


    #Display bill
    print('PARAPANCHA'.center(101))
    print('date'+curr.ljust(50) + ('BillID:'+'100' + str(random.randint(100,500))).rjust(50))
    starline = "*"* 100
    print(starline)
    print("Items".ljust(25) + "Quantity".center(25) + 'Price'.center(25) + 'Total'.rjust(25))
    b=0
    for it in totalsi.keys():
        #print(it)
        print(it.ljust(25) + str(quantity[b]).center(25) + str(menu[menu2][it]).center(25) + str(totalsi[it]).rjust(25))
        b+=1
    print(starline)
    print('Sub Total:'.ljust(50) + str(total).rjust(50))
    print('GST @ 18%:'.ljust(50) + str(gst).rjust(50))
    print("Tip amount:".ljust(50)+ str(tip).rjust(50))
    print("Discount:".ljust(50) + str(d).rjust(50))
    print("Total:".ljust(50) + str(gt).rjust(50))
    print('****** Thank you for your visit. Visit again !!! ******'.center(100))

while True:
    print("1.Owner\t2.Billing\t3.Exit")
    ch=input("Enter your choice: ")
    if ch=='1':
        owner()
    elif ch=='2':
        billing()
    else:
        sys.exit(0)
