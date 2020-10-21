#Exercise 1:
#Change the socket program socket1.py to prompt the user
#for the URL so it can read any web page. You can use split('/') to
#break the URL into its component parts so you can extract the host
#name for the socket connect call. Add error checking using try and
#except to handle the condition where the user enters an improperly
#formatted or non-existent URL.


####################################################

#solution:-

import socket

i_url=input('enter the weblink:' )

try:
    host_name=i_url.split('/')[2]
    mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect((host_name,80))
    cmd='GET '+i_url+' HTTP/1.0\r\n\r\n'
    cmd=cmd.encode()
    mysock.send(cmd)
except:
    print('please enter a valid URL')
    exit()

while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()

########################################################

#/////////////////////////////////////////////////////////////////////////////

#######################################################

#Exercise 2:
#Change your socket program so that it counts the number
#of characters it has received and stops displaying any text after it has
#shown 3000 characters. The program should retrieve the entire document
# and count the total number of characters and display the count
#of the number of characters at the end of the document.

######################################################

#solution:-


import socket

i_url=input('enter the weblink:' )

try:
    host_name=i_url.split('/')[2]
    mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect((host_name,80))
    cmd='GET '+i_url+' HTTP/1.0\r\n\r\n'
    cmd=cmd.encode()
    mysock.send(cmd)
except:
    print('please enter a valid URL')
    exit()

recieved =b""
while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    recieved += data
recieved = recieved.decode()
print(recieved[:3000])
print(len(recieved))
mysock.close()


########################################################

#////////////////////////////////////////////////////////////////////////////

########################################################

#Exercise 3:
#Use urllib to replicate the previous exercise of (1) retrieving
#the document from a URL, (2) displaying up to 3000 characters, and
#(3) counting the overall number of characters in the document. Don’t
#worry about the headers for this exercise, simply show the first 3000
#characters of the document contents.


#######################################################

#solution:-

import urllib.request
url_get=input('enter the URL::')
fhand=urllib.request.urlopen(url_get).read()
fhand=fhand.decode()
print(fhand[:3000])
print(len(fhand))

#######################################################

#///////////////////////////////////////////////////////////////////////////

######################################################


#Exercise 4:
#Change the urllinks.py program to extract and count paragraph (p) tags from
#the retrieved HTML document and display the
#count of the paragraphs as the output of your program. Do not display
#the paragraph text, only count them. Test your program on several
#small web pages as well as some larger web pages.

#########################################################

#solutions:-

import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('ENTER-')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
#Retriever all of the paragraph tags
tags=soup('p')
print(len(tags))

######################################################

#//////////////////////////////////////////////////////////////////////////

######################################################

#Exercise 5:
#(Advanced) Change the socket program so that it only shows
#data after the headers and a blank line have been received. Remember
#that recv receives characters (newlines and all), not lines

######################################################

#solutions:-



#(-------------will be added soon----------)
