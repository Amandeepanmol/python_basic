#basics of messagebox

from tkinter import *
from tkinter import messagebox
root=Tk()


def show():
    messagebox.showinfo("Message Box","Hello everyone")
    messagebox.showerror("Message Box","Hello everyone")
    messagebox.showwarning("Message Box","Hello everyone")
    messagebox.askquestion("Message Box","Hello everyone")
    messagebox.askyesno("Message Box","Hello everyone")
    messagebox.showokcancel("Message Box","Hello everyone")
     # all the messagebox will appear one by one
        
b1=Button(root,text='popup',command=show).pack()

root.mainloop()
