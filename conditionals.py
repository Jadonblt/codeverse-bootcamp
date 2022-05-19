#   i = int(input("Enter the number:"))
#   if i != 5:
#      print("Not Equal to five")
#    else:
#       print("Caught ya!")

# If a number is less than 10: print less than 10 and if its divisible by 3: print divisible by 3

i = int(input("Enter the number:"))
if i < 10:
    print("Less than 10")
    if i % 3 == 0:
        print("Divisible by 3")
else : 
    print("Not less than 10")
    if i % 3 == 0:
        print("Divisible by 3")
