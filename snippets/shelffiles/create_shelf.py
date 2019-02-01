#!/usr/bin/env paython3
# Shelf files can store program variables

import shelve

settings = shelve.open('settings')
importFolder = "E:/Documents/My Church/Homilies/card/music"
exportFolder = "E:/Documents/My Church/Homilies/test"
directory1 = "Captured/"
directory2 = "Edited/"
directory3 = "WebReady/"
settings['import'] = importFolder
settings['export'] = exportFolder
settings['dir1'] = directory1
settings['dir2'] = directory2
settings['dir3'] = directory3
settings.close()
