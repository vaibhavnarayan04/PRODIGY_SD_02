#TASK 2
from tkinter import *
import random
Root=Tk()
Root.title("Guessing Game")
Root.geometry("550x250")
Root.resizable(0,0)
rn=random.randint(1,100)
c=0
def guess():
    global c
    a=int(entGn.get())
    
    if a!=rn:
        c=c+1
        if a>rn:
            lblResult.config(text=f'Guess is too HIGH !!',fg='red')
        elif a<rn:
            lblResult.config(text=f'Guess is too LOW !!',fg='red')
    else:
        c=c+1
        lblResult.config(text=f'!! YOU WIN !!',fg='green')
        lbl=Label(Root,text=f'{c} attempts',font=('Informal Roman',25),fg='green',bg='yellow')
        lbl.grid(row=4,column=0,padx=5,pady=5)

lblGn=Label(Root,text='Guess the Number',font=('BankGothic Md BT',38), fg='blue')
lblGn.grid(row=0,column=0)
entGn=Entry(Root,font=('Informal Roman',25),bg='light green')
entGn.grid(row=1,column=0)
lblResult=Label(Root,text='',font=("Arial Bold",14))
lblResult.grid(row=3,column=0,padx=5,pady=5)
but1=Button(Root,text='GUESS',font=("Arial Bold",14),bg='red',command=guess)
but1.grid(row=2,column=0,padx=5,pady=5)

Root.mainloop()
