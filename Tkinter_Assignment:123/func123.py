from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import time
import shutil
import sqlite3

import main123
import func123




#Get the window centered on the screen

def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo





#Source Directory 

def search_sourceDir(self):
    
    source_path=filedialog.askdirectory(initialdir=os.getcwd(),title='Pick a directory')
    if source_path:
        self.txtSource.insert(INSERT,source_path)
        self.source_dir = source_path


   
#Destination Directory 
                                
def search_destDir(self):
    
    dest_path=filedialog.askdirectory(initialdir=os.getcwd(),title='Pick a directory')
    if dest_path:
         self.txtDestination.insert(INSERT,dest_path)
         self.dest_dir = dest_path    


         
                
def work_with_files(self):

    #Warning message if directories have not been selected 
    if len(self.txtSource.get("1.0", "end-1c")) == 0:
        messagebox.showwarning("Warning", "You have not selected both directories!")
    elif len(self.txtDestination.get("1.0", "end-1c")) == 0:
        messagebox.showwarning("Warning", "You have not selected both directories!") 



        
    #Database Creation 
    conn = sqlite3.connect('files.db')

    with conn:
         cur = conn.cursor()
         cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname VARCHAR(25), \
            col_mtime VARCHAR(50) \
          )")
         conn.commit()
    conn.close()


    

    #File Transfer   
    fList = os.listdir(self.source_dir)
    for f in fList:
        if f.endswith('.txt'):
            txt_files_source = os.path.join(self.source_dir,f) 
            txt_files_dest = os.path.join(self.dest_dir,f) 
            shutil.move(txt_files_source,txt_files_dest)
            file_name=os.path.basename(txt_files_dest)
            mod_time = time.localtime(os.path.getmtime(txt_files_dest)) 
            fm_time = time.strftime("%m/%d/%Y, %H:%M:%S", mod_time)  
            print("File Name:", file_name.upper(),"was modified on", fm_time)

            
            conn = sqlite3.connect('files.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fname,col_mtime) VALUES (?,?)",(file_name,fm_time,))
                conn.commit()
            conn.close()

    
            
if __name__ == "__main__":
    pass
