try:
    str=input("Enter the string: ")
    rev_str=" "
    for i in str:
        rev_str=str[::-1]
    print("The reversed string is ",rev_str)
except ValueError:
    print("Enter only letters")
          

