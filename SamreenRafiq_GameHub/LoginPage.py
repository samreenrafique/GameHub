from tkinter import*
from tkinter import ttk,messagebox
import pymysql


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.iconbitmap("Image/icon.ico")
        self.root.geometry("800x600+100+50")
        self.root.resizable(False,False)
        # BG Image
        self.bg=PhotoImage(file="Image/img.png")
        self.bg_img=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1) 

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=450)

        
        title=Label(Frame_login,text="Login Yourself",font=("Garamond",35,"bold"),fg="#473062",bg="white").place(x=70,y=30)
        lbl_user=Label(Frame_login,text="Enter Email",font=("Garamond",18,"bold"),fg="#473062",bg="white").place(x=70,y=120)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=70,y=150,width=250,height=35)

        lbl_pswd=Label(Frame_login,text="Enter Password",font=("Garamond",18,"bold"),fg="#473062",bg="white").place(x=70,y=190)
        self.txt_pswd=Entry(Frame_login,font=("times new roman",15),bg="lightgray", show="*")
        self.txt_pswd.place(x=70,y=220,width=250,height=35)

        btn_login = Button(Frame_login,text="Login",bg="#94768a",fg="#473062",font=("times new roman",20),command=self.Login).place(x=90,y=280,width=180,height=40)

        side=Frame(self.root,bg="#94768a")
        side.place(x=560,y=150,height=170,width=50)
        side2=Frame(self.root,bg="#473062")
        side2.place(x=560,y=320,height=170,width=50)
    def clear(self):
        self.txt_user.delete(0,END)
        self.txt_pswd.delete(0,END)

    def Login(self):
        if self.txt_user.get() == "" or self.txt_pswd.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="gamehub")
                cur=con.cursor()
                cur.execute("select * from Register where Email=%s and Password=%s",(self.txt_user.get(),self.txt_pswd.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showinfo("Success","Login Successfull",parent=self.root)
                    self.root.destroy()
                    import WelcomeScreen
                else:                       
                    con.close()
                    messagebox.showerror("Error","Invalid Credentials",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showwarning("Error",f"Error due to {str(es)}",parent=self.root)

root=Tk()
obj=Login(root)
root.eval('tk::PlaceWindow . center')
root.mainloop()