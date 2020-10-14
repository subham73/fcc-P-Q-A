#Exercise 2:
#Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter).

###################################

#solutions:-

iread=input('enter the file name: ')
fread=open(iread)

oxford=dict()
for line in fread:
    if line.startswith('From '):
        n_line=line.rstrip().split()
        word=n_line[2]
        oxford[word]=oxford.get(word,0)+1
print(oxford)

####################################

#/////////////////////////////////////////////////////////////////////////

####################################

#Exercise 3:
#Write a program to read through a mail log, build a histogram using a dictionary
#to count how many messages have come from each email address,
#and print the dictionary.

#####################################


#solutions:-

iread=input('enter the file : ')
fread=open(iread)

oxford=dict()
for line in fread:
    if line.startswith('From '):
        id=line.rstrip().split()[1]
        oxford[id]=oxford.get(id,0)+1

print(oxford)

#####################################

#/////////////////////////////////////////////////////////////////////////

#####################################

#Exercise 4:
#Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the
# dictionary has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.

####################################

#solution:-

iread=input('enter the file : ')
fread=open(iread)

oxford=dict()
for line in fread:
    if line.startswith('From '):
        id=line.rstrip().split()[1]
        oxford[id]=oxford.get(id,0)+1

maxkey=None
maxval=None
for key,value in oxford.items():
    if maxval is None or  value > maxval:
        maxval=value
        maxkey=key
print (maxkey,maxval)


######################################

#//////////////////////////////////////////////////////////////////////

######################################

#Exercise 5:
#This program records the domain name (instead of the
#address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print
#out the contents of your dictionary.

#######################################


#solutions:-

iread=input('enter the file : ')
fread=open(iread)

oxford=dict()
for line in fread:
    if line.startswith('From '):
        n_line=line.rstrip().split()[1]
        word=n_line.split('@')[1]
        oxford[word]=oxford.get(word,0)+1

print (oxford)

########################################
