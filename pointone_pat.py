#0.1_pattern
rows = int(input("number of rows: "))
for i in range(1,rows+1):
    for j in range (1,i+1):
        print(j/10,end=" ")
    print("\r")
    
