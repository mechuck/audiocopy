#!/usr/bin/env python3

# Copyright 2019 by Chuck Nelson

# *** Module Loads ***
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import csv
from os import path
import shutil
import datetime
import cnfunc as cnf
import homilists as hom
import masses as mas
import shelve
import threading

root = Tk()
directories = []

class formLoad:

    def __init__(self, master):
        self.master = master
        self.master.title('Audio Copy - Pro v0.1')
        self.master.resizable(False, False)
        self.master.geometry("1280x650")
        self.menubar = Menu(master)
        self.master.config(menu = self.menubar)
        self.iQuite = False
        self.testCheckCard = False

        # Window Sytles
        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.style.configure('TLabel', font = ('Arial', 12, 'bold'))
        self.style.configure('TButton', font = ('Times', 12))
        self.style.configure('TCombobox', font = ('Arial', 12))

        # Get Applications Settings
        self.loadSettings()
        self.testCopyFiles = False

        # Create Window Widgets
        self.createMenu(master)
        self.createTopBar(master)
        self.createHeadCanvas(master)
        self.createStatusBar(master)
        # self.createHead()

    # ****************************************************
    # ***                App Settings                  ***
    # ****************************************************
    def loadSettings(self):
        # This will load the application settings from a shelve file.
        global directories
        settings = shelve.open('settings')
        # load import folder
        self.importFolder = settings['import']
        # Load Export folder
        self.exportFolder = settings['export']
        # load directories
        dir1 = settings['dir1']
        dir2 = settings['dir2']
        dir3 = settings['dir3']
        directories = [dir1, dir2, dir3]
        settings.close()


    # ****************************************************
    # ***            Create Window Widgets             ***
    # ****************************************************

    def createTopBar(self, master):
        self.frame_topbar = ttk.Frame(master)
        self.frame_topbar.pack()

        # Elements in the topbar
        ttk.Label(self.frame_topbar, text = " ").grid(row = 0, column = 0)
        ttk.Label(self.frame_topbar, text = 'Card Location').grid(row = 1, column = 0, columnspan = 1)
        self.lbl_cardlocation = ttk.Label(self.frame_topbar, text = self.importFolder)
        self.lbl_cardlocation.grid(row = 2, column = 0, columnspan = 2, padx = 20)
        # Button "Check Card"
        self.btn_checkcard = ttk.Button(self.frame_topbar, text = 'Check Card',
                        command = self.runCheckCard)
        self.btn_checkcard.grid(row = 1, column = 2, rowspan = 2, padx = 20, pady = 5)

        # Button "Copy Files"
        self.btn_copyfiles = ttk.Button(self.frame_topbar, text = 'Copy Files',
                        command = self.startCopyFiles)
        self.btn_copyfiles.grid(row = 1, column = 3, rowspan = 2, padx = 20, pady = 5)
        # Combo Box "Month"
        ttk.Label(self.frame_topbar, text = 'Month').grid(row = 1, column = 4, padx = 20, sticky = "w")
        # Get the current month
        getNow = datetime.datetime.now()
        getMonth = cnf.getMonthFromNum(getNow.month)

        self.month = StringVar(self.frame_topbar, value=getMonth)
        self.cmbo_month = ttk.Combobox(self.frame_topbar, textvariable = self.month)
        self.cmbo_month.grid(row = 2, column = 4, padx = 20, sticky = 'w')
        self.cmbo_month.config(values = ('Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        self.cmbo_month.config(width = 10, font = 'Arial')

        # Combo Box "Day"
        ttk.Label(self.frame_topbar, text = 'Day').grid(row = 1, column = 5, padx = 20, sticky = 'w')
        # get Current day
        cDay = str(getNow.day)
        self.day = StringVar(self.frame_topbar, value=cDay)
        self.cmbo_day = ttk.Combobox(self.frame_topbar, textvariable = self.day)
        self.cmbo_day.grid(row = 2, column = 5, padx = 20, sticky = 'w')
        self.cmbo_day.config(value = ('Day', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                      '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                      '31'))
        self.cmbo_day.config(width = 5, font = "Arial")

        # Entry Box "Year"
        ttk.Label(self.frame_topbar, text = 'Year').grid(row = 1, column = 6, padx = 20, sticky = 'w')
        cYear = getNow.year  # Get current year to auto fill the year
        self.txt_Year = ttk.Entry(self.frame_topbar, width = 5, font = ('Arial', 12))
        self.txt_Year.grid(row = 2, column = 6, padx = 20)
        self.txt_Year.insert(0, cYear)

        # Delete Button
        self.btn_delete = ttk.Button(self.frame_topbar, text = 'Delete',
                            command = self.cmdDelete)
        self.btn_delete.grid(row = 1, column = 7, rowspan = 2, padx = 20, pady = 5)

    def createMenu(self, master):
        # Creates the menu bar at the top of the page.
        # Top Level Items
        global root
        self.file = Menu(self.menubar)
        self.run = Menu(self.menubar)
        self.edit = Menu(self.menubar)
        self.help_ = Menu(self.menubar)

        self.menubar.add_cascade(menu = self.file, label = "File")
        self.menubar.add_cascade(menu = self.run, label = "Run")
        self.menubar.add_cascade(menu = self.edit, label = "Edit")
        self.menubar.add_cascade(menu = self.help_, label = "Help")

        # File Menu Items
        self.file.add_command(label = "Reset Form",
                    command = self.menuSelectResetForm, accelerator = 'Ctrl-R')
        master.bind('<Control-r>', self.menuSelectResetForm)
        self.file.add_separator()
        self.file.add_command(label = "Exit", command = self.menuSelectExit)
        # self.file.add_command(label = "Exit", command = master.destroy)
        self.file.entryconfig('Exit', accelerator = 'Ctrl+Q')
        master.bind('<Control-q>', self.menuSelectExit)

        # Run Menu Items
        self.run.add_command(label = "Check Card", command = self.runCheckCard,
                            accelerator = 'Ctrl-H')
        master.bind('<Control-h>', self.runCheckCard)
        self.run.add_command(label = 'Copy', command = self.startCopyFiles,
                            accelerator = "Ctrl+C")
        master.bind('<Control-c>', self.startCopyFiles)
        self.run.add_command(label = 'Delete', command = self.cmdDelete,
                            accelerator = "Ctrl+D")
        master.bind('<Control-d>', self.cmdDelete)


        # Edit Menu Items
        self.edit.add_command(label = "Import Directory",
                            command = self.mnuImportDirectory)
        self.edit.add_command(label = "Library Directory",
                            command = self.mnuExportDirectory)
        self.edit.add_separator()
        self.edit.add_command(label = "Homily Filenaming Template")
        self.edit.add_command(label = "Mass Filenaming Template")
        self.edit.add_command(label = "Other Filenaming Template")
        self.edit.add_separator()
        self.edit.add_command(label = "Directories on Import")
        self.edit.add_separator()
        self.edit.add_command(label = "Application Settings")
        #Help Menu Items
        self.help_.add_command(label = "Help Topics")
        self.help_.add_separator()
        self.help_.add_command(label = "About Audio Copy Pro")

    def createHeadCanvas(self, master):
        # Creating header canvas for column names
        self.headCanvas = Canvas(master)
        self.headCanvas.config(width = 1100, height = 55)
        self.headCanvas.pack()

        # top seperator line
        self.sepLine1 = self.headCanvas.create_line(1, 25, 1095, 25,
                    fill = 'black', width = 2)

        # columns defined

        self.h1 = self.headCanvas.create_text(10, 40, text = "#",
                    font = ('Courier', 14, 'bold'))
        self.h2 = self.headCanvas.create_text(80, 40, text = "Filename",
                    font = ('Courier', 14, 'bold'))
        self.h3 = self.headCanvas.create_text(270, 40, text = "Import",
                    font = ('Courier', 14, 'bold'))
        self.h4 = self.headCanvas.create_text(390, 40, text = "Homilist",
                    font = ('Courier', 14, 'bold'))
        self.h5 = self.headCanvas.create_text(550, 40, text = "Mass",
                    font = ('Courier', 14, 'bold'))
        self.h6 = self.headCanvas.create_text(750, 40, text = "Homily Filename",
                    font = ('Courier', 14, 'bold'))

        self.sepLine2 = self.headCanvas.create_line(1, 55, 1095, 55,
                    fill = 'black', width = 2)

    def createBodyCanvas(self, filelist):
        # Create new Canvas for Body
        self.filelist = filelist
        self.bodyCanvas = Canvas(self.master)
        self.bodyCanvas.config(width = 1100, height = 300)
        self.bodyCanvas.pack()
        self.linenum = [None]
        self.filename = [None]
        self.importchk = [None]
        self.impchk = [None]
        self.chkbtn = [None]
        self.checkboxval = [None]
        self.homilistCmbo = [None]
        self.clergy = [None]
        self.mass = [None]
        self.selectedMass = [None]
        self.massCmbo = [None]
        self.homilyEntry = [None]
        self.fileCopied = [None]
        file_num = 0
        line_height = 20
        defaulthom = hom.clergy[0][0]
        defaultmas = mas.mass[0][0]

        for x in filelist:
            file_num = file_num + 1
            self.linenum.append(self.bodyCanvas.create_text(10, line_height,
                    text = str(file_num), font = ('Courier', 12)))
            self.filename.append(self.bodyCanvas.create_text(113, line_height,
                    text = x, font = ('Courier', 12)))
            self.checkboxval.append(IntVar())
            self.fileCopied.append(False)
            self.chkbtn.append(ttk.Checkbutton(self.bodyCanvas, text = "add",
                    variable = self.checkboxval[file_num]))
            self.bodyCanvas.create_window(265, line_height, window = self.chkbtn[file_num])
            # Homilist Drop Down
            self.clergy.append(StringVar(self.bodyCanvas, value = defaulthom))
            self.homilistCmbo.append(ttk.Combobox(self.bodyCanvas, textvariable = self.clergy[file_num]))
            self.bodyCanvas.create_window(425, line_height, window = self.homilistCmbo[file_num])
            self.homilistCmbo[file_num].config(value = hom.clergy[0])
            # Masses Drop Down
            self.mass.append(StringVar(self.bodyCanvas, value = defaultmas))
            self.selectedMass.append(ttk.Combobox(self.bodyCanvas, textvariable = self.mass[file_num]))
            self.bodyCanvas.create_window(570, line_height, window = self.selectedMass[file_num])
            self.selectedMass[file_num].config(value = mas.mass[0], width = 11)
            # Homily File name entry box
            self.homilyEntry.append(ttk.Entry(self.bodyCanvas, width = 50, font = ('Arial', 12)))
            self.bodyCanvas.create_window(850, line_height, window = self.homilyEntry[file_num])
            tempText = "Homily Names will populate after copying over files."
            self.homilyEntry[file_num].insert(0, tempText)
            line_height = line_height + 30

        self.testCheckCard = True

    def createStatusBar(self, master):
        self.statusBar = Canvas(self.master, width = 1100, height = 25,
                bd = 3, relief=SUNKEN)
        self.statusBar.pack(side=BOTTOM, fill=X)
        # Library Path Display in Status Bar
        self.librarySBText = "Library: " + self.exportFolder
        self.librarySB = self.statusBar.create_text(10,20, text = self.librarySBText,
            font = ('Courier', 10, 'bold'), anchor=W)
        # Vertical Line
        self.sepLine1 = self.statusBar.create_line(500, 0, 500, 25,
            fill = 'black', width=2)
        # Program Status
        self.status = "Status: Awaiting Orders, Captain"
        self.statusLabel = self.statusBar.create_text(510, 18, text = self.status,
            font = ('Courier', 10, 'bold'), anchor=W)
        # Vertical Line
        self.sepLine1 = self.statusBar.create_line(1025, 0, 1025, 25,
            fill = 'black', width=2)
        # Progress Bar
        self.progressText = self.statusBar.create_text(1035, 18, text = 'Progress:',
            font = ('Courier', 10, 'bold'), anchor=W)
        self.progressBar = ttk.Progressbar(self.statusBar, orient = HORIZONTAL,
            length = 150)
        self.statusBar.create_window(1185, 19, window = self.progressBar)
        return None

    # ****************************************************
    # ***          Interacting with Widgets            ***
    # ****************************************************

    def runCheckCard(self, event = None):
        # get directory from import app seetting
        self.status = "Status: Checking Card . . ."
        self.statusBar.itemconfig(self.statusLabel, text=self.status)
        directory = self.importFolder
        print(directory)
        # get list of files
        filelist = os.listdir(directory)
        # Call the createBodyCanvas to create list of files.
        self.createBodyCanvas(filelist)
        self.status = "Status: Card Checked"
        self.statusBar.itemconfig(self.statusLabel, text=self.status)

    def saveFilenameTextFile(self):
        # Saves the actual filenames text file out to a file
        # Format the contents of the file
        textFileContents = ["Filename List\n"]
        textFileContents.append("-------------------------\n")
        textFileContents.append("\n")
        textFileContents.append(self.dateSaturday)
        textFileContents.append(self.dateSunday)
        textFileContents.append("\n")
        for mline in self.recordFilenamesMass:
            textFileContents.append(mline)
        textFileContents.append("\n")
        for hline in self.recordFilenamesHomily:
            textFileContents.append(hline)
        # Setup file name to write
        filename = self.capturePath + "filenames.txt"
        # Open file to write
        file = open(filename, "x")
        for contentLine in textFileContents:
            file.write(contentLine)
        file.close()

    def startCopyFiles(self):
        # Change the status bar's status label
        self.status = "Status: Copying Files ..."
        self.statusBar.itemconfig(self.statusLabel, text=self.status)
        self.progressBar.config(mode = 'indeterminate')
        self.progressBar.start()
        self.thread = threading.Thread(target = self.runCopyFiles, name = "CopyThread")
        self.thread.start()

    def runCopyFiles(self, event = None):
        # Starts the process of copying files over, but first
        # Test if the user has check the card for files, which therefore would
        # make the chance that there are files selected to copy.
        if self.testCheckCard == False:
            # Display a message that the user needs to run and select files
            # to copy prior to running the Copy Files.
            messagebox.showwarning('Warning!', 'You must run "Check Card" and select files before runing "Copy Files".')
            # Break out of this function as nothing else can be done without checking
            # the card first.
            return
        # else:
        #
        #     # User has already clicked on the Check Card.
        #     # print("Card Already Checked...")
        self.testCopyFiles = True
        self.folderLibCreated = False
        testImport = False
        file_num = 0
        files = self.filelist
        self.recordFilenamesMass = []

        # get Date information
        dm = cnf.getMonthFromText(self.month.get())

        dd = int(self.day.get())
        dy = self.txt_Year.get()

        fdt = dm + "-" + str(dd) + "-" + dy

        # process for Saturday Morning Mass
        if dd == 1:
            datedata = cnf.getMonthDays(dm, dy)
            fsatd = str(datedata[0])
            dy = str(datedata[1])
            dm = str(datedata[2])
            fsdt = dm + "-" + fsatd + "-" + dy
        else:
            fsat = str(dd - 1)
            fsdt = dm + "-" + fsat + "-" + dy
        # print("<<< Import Notes for copy>>")
        # print("Date: " + fdt)
        # print("File to be imported: " + files[file_num])

        # Create Directories
        libPath = self.exportFolder

        # Check to see if the directory has already been created.
        if path.exists(libPath + "/" + fdt):
            # Path Alredy exists need to send up warning to the user
            messagebox.showwarning("Directory Already Exists!",
                        "Unable to process request due to the directory already exists.")
            self.progressBar.stop()
            return None

        self.recordFilenamesHomily = []
        # print(files)
        for x in files:
            # file_num = file_num + 1

            # print(self.filelist[file_num])
            if self.checkboxval[file_num + 1].get() == 1:
                # print('File Selected')

                fimport = self.checkboxval[file_num + 1].get()
                sclergy = self.clergy[file_num + 1].get()
                smass = self.mass[file_num + 1].get()
                fmass = mas.getMassFileName(smass)
                fclergy = hom.getClergyFileName(sclergy)

                if smass == "Sat 5pm":
                    massFileName =  "smk_Mass_" + fsdt + "_" + fmass + ".wav"
                else:
                    massFileName =  "smk_Mass_" + fdt + "_" + fmass + ".wav"
                if smass == "Sat 5pm":
                    fileH = "smk_Homily_" + fsdt + "_" + fmass + "_" + fclergy + ".wav"
                    self.homilyEntry[file_num + 1].delete(0, END)
                    self.homilyEntry[file_num + 1].insert(0, fileH)
                else:
                    fileH = "smk_Homily_" + fdt + "_" + fmass + "_" + fclergy + ".wav"
                    self.homilyEntry[file_num + 1].delete(0, END)
                    self.homilyEntry[file_num + 1].insert(0, fileH)
                # Record Dates in Filename Text File
                self.dateSaturday = "Saturday: " + fsdt + "\n"
                self.dateSunday = "Sunday: " + fdt + "\n"

                if self.folderLibCreated != True:
                    self.capturePath = directoryCreate(libPath, fdt)
                    self.folderLibCreated = True
                # print(self.capturePath)
                # print("----->>>>" + str(self.folderLibCreated))
                src = self.importFolder + "/" + self.filelist[file_num]
                dst = self.capturePath + massFileName
                # print(self.filelist[file_num] + " -- " + src + " -- " + dst)

                # TODO: Uncomment the following line to actually copy files.
                shutil.copyfile(src, dst)
                # Message box that files have not been copied
                # messagebox.showwarning("Copy Files Disabled",
                #         "No files were copied while in test mode.")

                # Write out filenames
                self.fileCopied[file_num + 1] = True
                self.recordFilenamesMass.append(massFileName + "\n")
                self.recordFilenamesHomily.append(fileH + "\n")
            else:
                continue
                # print('File Not Selected')
            # print("----------------------")
            file_num = file_num + 1

        self.saveFilenameTextFile()

        # Change the status bar's status label
        self.status = "Status: File Copying Finished."
        self.statusBar.itemconfig(self.statusLabel, text=self.status)

        # Stop the progress bar
        self.progressBar.stop()

        print(self.fileCopied)
        print(self.filelist)


    def cmdDelete(self):
        # This method deletes files that have already been copied.
        # But first it must check to see if the file was already copied,

        # Check to see if the "Check Card" command has been run
        if not self.testCheckCard:
            # "Check Card" has not been run, no files can be deleted.
            messagebox.showwarning('Warning!', 'No files have been copied.')
            return None
        # Check to see if the user has Copied Files.
        if not self.testCopyFiles:
            messagebox.showwarning('Warning!', "You must copy files before deleting them.")
            return None

        # Change the status bar.
        self.status = "Status: Deleting Files from card ..."
        self.statusBar.itemconfig(self.statusLabel, text=self.status)

        # Process Deleting Files
        fileDeleted = False
        file_num = 0
        for file in self.filelist:
            if self.fileCopied[file_num + 1]:
                os.remove(self.importFolder + "/" + file)
                fileDeleted = True
                print(file + " has been removed.")
            file_num = file_num + 1
        if fileDeleted:
            messagebox.showinfo("Succes!", "Files have been deleted from card.")
        else:
            messagebox.showwarning("File Deletion Failed", "No files were deleted.")

        # Destory the canvas
        self.killBodyCanvas()
        # run the "runCheckCard" function to reload a new list of the filesself.
        self.runCheckCard()

        # update the programs status in the status bar
        self.status = "Status: Files Deleted"
        self.statusBar.itemconfig(self.statusLabel, text=self.status)

        return None

    def killBodyCanvas(self):
        # need to destroy the bodyCanvas widget
        self.bodyCanvas.destroy()

        # Change the status bar's status label
        self.status = "Status: Reset Application"
        self.statusBar.itemconfig(self.statusLabel, text=self.status)
        return None

    def menuSelectResetForm(self, event = None):
        if self.iQuite == False:
            print("Reset Form initiated...")
        #testing
        self.killBodyCanvas()

    def menuSelectExit(self, event = None):
        global root
        root.quit()

    def mnuImportDirectory(self):
        # Set the import directory
        directory = filedialog.askdirectory(title = "Select Import Directory")
        # update card label location
        self.lbl_cardlocation.config(text = directory)
        # update the importFolder location
        self.importFolder = directory
        # Need to save to shelve
        settings = shelve.open('settings')
        settings['import'] = directory
        settings.close()
        return None

    def mnuExportDirectory(self):
        # Ask user for the Export or Library directory
        directory = filedialog.askdirectory(title = "Select Export / Library Directory")
        # update export/library directory exportFolder location
        self.exportFolder = directory
        # Need to save the export / library folder location into shelve file
        settings = shelve.open('settings')
        settings['export'] = directory
        settings.close()

        # update library label in status bar.
        self.librarySBText = "Library: " + directory
        self.statusBar.itemconfig(self.librarySB, text=self.librarySBText)
        return None

def directoryCreate(libPath, sundt):
    # takes the Library Root and date to create folders for the copying of Files
    global formload
    global directories
    dirMainFolder = libPath + "/" + sundt
    os.mkdir(dirMainFolder)
    dirCapture = dirMainFolder + "/" + directories[0]
    os.mkdir(dirCapture)
    os.mkdir(dirMainFolder + "/" + directories[1])
    os.mkdir(dirMainFolder + "/" + directories[2])
    return dirCapture

def main():
    # root = Tk()
    global root
    root.option_add('*tearOff', False)
    formload = formLoad(root)
    root.mainloop()

if __name__ == "__main__": main()
