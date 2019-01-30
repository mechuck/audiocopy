#!/usr/bin/env python3

# Lists for the clergy Homilist drop down menus.

clergyDisplay = ['Father Ben', 'Father Vitalis', 'Mike Lowe',
            'Joe Rodriguez', 'Jim Pasker', 'Jim Ineck', 'Terry Nelson',
            'Clyde Brinegar', 'Bishop Peter', 'Father Muha', 'Father Loucks',
            'Father Lankenau', 'Bruno Segatta', 'Father Enrique', 'Father Radmar']

clergyFile = ['fr-ben', 'fr-vitalis-onyeama', 'dcn-mike-lowe',
            'dcn-joe-rodriguez', 'dcn-jim-pasker', 'dcn-jim-ineck', 'dcn-terry-nelson',
            'dcn-clyde-brinegar', 'bishop-peter', 'fr-muha', 'fr-loucks',
            'fr-lankenau', 'fr-bruno-segatta', 'fr-enrique', 'fr-radmar']

clergy = [clergyDisplay, clergyFile]

def getClergyFileName(sname):
    number = 0
    for name in clergyDisplay:
        if sname == name:
            return clergyFile[number]
        else:
            number = number + 1


# print("The clergy's name = " + clergy[0][0] + " and " +
#    "their file name will be: " + clergy[1][0])
