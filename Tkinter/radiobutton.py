#use of radiobutton: it allows users to have many possible selection options,but let users to select only one. 

from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Language Selection")


def click_me():
    messagebox.showinfo("Selection","You Selected " +str(i.get()))

i=StringVar(value="Nothing")                 # it is done so their is nothing selection from start

l1=Label(root,text="Select ur favourite language")
r1=Radiobutton(root,text='PYTHON',value='PYTHON',variable=i).pack(anchor=W)
r2=Radiobutton(root,text='JAVA',value='JAVA',variable=i).pack(anchor=W)
r3=Radiobutton(root,text='C',value='C',variable=i).pack(anchor=W)
r4=Radiobutton(root,text='C++',value='C++',variable=i).pack(anchor=W)

b1=Button(root,text="Click",command=click_me).pack(anchor=W)

root.mainloop()
#checkbutton in tkinter
