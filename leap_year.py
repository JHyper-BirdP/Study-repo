year = int(input("what year do you want to know if it's leap year or not."))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("It's leap year")
        else:
            print("It's not leap year")
    else:
        print("It's leap year")    
else: 
    print("It's not leap year")

     