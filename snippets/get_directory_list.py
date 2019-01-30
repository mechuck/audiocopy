#!/usr/bin/env python3
import os

path = "E:/Documents/My Church/Homilies/12-24-2015/Raw/"

test = os.listdir(path)
print(test)

print("This list contains " + str(len(test)) + " files.")

# Loop through list.
y = 0
for x in test:
    y  = y + 1
    print(str(y) + " " +x)
    
