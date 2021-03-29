from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.iconbitmap("Image/icon.ico")
tk.title("Tic Tac Toe")

tk.resizable(False,False)

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()


bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Computer Win"
        pa = p1.get() + " You Win!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
def back():
    tk.destroy();
    import WelcomeScreen

buttons = StringVar()

title=Label(tk, text="Tic Tac Toe", font='Garamond 30 bold', bg='#5289a6', fg='white', height=2, width=17,borderwidth=3, relief="solid",wraplength=300, justify="center")
title.grid(row=0, column=1, columnspan=3)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='#44598d', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=1)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='#446c96', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=2)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='#44598d', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=3)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='#446c96', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=1)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='#44598d', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=2)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='#446c96', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=3)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='#44598d', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=1)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='#446c96', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=2)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='#44598d', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=3)

backbtn = Button(tk, text='Back', font='Garamond 20 bold', bg='#5289a6', fg='white', height=1, width=25, command=back,borderwidth=3, relief="solid")
backbtn.grid(row=6, column=1, columnspan=3)
tk.eval('tk::PlaceWindow . center')
tk.mainloop()

