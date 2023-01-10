from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()




class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")
        
     #   self.bg=ImageTk.PhotoImage(file=r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\bg1.jpg")
      #  lbl_bg=Label(self.root,image=self.bg)
      #$  lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

       
        img3=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\bg2.jpg")
        img3=img3.resize((1280,650),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=0,width=1280,height=650)


        
        frame=Frame(self.root,bg="black")
        frame.place(x=460,y=30,width=350,height=420)
        
        img1=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\get started.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=580,y=35,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)


        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #====== Icon Images ====
        img2=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\icon.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=180,width=25,height=25)

        img3=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\icon2.jpg")
        img3=img3.resize((25,24),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=252,width=25,height=24)

     
        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=8,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

        
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Ankita" and self.txtpass.get()=="mahakal":
            messagebox.showinfo("Success","Welcome to my desktop Application")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mahakal",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

       # ==== reset password ============


    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root)
        elif self.txt_security.get()=="":
             messagebox.showerror("Error","Please enter the answer",parent=self.root)
        elif self.txt_newpass.get()=="": 
            messagebox.showerror("Error","Please enter the new password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mahakal",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password")
                self.root2.destroy()






# =========== forget password window=========
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="mahakal",database="mydata")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             
             if row==None:
                 messagebox.showerror("My error","Please enter the valid username")
             else:
                 conn.close()
                 self.root2=Toplevel()
                 self.root2.title("Forget password")
                 self.root2.geometry("340x450+580+140")

                 l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                 l.place(x=0,y=10,relwidth=1)

                 security_Q=Label(self.root2,text="Select Security Quetions",font=("times new roman",12,"bold"),bg="white",fg="black")
                 security_Q.place(x=50,y=80)

                 self.combo_securiy_Q=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly")
                 self.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                 self.combo_securiy_Q.place(x=50,y=110,width=250)
                 self.combo_securiy_Q.current(0)


                 security_A=Label(self.root2,text="Security Answer",font=("times new roman",12,"bold"),bg="white",fg="black")
                 security_A.place(x=50,y=150)
                    
                 self.txt_security=ttk.Entry(self.root2,font=("times new roman",12))
                 self.txt_security.place(x=50,y=180,width=250)


                 new_password=Label(self.root2,text="New Password",font=("times new roman",12,"bold"),bg="white",fg="black")
                 new_password.place(x=50,y=220)
                    
                 self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",12))
                 self.txt_newpass.place(x=50,y=250,width=250)

                 btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",18,"bold"),fg="white",bg="green")
                 btn.place(x=120,y=300,width=100)














class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        #===== varibles =====#==
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #============ bg image ====
      #  self.bg=ImageTk.PhotoImage(file=r"C:\Users\ankit\OneDrive\Documents\login_form\bg1.jpg")
      #  bg_lbl=Label(self.root,image=self.bg)
      #  bg_lbl.place(x=0,y=0,relwidth=1, relheight=1, anchor='nw')

        img3=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\bg1.jpg")
        img3=img3.resize((1280,650),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=0,width=1280,height=650)

        
        
        #============ left image === ‒‒‒‒‒‒‒‒‒‒‒‒‒‒
   #     self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ankit\OneDrive\Documents\login_form\1.jpg")
    #    left_lbl=Label(self.root,image=self.bg1)
     #   left_lbl.place(x=50,y=130,width=350,height=450)

        img2=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\1.jpg")
        img2=img2.resize((350,450),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_image=Label(self.root,image=self.photoimg2)
        bg_image.place(x=150,y=110,width=350,height=450)

        
        #============== main Frame ========
        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=110,width=630,height=450)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #‒‒‒‒‒‒‒‒‒‒ label and entry ===
        
        #-----row1
        fname=Label(frame,text="First Name",font=("times new roman",12,"bold"),bg="white")
        fname.place(x=35,y=70)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new rom",12,"bold"))
        self.fname_entry.place(x=35,y=100,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",12,"bold"),bg="white",fg="black")
        l_name.place(x=335,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12))
        self.txt_lname.place(x=335,y=100,width=2504)
        
        #--row2
        contact=Label(frame,text="Contact No",font=("times new roman",12,"bold"),bg="white",fg="black")
        contact.place(x=35,y=140)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        self.txt_contact.place(x=35,y=170,width=250)

        email=Label(frame,text="Email",font=("times new roman",12,"bold"),bg="white",fg="black")
        email.place(x=335,y=140)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12))
        self.txt_email.place(x=335,y=170,width=250)
                  
        #--row3
        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_Q.place(x=35,y=210)

        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_securiy_Q.place(x=35,y=240,width=250)
        self.combo_securiy_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_A.place(x=335,y=210)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",12))
        self.txt_security.place(x=335,y=240,width=250)
        
        # --row4

        pswd=Label(frame,text="Password",font=("times new roman",12,"bold"),bg="white",fg="black")
        pswd.place(x=35,y=280)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",12))
        self.txt_pswd.place(x=35,y=310,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",12,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=335,y=280)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",12))
        self.txt_confirm_pswd.place(x=335,y=310,width=250)

        #======= ==== checkbutton ====
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="IAgree The Terms&Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=35,y=350)

        #================= buttons ======= ===========
        img=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\register.jpg")
        img=img.resize((230,40),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=35,y=390,width=230)


        img1=Image.open(r"C:\Users\ankit\OneDrive\Documents\login_form\New folder\login.jpg")
        img1=img1.resize((200,55),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=350,y=360,width=200)
        
    #==== Function declaration ===
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="mahakal",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.var_fname.get(),#=StringVar()
                                                                                           self.var_lname.get(),#=StringVar()
                                                                                           self.var_contact.get(),#=StringVar()
                                                                                           self.var_email.get(),#=StringVar()
                                                                                           self.var_securityQ.get(),#=StringVar()
                                                                                           self.var_SecurityA.get(),#=StringVar()
                                                                                           self.var_pass.get()#=StringVar()
                      
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")                                                                                      
                                   
    def return_login(self):
        self.root.destroy()
                                      
                                        

     
     
if __name__ =="__main__":
    main()
   
        
        