class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        
        # self.master here is the parent window and the options are affecting the properties of the window. 
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(390, 100))
        self.master.title('Open Directory')
        self.master.config(bg='lightgray')



        """The following lines of code below allows us to add different widgets inside of the
           Parent Window and places them in the window using the grid method."""


        # The following lines of code are for the BUTTON WIDGET inside of the Parent Window of the GUI. 
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1, command=self.browse) 
        self.btnBrowse1.grid(row=1, column=1, padx=(10,0) , pady=(30,0), sticky=NW)
   

        # The following lines of code are for the ENTRY WIDGET inside of the Parent Window of the GUI.
        self.txt = Entry(self.master,text='', font=("Helvetica", 13), fg='black', bg='white', width="25")
        self.txt.grid(row=1, column=3,padx=(30,0), pady=(30,0))


        """ The function below allows you to browse the computers directory and
           inserts the chosen directory path into the entry widget. """

    def browse(self):
        #msgBox = tkinter.messagebox.askquestion("Do you want to pick a directory?")
        msgBox = messagebox.askquestion(message='Do you want to select a directory?', icon='question', title='Open Directory')
        if msgBox == 'yes':
            dirname = filedialog.askdirectory(parent=self.master,initialdir="/")
            self.txt.insert(0, dirname) 
        else:
            self.master.destroy()
        
        
       




if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() 
