import tkinter as tk
from tkinter import *
import random
import os
from PIL import Image, ImageTk

win = tk.Tk()
win.configure(bg="#75afbe")
win.geometry("650x550")
win.title("Number Guessing Game")
win.iconbitmap("Image/icon.ico")
win.resizable(False, False)
result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,20)
result.set("Guess a number between 1 to 20 ")
chances.set(3)
chances1.set(chances.get())

def fun():
  chances1.set(chances.get())
  if chances.get()>0:

    if choice.get() > 20 or choice.get()<0:
      result.set("Out of Range Guess")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    elif no==choice.get():
      result.set("Congratulation YOU WON!!!")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no > choice.get():
      result.set("Your guess was too low: Guess a number higher ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    elif no < choice.get():
      result.set(
          "Your guess was too High: Guess a number Lower ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  else:
     result.set(
         "Game Over You Lost")

def restart():
  no=random.randint(1,20)
  result.set("Guess a number between 1 to 20 ")
  chances.set(5)
  chances1.set(chances.get())
def back():
    win.destroy()
    import WelcomeScreen
ent1 = Entry(win, textvariable=choice, width=3,
             font=('Ubuntu', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(win, textvariable=result, width=50,
             font=('Courier', 15), relief=GROOVE,bg="#75afbe")
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(win, text=chances1, width=2,
             font=('Ubuntu', 24), relief=RIDGE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(win, text='Guess a number between 1 to 20 ',
            font=("Comic sans MS", 25), relief=GROOVE,bg="#75afbe")
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Chances Left :',
             font=("Comic sans MS", 25,"bold"), relief=GROOVE,bg="#75afbe")
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=(
    'Times', 25,"bold"), command=fun, relief=GROOVE,bg="#4888aa",fg="white")
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

back = tk.Button(win, text='Back', width=26, command=back,font=("Times",16,"bold"),
                 bg="#4888aa",fg="white", activebackground="#54768a", relief=GROOVE)
back.place(relx=0.25, rely=1, anchor=S)

reset = tk.Button(win, text='Restart', width=26, command=restart,font=("Times",16,"bold"),
                 bg="#4888aa",fg="white", activebackground="#54768a", relief=GROOVE)
reset.place(relx=0.75, rely=1, anchor=S)

win.eval('tk::PlaceWindow . center')
win.mainloop()