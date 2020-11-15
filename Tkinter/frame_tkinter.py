#creating frame in tkinter


from tkinter import*
root=Tk()
frame=LabelFrame(root,padx=50,pady=50)   #frame creation
frame.pack(padx=10,pady=10)

#button creation
b=Button(frame,text="Wish u a very Happy Diwali!!!",fg='green')
b.grid(row=0,column=0)
b1=Button(frame,text="Thanks for visting Tkinter folder of my github",fg='brown')
b1.grid(row=1,column=0)
b2=Button(frame,text="Please star my repository if u find it helpful",fg='blue')
b2.grid(row=2,column=0)

b3=Button(root,text="Exit",command=root.quit)
b3.pack()

root.mainloop()
