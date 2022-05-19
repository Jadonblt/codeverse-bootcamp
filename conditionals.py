#   i = int(input("Enter the number:"))
#   if i != 5:
#      print("Not Equal to five")
#    else:
#       print("Caught ya!")

# If a number is less than 10: print less than 10 and if its divisible by 3: print divisible by 3

#i = int(input("Enter the number:"))
#if i < 10:
#    print("Less than 10")
#    if i % 3 == 0:
#        print("Divisible by 3")
#else : 
#    print("Not less than 10")
#    if i % 3 == 0:
#        print("Divisible by 3")

# i = 0
# while i <= 5:
#     print(i)
#     i = i + 1
# print("Done!")

# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i + j)
#         j = j + 1
#     i = i + 1
# print('Done!')

# Print numbers up to 20 where number divisible by 5 print high five!

# i = 0
# while i <= 20:
#     if i % 5 == 0:
#         print("High Five!")
#     else:
#         print(i)
#     i += 1

# Homework: Print numbers upto 200. where numbers divisible by 3 print "Free" & Divisible by 7 print "Heaven"
# if both then " Free Heaven" instead"

i = 0
while i <= 200:
    if i % 3 == 0:
        print("Free")
        if i % 7 == 0:
            print("Heaven")
    elif i % 3 or 7 == 0:
        print("Free Heaven")
    else:
        print(i)
    i = i + 1