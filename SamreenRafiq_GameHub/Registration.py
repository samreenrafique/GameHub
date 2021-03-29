from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.iconbitmap("Image/icon.ico")  
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#b6c4c4")

        #Background Image

        self.bg=ImageTk.PhotoImage(file="Image/img.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Left Image
        self.left=ImageTk.PhotoImage(file="Image/Bg.png")
        left=Label(self.root,image=self.left).place(x=220,y=100,width=400,height=500)

        #register side
        frame1=Frame(self.root,bg="#b6c4c4")
        frame1.place(x=620,y=100,width=500,height=500)

        title=Label(frame1,text="Register Yourself",font=("times new roman",25,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=30)

   
        Username=Label(frame1,text="Enter Username",font=("times new roman",15,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=100)
        self.txt_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_name.place(x=50,y=130,width=250)

        Email=Label(frame1,text="Enter Email",font=("times new roman",15,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=200,width=250)

        Password=Label(frame1,text="Enter Password",font=("times new roman",15,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=250)
        self.txt_pswd=Entry(frame1,font=("times new roman",15),bg="lightgray", show="*")
        self.txt_pswd.place(x=50,y=280,width=250)

        C_Password=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=320)
        self.txt_cpswd=Entry(frame1,font=("times new roman",15),bg="lightgray", show="*")
        self.txt_cpswd.place(x=50,y=350,width=250)

        self.var_chk=IntVar()
        chk= Checkbutton(frame1,text="I Agree with terms and condition",font=("times new roman",15,"bold"),fg="#3d7c7c",variable=self.var_chk,onvalue=1,offvalue=0,bg="#b6c4c4").place(x=50,y=390)

        b1_register = Button(frame1, text='Register',width=20,bg='#3e7e7d',bd=0,cursor="hand2",command=self.register_data,font=("times new roman",15,"bold"),fg='#b6c4c4').place(x=50,y=440)
        
        b2 = Button(self.root, text='Already have Account',width=20,bg='#3e7e7d',bd=0,cursor="hand2",font=("times new roman",15,"bold"),fg='#b6c4c4',command=self.LoginWindow).place(x=300,y=120)

        # question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=320)
        # cmb_que=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify="center")
        # ques['values']=("Select Questions","First Pet Name","Favourite Programming Language","FYP Project")
        # ques.place(x=50,y=350,width=250)
        # ques.current(0)

        # answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="#b6c4c4",fg="#3e7e7d").place(x=50,y=390)
        # txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=420,width=250)
    
    def clear(self):
        self.txt_name.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pswd.delete(0,END)
        self.txt_cpswd.delete(0,END)

    def LoginWindow(self):
        self.root.destroy()
        import LoginPage

    def register_data(self):
        if self.txt_name.get()=="" or self.txt_email.get()=="" or self.txt_pswd.get()=="" or self.txt_cpswd.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_pswd.get()!=self.txt_cpswd.get():
            messagebox.showerror("Error","Password and Confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="gamehub")
                cur=con.cursor()
                cur.execute("select * from Register where Email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User Already Exist, Try Another Email",parent=self.root)
                else:
                    cur.execute("INSERT INTO Register(Name, Email, Password) VALUES (%s,%s,%s)",
                    (
                        self.txt_name.get(),self.txt_email.get(),self.txt_pswd.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)            
                    self.clear()
                    self.root.destroy()
                    import LoginPage
            except Exception as es:
                messagebox.showwarning("Error",f"Error due to {str(es)}",parent=self.root)

            
root = Tk()
root.eval('tk::PlaceWindow . center')
obj=Register(root)
root.mainloop()  
