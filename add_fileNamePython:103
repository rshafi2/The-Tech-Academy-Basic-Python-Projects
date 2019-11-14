import sqlite3


 # the conn variable is going to hold our connection 
 # when we connect to a database
 # with loop meaning while we have the connection
 # do the following lines of code after with
 # cur or cursor is what actually operating on the database
 # when we want to invoke commands or do something we would call on the
 # cursor to do it 

fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

        
conn = sqlite3.connect('pyassign103.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Assign103(\
     ID INTEGER PRIMARY KEY AUTOINCREMENT,\
     col_info VARCHAR \
     ) ")
    conn.commit()


conn = sqlite3.connect('pyassign103.db')

for files in fileList:
        cur = conn.cursor()
        if files.find(".txt", len(files) - 4) > -1:
            strSQL = 'INSERT INTO tbl_Assign103(col_info) VALUES (\'' + f'{files}' + '\')'
            # print(strSQL)
            cur.execute(strSQL)
            print("{}".format(files))
            conn.commit()

conn.close()
