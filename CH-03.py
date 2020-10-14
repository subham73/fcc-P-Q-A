#####################

#Exercise 1:
#Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.

####################

#solution:-
inp = input('Enter Hours: ')
hours = float(inp)
inp = input('Enter Rate: ')
rate = float(inp)

if hours > 40:
    pay = ((hours-40)*rate*1.5)+rate*40
else:
    pay = hours * rate

print('Pay:', pay)

###################

#///////////////////////////////////////////

###################

#Exercise 2:
#Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

###################

#solution:-
while True:
    try:
        inp = input('Enter Hours: ')
        hours = float(inp)
        inp = input('Enter Rate: ')
        rate = float(inp)
        break
    except:
        print('Error, please enter numeric input')
        exit(0)

if hours > 40:
    pay = ((hours-40)*rate*1.5)+rate*40
else:
    pay = hours * rate

print('Pay:', pay)

######################

#//////////////////////////////////////////////

######################

#Exercise 3:
#Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table:
#
#   >=  0.9  A
#   >=  0.8  B
#   >=  0.7  C
#   >=  0.6  D
#   <   0.6  F

######################

#solution:-
inp=input('Enter score:')
try:
    score=float(inp)
except ValueError:
    print('Bad score')
    exit()
if score > 1.0 or score < 0.0:
    print('Bad score')
    exit()
if   score >= 0.9: print('A')
elif score >= 0.8: print('B')
elif score >= 0.7: print('C')
elif score >= 0.6: print('D')
else :print('F')

####################
