def Fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(Fibonacci(n-2)+Fibonacci(n-1))
print("Enter the value of num: ")
n=int(input())
for num in range(0,n):
    print(Fibonacci(num))
