#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))
   

contents = []

srchstr = 'C:\\Users\\mysti\\Coding\\BFFMaker\\'

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".m3u"):

            contents.append(filepath)

sizdict = {}

for x in range(5):

    pl = []

    infile = open(contents[x], "r")

    plist = infile.readline()

    while plist:
        pl.append(plist.strip())
        plist = infile.readline()

    infile.close()

    sizdict[contents[x]] = len(pl)

filst = []

filst = sorted(sizdict, key=sizdict.get, reverse=False)

print(sizdict)

print(filst)

limlen = sizdict[contents[4]]

print(limlen)

pl1 = []

elem = contents[0]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl1.append(plist.strip())
    plist = infile.readline()

infile.close()

pl2 = []

elem = contents[1]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl2.append(plist.strip())
    plist = infile.readline()

infile.close()

pl3 = []

elem = contents[2]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl3.append(plist.strip())
    plist = infile.readline()

infile.close()

pl4 = []

elem = contents[3]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl4.append(plist.strip())
    plist = infile.readline()

infile.close()

pl5 = []

elem = contents[4]

infile = open(elem, "r")

plist = infile.readline()

while plist:
    pl5.append(plist.strip())
    plist = infile.readline()

infile.close()

spl = []

for x in range(limlen):
    spl.append(pl1[x])
    spl.append(pl2[x])
    spl.append(pl3[x])
    spl.append(pl4[x])
    spl.append(pl5[x])

oustr = "Shuffled_Playlist.txt"

outfile = open("temp.txt", "w")

for elem in spl:
    outfile.write(elem + '\n')

outfile.close()   

outfile = open(oustr, "w")

with open("temp.txt") as f: 
    for line in f: 
        if not line.isspace(): 
            #sys.stdout.write(line)
            outfile.write(line)

outfile.close()

## THE GHOST OF THE SHADOW ##




