
#Test Calculator in Python#

import math
print(" Weclome to Patrick Arthur's Calculator: V1")
print("     A) Add")
print("     B) Sub")
print("     C) Mul")
print("     D) Div")
choice = raw_input("Pick your choice: ")
if choice == "A":
   print("You better be ready to add numbers!")
   x= input("First Number: ")
   y= input("Second Number: ")
   print("Your answer is: "+str(x+y))
   raw_input("Press <ENTER> to exit")
if choice == "B":
    print("You better be ready to subtract numbers!")
    x= input("First Number: ")
    y= input("Second Number: ")
    print("Your answer is: "+str(x-y))
    raw_input("Press <ENTER> to exit")
if choice == "C":
    print("You better be ready to multiply numbers!")
    x= input("First Number: ")
    y= input("Second Number: ")
    print("Your answer is: "+str(x*y))
    raw_input("Press <ENTER> to exit")
if choice == "D":
    print("You better be ready to divide numbers!")
    x= input("First Number: ")
    y= input("Second Number: ")
    print("Your answer is: "+str(x/y))
    raw_input("Press <ENTER> to exit")