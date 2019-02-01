#!/usr/bin/env python3

# Mass File Names lists

massDis = ['Sat 5pm', 'Sun 8:30am', 'Sun 11am', 'Sun 5pm']

massFile = ['sat-5pm', 'sun-830am', 'sun-11am', 'sun-5pm']

mass = [massDis, massFile]

def getMassFileName(sdisplay):
    number = 0
    for mass in massDis:
        if sdisplay == mass:
            return massFile[number]
        else:
            number = number + 1
