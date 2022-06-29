from tkinter import *
import tkinter as tk
import webbrowser

class window(Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.pack(side=TOP,anchor=NW) #sets my buttons to the top left of the GUI
        self.master.title("Create HTML")
        self.master.geometry('500x200') #size of the window
        self.e1= Entry(self, text ="") #input for Webpage name
        self.e1.grid(row = 0, column = 1, columnspan = 2, padx=(30,0),pady=(30,0), sticky = N+E+S+W)
        self.e2= Entry(self, text ="") #input for the body
        self.e2.grid(row = 1, column = 1, columnspan = 2, padx=(30,0),pady=(30,0),sticky = N+E+S+W)
        self.b1 = Button(self,text="Create New Webpage",width =20,command=lambda:create(self)) #submits the entry by calling the function
        self.b1.grid(row=0,column=0,padx=(30,0),pady=(30,0),sticky = N+E)
        self.b2 = Button(self, text="Create New Body",width = 20, command=lambda:create(self))
        self.b2.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky = N+E)
        self.b3 = Button(self, text="Open HTML",width = 20, command=lambda:openp(self))
        self.b3.grid(row=2, column=0,padx=(30,0),pady=(30,0),sticky = N+E)
        def create(self): 
            webpage=self.e1.get() # accesses the input from the entry 
            f=open(webpage,'w') #
            text1='''<html>
        <body>
            <h1>
            Stay tuned for our amazing summer sale!
             </h1>
             '''
            text2 =self.e2.get() #inputs the text entry into the html body

            text3= '''
        </body>
            </html>'''
            f.write(text1+text2+text3)
            f.close()
            

        def openp(self):# opens the webpage
            webpage=self.e1.get()
            webbrowser.open_new_tab(webpage)
        
def main():
    window().mainloop()

if __name__ == '__main__':
    main()
    
