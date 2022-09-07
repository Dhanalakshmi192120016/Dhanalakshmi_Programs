try:
    num = int(input(" Please Enter any Number: "))
    Sum = 0
    if(num>=0):
        for i in range(1, num,1):
            if(num % i == 0):
                Sum = Sum + i
        if (Sum == num):
            print(" %d is a Perfect Number" %num)
        else:
            print(" %d is not a Perfect Number" %num)
    else:
        print("Enter a positive integer")
        
except ValueError:
        print("Enter a valid whole number")


