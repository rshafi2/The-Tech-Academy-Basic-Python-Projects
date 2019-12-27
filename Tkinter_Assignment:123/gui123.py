from tkinter import *
import tkinter as tk

import main123
import func123


def window_gui(self):
    
        
    self.btnSource = Button(self.master, text="Source Dir", width=10, font=("Helvetica",10), fg='black', command=lambda: func123.search_sourceDir(self))
    self.btnSource.grid(row=1, column=0, padx=20, pady=40)
        
    self.btnDestination = Button(self.master, text="Destination Dir", width=12, font=("Helvetica",10), fg='black', command=lambda: func123.search_destDir(self))
    self.btnDestination.grid(row=2, column=0, padx=20)

    self.txtSource = Text(self.master,width=20, height=1, font=("Helvetica",11), fg='black',bg='white')
    self.txtSource.grid(row=1, column=1, padx=10, sticky=E)
      
    self.txtDestination = Text(self.master, width=20, height=1, font=("Helvetica",11), fg='black',bg='white')
    self.txtDestination.grid(row=2, column=1, padx=10, sticky=E)

    self.btnTransfer = Button(self.master, text="MOVE", width=7, height=1, font=("Helvetica",12), fg='black', bg='lightgrey', command=lambda: func123.work_with_files(self))
    self.btnTransfer.grid(row=3, column=1, padx=10, pady=20, sticky=E)


if __name__ == "__main__":
    pass
