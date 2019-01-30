#!/usr/bin/env python3

# read in settings.ini

import csv

with open('settings.ini') as settingfile:
    readCSV = csv.reader(settingfile, delimiter=';')

    settingName = []
    settingValue = []
    settings = {}

    for row in readCSV:
        a1 = row[0].rstrip()
        a2 = row[1].lstrip()
        settings[a1] = a2



print(settingName)
print("-------------------")
print(settings)
print("Import Directory: " + settings["import"])

print("Library Directory: " + settings["library"])
