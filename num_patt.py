#number_pattern
r=int(input("Enter the number of rows: "))
k=2*r-2
for i in range(1,r+1):
    for j in range(1,i-1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print("\r")
