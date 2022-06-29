import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import shutil
import os
import datetime
from datetime import timedelta

class window(Frame):
    
         
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Check Files")
        self.master.geometry('500x200')
        self.e1= Entry(self, text = "")
        self.e1.grid(row = 0, column = 1, columnspan = 2, padx=(30,0),pady=(20,0), sticky = N+E+S+W)
        self.e2= Entry(self, text = "",)
        self.e2.grid(row = 1, column = 1, columnspan = 2, padx=(30,0),pady=(20,0),sticky = N+E+S+W)
        self.b1 = Button(self, text = "Browse...",width = 15,command=lambda:path(self))
        self.b1.grid( row = 0, column = 0, padx=(30,0),pady=(20,0), sticky = W)
        self.b2 = Button(self, text = "Browse...",width = 15,command=lambda:path2(self))
        self.b2.grid( row = 1, column = 0, padx=(30,0),pady=(20,0), sticky = W)
        self.b3 = Button(self, text = "Check for files...",width = 15,height = 2,command=lambda:check(self))
        self.b3.grid( row = 2, column = 0, padx=(30,0),pady=(30,0), sticky = W)
        self.b4 = Button(self, text = "Close Program", width = 15, height = 2)
        self.b4.grid( row = 2, column = 2, padx=(200,0),pady=(30,0),sticky = E)

        def path(self):
            filepath = fd.askdirectory()
            self.e1.insert(0,filepath)

        def path2(self):
            filepath = fd.askdirectory()
            self.e2.insert(0,filepath) #inserts the directory info into the textbox

        def check(self):
            source = self.e1.get() #gets whats inside the entry1
            destination = self.e2.get() #gets whats inside the entry2
            files = os.listdir(source) #gets whats inside the directory

            for i in files:
                filepath = os.path.join(source,i)
                twentyfour = datetime.datetime.now()-timedelta(hours=24) #sets the variable to be within 24 hours
                filemodtime = os.path.getmtime(filepath) #gets the time of the source directory
                filemodification = datetime.datetime.fromtimestamp(filemodtime) #collects the modification time from the
                if  twentyfour < filemodification : #sets it to only transfer files that are less than 24hours
                    shutil.copy(filepath,destination) #copies the files from the sourse directory to the destination directory
            
def main():
    window().mainloop()



if __name__ == '__main__':
    main()


