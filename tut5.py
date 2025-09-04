total=0

while(True):
    choice=int(input("Enter your choice"))
    print("Options are available for you:1)cold drink 2)snacks 3)exit")
    if(choice==1):
        print("1.pepsi=30/- 2.coke=40/- 3.maaza=50/-")
        subchoice=int(input("enter your subchoice"))
        if(subchoice==1):
            total=total+30
        elif(subchoice==2):
            total=total+40
        else:
            total=total+50
    elif(choice==2):
        print("1.Samosa=40/-2.Burger=50/- 3.patties=40/-")
        subchoice=int(input("enter your subchoice"))
        if(subchoice==1):
            total=total+40
        elif(subchoice==2):
            total=total+50
        else:
            total=total+40
    else:
        print("exit and generate bill")  
        
    print("your bill",total)  
