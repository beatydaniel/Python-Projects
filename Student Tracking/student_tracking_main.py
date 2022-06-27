# Python Ver: 3.10.5
#
#Author: Daniel R. Beaty
#
#Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#         using Tkinter Parent and Child relationships.
#
# Tested OS: This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_tracking_gui
import student_tracking_func

class ParentWindow(Frame):
    def __init__(self,master,*args, **kwargs):
        Frame. __init__(self,master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,400)
        self.master.maxsize(500,400)
        student_tracking_func.center_window(self,600,500)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        student_tracking_gui.load_gui(self)
        

                                  
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
                             
            
                             
