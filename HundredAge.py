# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:47:03 2018
"""
"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many 
copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""
from datetime import datetime

#Function for Name and Age
def hundredYears(name,age):
    """This function displays the name and age of the user as well as the year when the user will be 100 years old.
           Aside from that, this function also repeats the message based on how many times the user wanted to redisplay
           the message.
      
           For example name = Jay, age = 5
         
           The program will output:" Hello Jay your age is 5 and you're going to be 100 years old in the year (yearhundred)"
           Where yearhundred is based on the current year - age + 100
    """
    
    yearhundred = (int(datetime.now().strftime('20%y'))-age) + 100
    
    print("Hello ",name," your age is ",age," and you're going to be 100 years old in the year ",yearhundred)
    
    while True:
        try:
            displaymany = int(input("Input how many times do you want to display the previous message "))
            break
        except:
            print("Invalid input! Please provide a number only!" )
    
    for i in range(displaymany):
        print("Hello ",name," your age is ",age," and you're going to be 100 years old in the year ",yearhundred,end = '\n')
        
    
#Main Program:
print("This program is about finding what year are going to turn 100", end = '\n')  
#Simple name input
name = input("What first is your name? ")
#This is used to ensure that the user will only type a valid age or number
while True:
    try:
        age = int(input("What is your age? "))
        break
    except:
        print("Invalid input! Please provide a number only!" )


hundredYears(name,age)
