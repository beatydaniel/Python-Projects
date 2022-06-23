import sqlite3   #imports the module sqlite3

conn =sqlite3.connect('files.db') #creates the database

with conn:      
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )") #Creates a table and a coloumn using string value, also cannot be created if it exists
    conn.commit()
conn.close() #closes the database 

conn = sqlite3.connect('files.db') #connects to the database

with conn:
    cur = conn.cursor()
    fileList = ('information.docx','Hello.txt','myImage.png',\ #list of files
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for file in fileList: #calling file list and using a new variable file
        if file.endswith('.txt'): #after looking in fileList gathers all that end with .txt
            cur.execute("INSERT INTO tbl_files(col_file) VALUES(?)",
                        (file,)) #inserts the data from the variable file and inserts into the coloum_file
            print(file) #prints the result of file
        conn.commit()
conn.close()
