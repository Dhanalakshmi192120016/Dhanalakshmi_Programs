try:
    n=int(input("Enter the number : "))
    rev=0
    if(n>=0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
        print("Reverse number:",rev)
    else:
        print("Enter only positive integers")
except ValueError:
    print("Enter only positive integers")
