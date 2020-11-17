# use of checkbutton

from tkinter import*
root=Tk()

def click_me():
    myLabel=Label(root,text=i.get()).pack()

i=StringVar()
c=Checkbutton(root,text='Konnichiwa',variable=i,onvalue='ON',offvalue='OFF')
c.deselect()
c.pack()
b=Button(root,text='Click Me',command=click_me).pack()
root.mainloop()
