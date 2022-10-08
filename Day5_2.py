start=int(input("Enter the starting range : "))
end=int(input("Enter the ending range : "))
count=0
if(start>0)and(end>0)and(start<end):
    print("Composite Numbers between %d and %d: " % (start, end))

    for start in range(start+1, end+1):
        for i in range(1, start+1):
            if(start % i == 0):
                count += 1
        if(count > 2):
           print(start, end=" ")
        count = 0
else:
    print("Range is invalid")
