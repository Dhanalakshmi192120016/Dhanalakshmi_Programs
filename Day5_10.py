c=input("Enter the Character to be printed: ")
rows=int(input("Max Number of time printed: "))
if(rows>0):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print(c, end=' ')
        print("\r")
else:
    print("No of rows cannot be negative")
