from tkinter import*
from PIL import Image, ImageTk


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome Screen")
        self.root.iconbitmap("Image/icon.ico")
        self.root.geometry("1199x400+100+50")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="Image/img.png")
        self.bg_img = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        Frame_zero = Frame(self.root, bg="white")
        Frame_zero.place(x=200, y=50, height=80, width=800)

        title = Label(Frame_zero, text="GAME HUB", font=(
            "Impact", 35, "bold"), fg="#473062", bg="white").place(x=300, y=5)

        Frame_One = Frame(self.root, bg="white")
        Frame_One.place(x=150, y=200, height=150, width=200)
        title_one = Label(Frame_One, text="Tic Tac Toe", font=(
            "Guddy old style", 20, "bold"), fg="#473062", bg="white").place(x=20, y=20)
        tic_tac = Button(Frame_One, text="Start", bg="#473062", fg="white", font=(
            "times new roman", 20), command=self.tictac).place(x=20, y=70, width=160, height=40)

        Frame_two = Frame(self.root, bg="white")
        Frame_two.place(x=400, y=200, height=150, width=200)
        title_two = Label(Frame_two, text="Hang Man", font=(
            "Guddy old style", 20, "bold"), fg="#473062", bg="white").place(x=30, y=20)
        hang_man = Button(Frame_two, text="Start", bg="#473062", fg="white", font=(
            "times new roman", 20),command=self.hangman).place(x=20, y=70, width=160, height=40)

        Frame_three = Frame(self.root, bg="white")
        Frame_three.place(x=650, y=200, height=150, width=200)
        title_three = Label(Frame_three, text="Guessing", font=(
            "Guddy old style", 20, "bold"), fg="#473062", bg="white").place(x=30, y=20)
        Guessing = Button(Frame_three, text="Start", bg="#473062", fg="white", font=(
            "times new roman", 20),command=self.guess).place(x=20, y=70, width=160, height=40)

        Frame_four = Frame(self.root, bg="white")
        Frame_four.place(x=900, y=200, height=150, width=200)
        title_four = Label(Frame_four, text="Quiz", font=(
            "Guddy old style", 20, "bold"), fg="#473062", bg="white").place(x=60, y=20)
        Color = Button(Frame_four, text="Start", bg="#473062", fg="white", font=(
            "times new roman", 20),command=self.quiz).place(x=20, y=70, width=160, height=40)

    def tictac(self):
        self.root.destroy()
        import TicTacToe

    def hangman(self):
        self.root.destroy()
        import Hangman

    def quiz(self):
        self.root.destroy()
        import Quiz

    def guess(self):
        self.root.destroy()
        import Guessing

root=Tk()
obj=Login(root)
root.mainloop()
