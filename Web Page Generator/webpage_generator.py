from tkinter import *
import tkinter as tk
import webbrowser

class window(Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.pack(side=TOP,anchor=NW) #sets my buttons to the top left of the GUI
        self.master.title("Create HTML")
        self.master.geometry('500x200') #size of the window
        self.e1= Entry(self, text ="") #input for the body
        self.e1.grid(row = 1, column = 1, columnspan = 2, padx=(30,0),pady=(30,0),sticky = N+E+S+W)
        self.b2 = Button(self, text="Generate Webpage",width = 20, command=lambda:create(self))
        self.b2.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky = N+E)
        def create(self): 
            f=open('webpage.html','w') 
            text1='''<html>
        <body>
            <h1>
            Stay tuned for our amazing summer sale!
             </h1>
             '''
            text2 =self.e1.get() #inputs the text entry into the html body

            text3= '''
        </body>
            </html>'''
            f.write(text1+text2+text3)
            f.close()

            webbrowser.open_new_tab('webpage.html')

        
def main():
    window().mainloop()

if __name__ == '__main__':
    main()
    
