#palindrome
a=input("Enter a string: ")
b=(a[::-1])
if a==b:
    print(a,"is palindrome")
else:
    print(a,"is not palindrome")
