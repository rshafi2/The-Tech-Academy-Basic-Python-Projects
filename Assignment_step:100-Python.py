import os


import time

path =  'C:\\A\\'

for files in os.listdir(path):
    if files.endswith('.txt'):
        txt_files = os.path.join(path, files)
        print(txt_files.upper(),"- Modified on", time.ctime(os.path.getmtime(txt_files)))
