#Exercise 4:
#Download a copy of the file www.py4e.com/code3/romeo.txt.
#Write a program to open the file romeo.txt and read it line by line. For
#each line, split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the word
#is not in the list, add it to the list. When the program completes, sort
#and print the resulting words in alphabetical order.

###################

#solution:-

file_read=input('Enter file: ')
file=open(file_read)

lst=list()                          #list for desired output

for line in file:                   #to read everey ine of romeo.txt
    n_line=line.rstrip().split()    #to eleminate the unwanted blank and turn the line into list of words
    for ele in n_line:              #check every element in word
        if ele in lst:              #if element is repeated
            continue                #do nothing
        else:                       #else if elements not in the list
            lst.append(ele)         #append

lst.sort()                          #sort the list
print (lst)                         #print the list

#####################

#///////////////////////////////////////////////////////////////////

####################

#Exercise 5:
#Write a program to read through the mail box data and
#when you find line that starts with “From”, you will split the line into
#words using the split function. We are interested in who sent the
#message, which is the second word on the From line.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#You will parse the From line and print out the second word for each
#From line, then you will also count the number of From (not From:)
#lines and print out a count at the end. This is a good sample output
#with a few lines removed:

############################

#solution:-

file_read=input('Enter the file name:')
file=open(file_read)
count=0
for line in file:
    if line.startswith("From") and not line.startswith("From:"):
        n_line=line.rstrip().split()
        print(n_line[1])
        count+=1
    else:
        continue
print('There were ',count,'lines in the file with From as the first word')

#############################

#////////////////////////////////////////////////////////////////////

#############################

#Exercise 6:
#Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes

############################

#solution:-

lst=list()
while True:
    inp=input('Enter a number:')
    if inp=='done':
        break
    try:
        num=float(inp)
        lst.append(num)
    except ValueError:
        print('Invalid input')
print('maximum:',max(lst))
print('minimum:',min(lst))

###############################
