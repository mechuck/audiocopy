#!/usr/bin/env python3

# create a new ini file
title = "Mass File Names\n"
under = "-----------------------\n"
date1 = "Saturday - 1/20/2019\n"
date2 = "Sunday - 1/21/2019\n"
line1 = "Testing line 1 of file\n"
line2 = "Testing line 2 of file\n"
lines = [title, under, date1, date2, line1, line2]
print(lines)

f = open("filenames.txt", "x")
for line in lines:
    f.write(line)
