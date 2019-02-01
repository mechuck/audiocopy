#!/usr/bin/env python3
# Testing shelve files

import shelve

#opening shelve file
settings = shelve.open('settings')
importFolder = settings['import']
print("Import Folder: " + importFolder)
exportFolder = settings['export']
print("Export Folder: " + exportFolder)
dir1 = settings['dir1']
dir2 = settings['dir2']
dir3 = settings['dir3']
print("Directory 1: " + dir1)
print("Directory 2: " + dir2)
print("Directory 3: " + dir3)
settings.close()
