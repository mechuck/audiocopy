#!/usr/bin/env python3


clergyDisplay = ['Father Ben', 'Father Reggie', 'Mike Lowe', 
            'Joe Rodriguez', 'Jim Pasker', 'Jim Ineck', 'Terry Nelson',
            'Clyde Brinegar', 'Bishop Peter', ' Father Muha', 'Father Loucks',
            'Father Lankenau', 'Bruno Segatta', 'Father Enrique']

clergyFile = ['fr-ben', 'fr-reggie', 'dcn-mike-lowe', 
            'dcn-joe-rodriguez', 'dcn-jim-pasker', 'dcn-jim-ineck', 'dcn-terry-nelson',
            'dcn-clyde-brinegar', 'bishop-peter', 'fr-muha', 'fr-loucks', 
            'fr-lankenau', 'fr-bruno-segatta', 'fr-enrique']

clergy = [clergyDisplay, clergyFile]

# print("The clergy's name = " + clergy[0][0] + " and " +
#    "their file name will be: " + clergy[1][0])


def getFileName(sname):
    number = 0
    for name in clergyDisplay:
        if sname == name:
            return clergyFile[number]
        else:
            number = number + 1

file = getFileName(clergyDisplay[3])
print(file)
