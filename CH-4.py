#Exercise 4:
# What is the purpose of the “def” keyword in Python?
#a) It is slang that means “the following code is really cool”
#b) It indicates the start of a function
#c) It indicates that the following indented section of code is to be stored for later
#d) b and c are both true
#e) None of the above

#solution:- (d)

########################

#////////////////////////////////////////////

########################

#Exercise 5: What will the following Python program print out?
#def fred():
#print("Zap")
#def jane():
#print("ABC")
#jane()
#fred()
#jane()
#a) Zap ABC jane fred jane
#b) Zap ABC Zap
#c) ABC Zap jane
#d) ABC Zap ABC
#e) Zap Zap Zap

#solution:- (d)

########################

#//////////////////////////////////////////////

########################

#Exercise 6:
#Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters
#(hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

###################

#solution:-
inp = input('Enter Hours: ')
hours = float(inp)
inp = input('Enter Rate: ')
rate = float(inp)

def computepay(hours,rate):
    if hours > 40:
        pay = ((hours-40)*rate*1.5)+rate*40
        return pay
    else:
        pay = hours * rate
        return pay

pay=computepay(hours,rate)
print('Pay:',pay)

########################

#//////////////////////////////////////////////

########################

#Exercise 7:
#Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.
#    Score    Grade
#   >=  0.9     A
#   >=  0.8     B
#   >=  0.7     C
#   >=  0.6     D
#   <   0.6     F
#######################

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

def computegrade(score):
    if   score >= 0.9: x='A'
    elif score >= 0.8: x='B'
    elif score >= 0.7: x='C'
    elif score >= 0.6: x='D'
    else :x='F'
    return x
grade=computegrade(score)
print(grade)

###################
