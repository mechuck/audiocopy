# Audio Copy Pro

Version 0.4

Audio Copy Pro is a graphically displayed version of the Audio Copy - Basic app. It is intended to aid in the workflow of processing recorded audio from an external recorder, like a memory stick or USB drive.

## About

Created by Chuck Nelson

Written in Python using Tkinter.

## Change Notes

Please see the document /docs/todo.md for more information on the changes and our to do list.OB

## Version Notes

* Version 0.4 - 2/3/2019 - Added the following features:

  * Created a Status bar at the bottom of the window which contains information, Library Folder, Program Status, and a progress bar that functions while the application is copying files.

  * Decrease window size to 1280x650.

  * Removed the "Save Mass Info" menu item from the File menu options. This option is now automatically done after it copies all the selected files over, see version 0.1.

* Version 0.3 - 2/3/2019 - Added the following features:

    * DONE: 2/3/2019 by Chuck Nelson - Removed the settings.ini file from the repo as it is no longer being used.

    * DONE: 2/3/2019 by Chuck Nelson - Fixed bug where program would stop during the "Copy Files" process. This was caused by the program trying to create a new directory when one already exists. So now it checks to see if the directory already exists and if it does it alerts the user with a message box warning and then exits the method.

    * Done: 2/3/2019 by Chuck Nelson - Create the reset form function, have it called when called from the File/Reset Form option. Also have it called after pressing the "Delete" button, but also have it recall the check device right after the destroy.

    * Done: 2/2/2019 by Chuck Nelson - Make the delete button delete the files on the card.

* Version 0.2 - Added the ability to save Import / Library (export) folder paths into the program for use on next program start up. 1/31/2019

* Version 0.1 - Basic working program, minimum viable product. Copies, renames.
