#Exercise 1:
#Write a program to read through a file and print the contents
#of the file (line by line) all in upper case. Executing the program will
#look as follows:
#python shout.py
#Enter a file name: mbox-short.txt
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#SAT, 05 JAN 2008 09:14:16 -0500

#####################

#solution:-

read_file = input('Enter a file name:')# enter mbox-short.txt
file=open(read_file)

for line in file:
    stripped_line= line.rstrip()
    print(stripped_line.upper())

#####################

#///////////////////////////////////////////////////

#####################

#Exercise 2:
#Write a program to prompt for a file name, and then read
#through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#values from these lines. When you reach the end of the file, print out
#the average spam confidence

##################

#solution:-

file_read=input('Enter the file name:')
file=open(file_read)
tot=0
cnt=0
for line in file:
    if line.startswith('X-DSPAM-Confidence'):
        str=line.strip().split(':')[1]
        num=float(str)
        cnt+=1
        tot+=num
avg=float(tot/cnt)
print('Average spam confidence',avg)

#Test the program on the mbox.txt and mbox-short.txt files.

##################

#///////////////////////////////////////////////////////

##################

#Exercise 3:
#Sometimes when programmers get bored or want to have a
#bit of fun, they add a harmless Easter Egg to their program. Modify
#the program that prompts the user for the file name so that it prints a
#funny message when the user types in the exact file name “na na boo
#boo”. The program should behave normally for all other files which
#exist and don’t exist. Here is a sample execution of the program:

#################

#solutions:-
fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punkd!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

##################
