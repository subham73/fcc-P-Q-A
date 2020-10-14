#Exercise 1:
# Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number

##################

#solution:-

count=0
sum=0
while True:
    inp=input('Enter a number:')
    if inp=='done':
        break
    try:
        num=int(inp)
        count+=1
        sum+=num
    except ValueError:
        print('Invalid input')
print(sum,count,sum/count)


####################

#/////////////////////////////////////////////////

###################

#Exercise 2:
#Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.

################

#solution:-

max=None
min=None
while True:
    inp=input('Enter a number:')
    if inp=='done':
        break
    try:
        num=int(inp)
        if max==None or max<num:
            max=num
        if min==None or min>num:
            min=num
    except ValueError:
        print('Invalid input')
print('maximum:',max)
print('minimum:',min)

###################
