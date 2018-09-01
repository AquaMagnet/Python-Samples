# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:50:20 2018

@author: JUSTINE
"""

"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the 
elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, 
make a new list that has all the elements less 
than 5 from this list in it and print out 
this new list.

Write this in one line of Python.

Ask the user for a number and return a list that 
contains only elements from the original list a 
that are smaller than that number given by the user.
"""

def lessthanList(listings,lessThan):
    print("The list where the numbers are less than {0} is = ".format(lessThan))
    print([listings[i] for i in range(len(listings)) if listings[i]<lessThan])
    #It will display listings or the number for each item under listings if listings < the threshold

print("This program accepts a list and a number that will be used as the \
      threshold for the final output. The output will be equal to the numbers \
      inside the list less than that number")

#How many numbers in list:
while True:
    try:
        usernumber = int(input("Input the number of values in the list: "))
        if usernumber < 0:
            print("Input a non-negative number")
        else:
            break
    except:
        print("Input a valid non-negative number!")
#Getting the values
listings = []
print(usernumber)
i = 0
while i < usernumber:
        listings.append(int(input("Number: ")))
        i += 1

#How many numbers in list:
while True:
    try:
        lessThan = int(input("Input the threshold: "))
        break
    except:
        print("Input a valid non-negative number!")
lessthanList(listings,lessThan)
