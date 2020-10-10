#Exercise 1:
#Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the number of
#messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits.

############################################################

#solution:-

iread=input('enter the file : ')
fread=open(iread)

oxford=dict()
for line in fread:
    if line.startswith('From '):
        id=line.rstrip().split()[1]
        oxford[id]=oxford.get(id,0)+1   #counting and adding to dict

lst=list()
for email,count in oxford.items():
    tmp=(count,email)                   #storing value in reverse order
    lst.append(tmp)
lst=sorted(lst,reverse=True)            #sort by highest value
for count,email in lst[:1]:             #displaying only largest value
    print(email,count)

###########################################################

#//////////////////////////////////////////////////////////////////////////

###########################################################

#Exercise 2:
#This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.

##########################################################

#solution:-

iread=input('enter the file : ')
fread=open(iread)

oxford=dict()
for line in fread:
    if line.startswith('From '):
        word=line.rstrip().split()[5]
        hour=word.split(':')[0]
        oxford[hour]=oxford.get(hour,0)+1

lst=list()
for k,v in oxford.items():
    temp=(k,v)
    lst.append(temp)
lst=sorted(lst)
for k,v in lst:
    print(k,v)

###########################################################

#//////////////////////////////////////////////////////////////////////////

##########################################################

#Exercise 3:
#Write a program that reads a file and prints the letters
#in decreasing order of frequency. Your program should convert all the
#input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters
#a-z. Find text samples from several different languages and see how
#letter frequency varies between languages. Compare your results with
#the tables at https://wikipedia.org/wiki/Letter_frequencies.

####################################################


#solutions:-

import string
import re
iread=input('Enter a file name:')
fread=open(iread)

oxford=dict()
for line in fread:
    line = re.sub('[\W_]+', '', line)
                #regular expression operations(next chapter)
                #removes every other character except alhabets and digits
    line = line.translate(str.maketrans('', '', string.digits))
                #to remove all digits from the string
    line = line.lower()
                #make the strng all lowercase
    for word in line:
        for letter in word:
            oxford[letter]=oxford.get(letter,0)+1
                #store all the alphabets and their frequency in key value format
lst=list()
for key,value in oxford.items():
    temp=(value,key)
    lst.append(temp)
                #store the alphabet and their frequency in reverse order ,
                # so that easy to print in decreasing oder as per question
lst=sorted(lst,reverse=True)

for key,value in lst:
    print(value,key)
                #again reversing the oder of prining


#######################################################
