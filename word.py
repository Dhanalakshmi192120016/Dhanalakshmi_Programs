#words_and_characters
string=input("Enter the string: ")
word = 1
cha = 0
for i in string:
    cha+=1
    if(i==' '):
        word+=1
print("Number of characters in the string",'=',cha)
print("Number of words in the string",'=',word)
