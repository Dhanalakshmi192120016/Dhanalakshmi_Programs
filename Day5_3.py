g=input("Enter the grade of the employee(A/B): ")
s=int(input("Enter the salary of the Employee: "))
B=0
if s<=0:
    print("Invalid input")
if(g!='A' and g!='B'):
    print("Invalid Input")
elif g=='A':
    b=s*0.05
    print("Salary : ",s)
    print("Bonus : ",B)
    print("Total Amount to be paid: ",s+B)
elif g=='B':
    B=s*0.10
    print("Salary : ",s)
    print("Bonus : ",B)
    print("Total Amount to be paid:",s+B)
elif s<10000:
    B=s*0.2
    print("Salary : ",s)
    print("Bonus : ",s-B)
    print("Total Amount to be paid : ",s+B)
else:
    print("Enter a valid input")
