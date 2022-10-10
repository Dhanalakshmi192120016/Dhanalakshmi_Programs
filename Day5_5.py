a=[ ]
b=int(input("Enter the number of elements: "))
for i in range(b):
    d=input("Enter the number: ")
    a.append(d)
frequency = {}
for item in a:
     if item in frequency:
         frequency[item] += 1
     else:
         frequency[item] = 1
      
print(frequency)
print("Element | Frequency")
for key, value in frequency.items():
    print(f'{key:<10}{value}')
