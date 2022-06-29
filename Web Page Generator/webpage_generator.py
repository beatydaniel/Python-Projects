from tkinter import *
import tkinter as tk
import webbrowser

def create():
    f = open("webpage.html","w")
    text='''<html>
        <body>
            <h1>
            Stay tuned for our amazing summer sale!
             </h1>
        </body>
    </html>'''
    f.write(text)
    f.close()
    webbrowser.open_new_tab("webpage.html")

class window(Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.pack(side=TOP,anchor=NW)
        self.master.title("Create HTML")
        self.master.geometry('500x200')
        self.e1= Entry(self, text ="")
        self.e1.grid(row = 0, column = 1, columnspan = 2, padx=(30,0),pady=(30,0), sticky = N+E+S+W)
        self.e2= Entry(self, text ="")
        self.e2.grid(row = 1, column = 1, columnspan = 2, padx=(30,0),pady=(30,0),sticky = N+E+S+W)
        self.b1 = Button(self,text="Create New Webpage",width =20,command=lambda:create())
        self.b1.grid(row=0,column=0,padx=(30,0),pady=(30,0),sticky = N+E)
        self.b2 = Button(self, text="Create New Body",width = 20, command=lambda:body())
        self.b2.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky = N+E)
        self.b3 = Button(self, text="Open HTML",width = 20, command=lambda:open())
        self.b3.grid(row=2, column=0,padx=(30,0),pady=(30,0),sticky = N+E)

        
def main():
    window().mainloop()

if __name__ == '__main__':
    main()
    
