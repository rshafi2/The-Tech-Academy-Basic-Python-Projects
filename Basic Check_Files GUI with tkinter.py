#
#
# Python Version: 3.7.4
#
#
# Author: Mohammad Shafi 
#
#
# Purpose: Creating a basic GUI using tkinter. The GUI contains few button and entry widgets.   
#
#
# Tested OS: This Code was written and tested to work with Windows 10. 
#
#



import tkinter
from tkinter import *




class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        
        # self.master here is the parent window and the options are affecting the properties of the window. 
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490, 200))
        self.master.title('Check files')
        self.master.config(bg='lightgray')



        """The following lines of code below allows us to add different widgets inside of the
           Parent Window and places them in the window using the grid method."""


        # The following lines of code are for the four BUTTON WIDGETS inside of the Parent Window of the GUI. 
        
        
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1) 
        self.btnBrowse1.grid(row=1, column=1, padx=(10,0) , pady=(30,0), sticky=NW)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=2, column=1, padx=(10,0) , pady=(30,0), sticky=NW)

        self.btnCheckForFiles = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheckForFiles.grid(row=3, column=1, padx=(10,0) , pady=(30,0), sticky=SW)

        self.btnCloseProgram = Button(self.master, text="Close Program", width=12, height=2)
        self.btnCloseProgram.grid(row=3, column=3, padx=(30,0), pady=(30,0), sticky=E)

        

        # The following lines of code are for the two ENTRY WIDGETS inside of the Parent Window of the GUI.
        
        
        self.txtFName = Entry(self.master,text='', font=("Helvetica", 13), fg='black', bg='white', width="35")
        self.txtFName.grid(row=1, column=3,padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text='', font=("Helvetica", 13), fg='black', bg='white', width="35" )
        self.txtLName.grid(row=2, column=3, padx=(30,0), pady=(30,0))


       




if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() 
