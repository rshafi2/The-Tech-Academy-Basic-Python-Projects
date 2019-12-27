from tkinter import *
import tkinter as tk

import gui123
import func123
                        

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
    
        self.master = master
        self.master.minsize(390,230) 
        self.master.maxsize(390,230)
        self.master.title("Files Transfer")
        self.master.configure(bg="#F0F0F0")
        func123.center_window(self,400,300)
        
#GUI widgets connected to the program functions

        gui123.window_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
