from tkinter import *
import random


def graph():
    #here is for bar chart............
 
    
    def prop(n): 
        return 360.0 * n / 1000
    # Label(root, text='Pie Chart').pack()
    c = Canvas(width=154, height=154)
    c.pack()
    c.create_arc((2,2,152,152), fill="#FAF402", outline="#FAF402", start=prop(0), extent = prop(600))
    c.create_arc((2,2,152,152), fill="#00AC36", outline="#00AC36", start=prop(200), extent = prop(400))
   
    

question = [
    "In Python 3, the maximum value for an integer is 263 - 1:",
    "What is a correct syntax to output 'Hello World' in Python?",
    "Which is the correct operator for power(xy)?",
    "Which one of these is floor division?",
    "What is the answer to this expression, 22 % 3 is?",
    "What is the maximum possible length of an identifier?",
    "Who developed the Python language?",
    "In which language is Python written?",
    "Which one of the following is the correct extension of the Python file?",
    "What do we use to define a block of code in Python language?"
    ]

answers = [
    ["True","False","None","Both"],
    [" p('Hello World')"," echo('Hello World');"," echo 'Hello World'"," print('Hello World')"],
    ["X^y","X**y","X^^y","None of the mentioned"],
    ["/","//","%","None of the mentioned"],
    ["7","1","0","5"],
    ["16","32","64","None of these above"],
    ["Zim Den","Guido van Rossum","Niene Stom","Wick van Rossum"],
    ["English","PHP","C","All of the above"],
    [".py",".python",".p","None of these"],
    ["Key","Brackets","Indentation","None of these"],




]
correctanswers=[1,2,1,1,1,3,1,2,0,2]
user_answers=[]
index = []

def back():
    root.destroy();
    import WelcomeScreen

def showresult(score):
    questionlbl.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(root,bg="white",border=0,width="400",height="400")
    labelimage.pack()
    labelresulttext2 = Label(root,font=("Times",15),fg="black",relief=GROOVE,bg="#75afbe")
    labelresulttext2.pack()
    labelresulttext = Label(root,font=("Times",15,"bold"),relief=GROOVE,bg="#75afbe",fg="black")
    labelresulttext.place(x=500,y=400)
   
    if score >= 20:
        img = PhotoImage(file="Image\\great2.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext2.configure(text="Excellent , Your Score is => ")
        labelresulttext.configure(text=score)
        btn_back = Button(root,text="Back",bg="#75afbe",fg="white",font=("times new roman",20),command=back).place(x=480,y=440,width=100,height=40)
    
    elif score>=10 and score <  20:
        img = PhotoImage(file="Image\\ok.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext2.configure(text="Good but this can be improve , Your Score is => ")
        labelresulttext.configure(text=score)
        btn_back = Button(root,text="Back",bg="#75afbe",fg="white",font=("times new roman",20),command=back).place(x=480,y=440,width=100,height=40)
        

    else:
        img = PhotoImage(file="Image\\bad.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext2.configure(text="Better Luck Next Time , Your Score is => ")
        labelresulttext.configure(text=score)
        btn_back = Button(root,text="Back",bg="#75afbe",fg="white",font=("times new roman",20),command=back).place(x=480,y=440,width=100,height=40)
        



def calculatresult():
    global index,user_answers,correctanswers
    x = 0
    score = 0
    for i in index:
        if user_answers[x] == correctanswers[i]:
           score =  score + 5
        x = x + 1
    showresult(score)




def generator():
    global index
    while(len(index)<5):
        x = random.randint(0,9)
        if x in index:
            continue
        else:
            index.append(x)

ques =  1 
def selectradio():
    global radio,user_answers,ques
    global questionlbl,r1,r2,r3,r4
    x=radio.get()
    user_answers.append(x)
    radio.set(-1)
    if ques < 5:
        questionlbl.config(text=question[index[ques]])
        r1["text"]=answers[index[ques]][0]
        r2["text"]=answers[index[ques]][1]
        r3["text"]=answers[index[ques]][2]
        r4["text"]=answers[index[ques]][3]
        ques += 1
    else:
        calculatresult()

def quizstart():
    global questionlbl,r1,r2,r3,r4
    questionlbl = Label(root,text=question[index[0]],font=("Consolas sans MS", 16),width=500,justify="center",wraplength=500,bg="#4888aa")
    questionlbl.pack(pady=(70,40))
    global radio
    radio = IntVar()
    radio.set(-1)
    r1=Radiobutton(root,text=answers[index[0]][0],font=("Times 12"),value=0,variable=radio,command=selectradio,bg="white")
    r1.pack(pady=(5))

    r2=Radiobutton(root,text=answers[index[0]][1],font=("Times 12"),value=1,variable=radio,command=selectradio,bg="white")
    r2.pack(pady=(5))

    r3=Radiobutton(root,text=answers[index[0]][2],font=("Times 12"),value=2,variable=radio,command=selectradio,bg="white")
    r3.pack(pady=(5))

    r4=Radiobutton(root,text=answers[index[0]][3],font=("Times 12"),value=3,variable=radio,command=selectradio,bg="white")
    r4.pack(pady=(5))

def startbutton():
    lbl_img.destroy()
    lbl_img2.destroy()
    btn_img_Button.destroy()
    generator()
    quizstart()


root=Tk()
root.title("Quiz")
root.geometry("600x490")
root.config(bg="white")
root.iconbitmap("Image/icon.ico")
root.resizable(False, False)




img = PhotoImage(file="Image\\transparentGradHat.png")
lbl_img=Label(root,image=img,bg="#82c4d0")
lbl_img.pack(pady=(40,10))

img2 = PhotoImage(file="Image\\quiz.png")
lbl_img2=Label(root,image=img2,bg="#82c4d0")
lbl_img2.pack(pady=(0,30))

btn_img = PhotoImage(file="Image\\Frame.png")
btn_img_Button = Button(root,image=btn_img,relief=FLAT,border=0,command=startbutton)
btn_img_Button.pack()

root.eval('tk::PlaceWindow . center')
root.mainloop()
 