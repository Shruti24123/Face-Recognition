from cgitb import text
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import title
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help_desk
from time import strftime
from datetime import datetime
from chatbot import ChatBot


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognition System")

        img=Image.open(r"Images\download.jpg")
        img=img.resize((440,110),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=440,height=110)

        img1=Image.open(r"Images\download (2).jpg")
        img1=img1.resize((440,110),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=440,y=0,width=440,height=110)

        img2=Image.open(r"Images\download (3).jpg")
        img2=img2.resize((440,110),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=880,y=0,width=440,height=110)

        #bg image

        img3=Image.open(r"Images\bg.jpg")
        img3=img3.resize((1300,550),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=110,width=1272,height=550)

        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1272,height=40)



        # ====time ======

        def time():
           string=strftime('%H:%M:%S %p')
           lbl.config(text=string)
           lbl.after(1000, time)

        lbl=Label(title_lbl, font=('times new roman',12,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=90,height=50)
        time()



        #student button

        img4=Image.open(r"Images\b1.jpg")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=160,y=80,width=170,height=170)

        
        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=160,y=220,width=170,height=30)


             #face detector image

        img5=Image.open(r"Images\face detector.jpg")
        img5=img5.resize((170,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_image,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=380,y=80,width=170,height=170)

        
        b1_1=Button(bg_image,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=380,y=220,width=170,height=30)


        img6=Image.open(r"Images\attendance.jpg")
        img6=img6.resize((170,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=600,y=80,width=170,height=170)

        
        b1_1=Button(bg_image,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=600,y=220,width=170,height=30)


        """  img7=Image.open(r"Images\help desk.jpg")
          img7=img7.resize((170,170),Image.ANTIALIAS)
          self.photoimg7=ImageTk.PhotoImage(img7)

          b1=Button(bg_image,image=self.photoimg7,cursor="hand2",command=self.help_data)
          b1.place(x=820,y=80,width=170,height=170)

          
          b1_1=Button(bg_image,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
          b1_1.place(x=820,y=220,width=170,height=30) """

        img7=Image.open(r"New folder\chatbot.png")
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,cursor="hand2",command=self.chatbot)
        b1.place(x=820,y=80,width=170,height=170)

          
        b1_1=Button(bg_image,text="ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=820,y=220,width=170,height=30)



        img8=Image.open(r"Images\train data.jpg")
        img8=img8.resize((170,170),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=160,y=290,width=170,height=170)

        
        b1_1=Button(bg_image,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=160,y=440,width=170,height=30)



        img9=Image.open(r"Images\photos.jpg")
        img9=img9.resize((170,170),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=380,y=290,width=170,height=170)

        
        b1_1=Button(bg_image,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=380,y=440,width=170,height=30)


        img_a=Image.open(r"Images\developer.jpg")
        img_a=img_a.resize((170,170),Image.ANTIALIAS)
        self.photoimg_a=ImageTk.PhotoImage(img_a)

        b1=Button(bg_image,image=self.photoimg_a,cursor="hand2",command=self.developer_data)
        b1.place(x=600,y=290,width=170,height=170)

        
        b1_1=Button(bg_image,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=600,y=440,width=170,height=30)



        img11=Image.open(r"Images\exit.jpg")
        img11=img11.resize((170,170),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
            
        b1=Button(bg_image,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=820,y=290,width=170,height=170)

        
        b1_1=Button(bg_image,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=820,y=440,width=170,height=30)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face recognition","Are you sure to exit this project")
       if self.iExit>0:
        self.root.destroy()
       else:
         return 





        # =======functions btns====


    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)


    
    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)  


   
    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window) 


    def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)   


    def developer_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Developer(self.new_window)  


    """def help_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Help_desk(self.new_window) """

    def chatbot(self):
      self.new_window=Toplevel(self.root)
      self.app=ChatBot(self.new_window)       
  


    


if __name__ == "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()