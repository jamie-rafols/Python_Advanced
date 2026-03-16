day = int(input("Enter number 1-7: "))

match day:
    case 1:
        print("This is Monday")
    case 2: 
        print("This is Tuesday")
    case 3:
        print("This is Wednesday")
    case 4:
        print("This is Thursday")
    case 5:
        print("This is friday")
    case 6:
        print("This is Saturday")
    case 7:
        print("This is Sunday")
    case _:
        print("Entered number not within the range")