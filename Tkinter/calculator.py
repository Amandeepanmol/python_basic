#basic_calculator

from tkinter import*
root=Tk()                                    #for blank window
root.title("Simple Calculator")              #for keeping title of calculator
root.config(background='yellow')                   #keep background color yellow

e=Entry(root,width=15,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=80,pady=40)


#calculator body
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def clear():
    e.delete(0,END)
    
def add():
    first_no=e.get()
    global f_no
    global choice
    choice="Addition"
    f_no=int(first_no)
    e.delete(0,END)   

def subtract():
    first_no=e.get()
    global f_no
    global choice
    choice="Subtraction"
    f_no=int(first_no)
    e.delete(0,END)

def multiply():
    first_no=e.get()
    global f_no
    global choice
    choice="Multiplication"
    f_no=int(first_no)
    e.delete(0,END)

def division():
    first_no=e.get()
    global f_no
    global choice
    choice="Division"
    f_no=int(first_no)
    e.delete(0,END)
    
def equal():
    second_no=e.get()
    e.delete(0,END)
    
    if(choice=="Addition"):
        e.insert(0,f_no+int(second_no))
    
    elif(choice=="Subtraction"):
        e.insert(0,f_no-int(second_no))
        
    elif(choice=="Multiplication"):
        e.insert(0,f_no*int(second_no))
        
    elif(choice=="Division"):
        e.insert(0,f_no/int(second_no))

    
#Button creation
b1=Button(root,text='1',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(1))
b2=Button(root,text='2',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(2))
b3=Button(root,text='3',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(3))

b4=Button(root,text='4',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(4))
b5=Button(root,text='5',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(5))
b6=Button(root,text='6',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(6))

b7=Button(root,text='7',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(7))
b8=Button(root,text='8',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(8))
b9=Button(root,text='9',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(9))

b0=Button(root,text='0',padx=40,pady=20,fg='black',bg='lightblue',command=lambda: button_click(0))

b_add=Button(root,text='+',padx=39,pady=20,fg='brown',bg='lightblue',command=add)
b_clear=Button(root,text='clear',padx=78,pady=20,fg='orange',bg='lightblue',command=clear)
b_equal=Button(root,text='=',padx=86,pady=20,fg='brown',bg='lightblue',command=equal)


b_subtract=Button(root,text='-',padx=40,pady=20,fg='brown',bg='lightblue',command=subtract)
b_multiply=Button(root,text='*',padx=40,pady=20,fg='brown',bg='lightblue',command=multiply)
b_division=Button(root,text='/',padx=40,pady=20,fg='brown',bg='lightblue',command=division)


b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)




b_clear.grid(row=4,column=1,columnspan=2)
b_add.grid(row=5,column=0)
b_equal.grid(row=5,column=1,columnspan=2)

b_subtract.grid(row=6,column=0)
b_multiply.grid(row=6,column=1)
b_division.grid(row=6,column=2)


root.mainloop()
