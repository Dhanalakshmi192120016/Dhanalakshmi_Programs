#Average_of_marks
print("Enter marks in subject 1: ")
m1=int(input())
print("Enter marks in subject 2: ")
m2=int(input())
print("Enter marks in subject 2: ")
m3=int(input())
print("Enter marks in subject 2: ")
m4=int(input())

avg=(m1+m2+m3+m4)/4
if(avg>=90):
    print("S grade")
elif(avg>=80):
    print("A grade")
elif(avg>=70):
    print("B grade")
elif(avg>=60):
    print("C grade")
elif(avg>=50):
    print("D grade")
else:
    print("Fail")
        
