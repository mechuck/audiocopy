#!/usr/bin/env python3

# create a new ini file


line1 = "import: E:/Documents/My Church/Homilies/12-24-2015/raw/"
line2 = "library: E:/Documents/My Church/ Homilies/"


f = open("settings.ini", "x")
f.write(line1)
f.write(line2)


