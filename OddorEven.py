# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 02:18:20 2018

@author: JUSTINE
"""
"""
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd number
 react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to 
divide by (check). If check divides evenly into num, tell that to the user.
 If not, print a different appropriate message.
"""

def oddOrEven(number,divisor):
    if number%2 == 0:
        if number%4 == 0:
            print("{} is an even number and a multiple of 4!".format(number))
        else:
             print("{} is an even number!".format(number))
    else:
        print("{} is an odd number!".format(number))
    print()
    print()
    print()
    print("Now checking whether the number is divided by the divisor evenly: ")
    if number%divisor == 0:
        print("{} is divided evenly by {}".format(number,divisor), end = '\n')
    else:
       print("{} is not divided evenly by {}".format(number,divisor), end = '\n')
   
        

print("This program determine whether the user input is an odd or an even number", end = '\n')
print("This program also determines whether the user's chosen divider will divide the first number evenly.", end = '\n')

#First number:
while True:
    try:
        usernumber = int(input("Input the number you wanted to check: "))
        if usernumber < 0:
            print("Input a non-negative number")
        else:
            break
    except:
        print("Input a valid non-negative number!")
#Second number: 
        
while True:
    try:
        divisor = int(input("Input the divisor: "))
        if usernumber < 0:
            print("Input a non-negative number")
        else:
            break
    except:
        print("Input a valid non-negative number!")
oddOrEven(usernumber,divisor)
        
