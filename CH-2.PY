
##################

# Exercise 2:
#Write a program that uses input to prompt a user for their
# name and then welcomes them.
##################

#solution:-
fhand=input('Enter your name: ')
print('Hello',fhand)

###################
#/////////////////////////////////////////////
###################

#Exercise 3:
#Write a program to prompt the user for hours and rate per
#hour to compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
##################

#solution:-
hour=input('Enter Hours:')
h=float(hour)
rate=input('Enter Rate:')
r=float(rate)
pay=float(h*r)
print(round(pay,2)) #round funcn is use to properly round
                    #the resulting pay to two decimal places .
##################
#////////////////////////////////////////////////
##################

#Exercise 4:
#Assume that we execute the following assignment statements:
#width = 17
#height = 12.0
#For each of the following expressions, write the value of the expression and the
#type (of the value of the expression).
#1. width//2
#2. width/2.0
#3. height/3
#4. 1 + 2 * 5
#Use the Python interpreter to check your answers
##################

#solution:-
width=17
height=12.0
print(width//2) #the floor division // rounds the result down to the nearest whole number
#8(int)
print(width/2.0)
#8.5(floor)
print(height/3)
#4.0(floor)
print(1 + 2 * 5)
#11(int)

###################
