t=int(input("Enter the no of Total Users = "))
if(t>0):
      s=int(input("Enter the no of Staff users = "))
      print("Total Users = ",t)
      print("Staff Users = ",s)
      if(t>s):
          n=s/3
          print("Non-teaching staff users = ",n)
          res = t-(s+n)
          print("Student Users = ",res)
      else:
          print("Invalid Entries")
else:
    print("No of Total users entered is invalid")

