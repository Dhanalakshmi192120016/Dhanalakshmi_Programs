#n_perfect_numbers
try:
    start=int(input("Enter the start number of range: "))
    end=int(input("Enter the end number of range: "))
    for n in range(start,end+1):
        sum=0
        for i in range(0,n):
            if (n%i == 0):
                sum+=i
        if(n==sum):
            print(n)
except ValueError:
    print("Enter the input as positive integer")
    

