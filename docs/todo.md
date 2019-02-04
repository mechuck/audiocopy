# Audion Copy - Pro: To Do List

## Features to Add

### Still To Do

* The Directories on import feature, can also be used to

### Completed

* Done: 2/3/2019 (v. 0.4) by Chuck Nelson - Created a Status bar at the bottom of the window which contains information, Library Folder, Program Status, and a progress bar that functions while the application is copying files.

* Done: 2/3/2019 (v. 0.4) by Chuck Nelson - Decrease window size to 1280x650.

* Done: 2/3/2019 (v. 0.4) by Chuck Nelson - Removed the "Save Mass Info" menu item from the File menu options. This option is now automatically done after it copies all the selected files over, see version 0.1.

* DONE: 2/3/2019 by Chuck Nelson - Removed the settings.ini file from the repo as it is no longer being used.

* DONE: 2/3/2019 by Chuck Nelson - Fixed bug where program would stop during the "Copy Files" process. This was caused by the program trying to create a new directory when one already exists. So know it checks to see if the directory already exists and if it does it alerts the user with a message box warning and then exits the method.

* Done: 2/3/2019 by Chuck Nelson - Create the reset form function, have it called when called from the File/Reset Form option. Also have it called after pressing the "Delete" button, but also have it recall the check device right after the destroy.

* Done: 2/2/2019 by Chuck Nelson - Make the delete button delete the files on the card.

* Done: 1/31/2019 by Chuck Nelson - Get the above directories to save when changed.

* DONE: 1/31/2019 by Chuck Nelson - Complete the Save Mass Filenames to file in the directory the files were copied.

* Done: 1/31/2019 by Chuck Nelson - Get the commands to set the directory for the card, and library to function



## Other Changes Notes

# 02/2/2019

Added titles to the import and export / library dialogue boxes to identify their purpose.

# 01/31/2019

Changing from a settings.ini file to a using a "dat", or shelve file to store settings for the application. The file will be named settings.dat and on windows it will contain a "settings.bak" and "settings.dir" file.

Removing all code using or calling the settings.ini file
