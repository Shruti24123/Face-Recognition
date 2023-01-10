#from cgitb import text
from tkinter import*
from tkinter import ttk
#from tokenize import String
#from turtle import title
from PIL import Image, ImageTk
from tkinter import messagebox
#from cv2 import VideoCapture
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognition System")



        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1272, height=40)



        img_top = Image.open(
            r"Images\f1.jpg")
        img_top = img_top.resize((630, 600), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=630, height=600)




        img_bottom = Image.open(
            r"Images\f2.jpg")
        img_bottom = img_bottom.resize((650, 600), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=630, y=45, width=650, height=600)


         # button


        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=230,y=530,width=180,height=30)

       # ===== attendence =====

    def mark_attendance(self,i,r,n,d):
        with open("attendence report/present.csv","r+",newline="\n") as f:
            mydataList=f.readlines()
            name_list=[]
            for line in mydataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


        # ====== face recognition ========


    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
               gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
               features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

               coord=[]

               for(x,y,w,h) in features:
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                   id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                   confidence=int((100*(1-predict/300)))

                   conn = mysql.connector.connect(host="localhost",username="root",password="mahakal",database="face_recognizer")
                   my_cursor=conn.cursor()

                   my_cursor.execute("Select name from student where Student_id="+str(id))
                   n=my_cursor.fetchone()
                   n="+".join(n)
                   #n=str(n)

                   my_cursor.execute("Select roll from student where Student_id="+str(id))
                   r=my_cursor.fetchone()
                   r="+".join(r)
                   #r=str(r)

                   my_cursor.execute("Select Dep from student where Student_id="+str(id))
                   d=my_cursor.fetchone()
                   d="+".join(d)
                   #d=str(d)

                   my_cursor.execute("Select student_id from student where Student_id="+str(id))
                   i=my_cursor.fetchone()
                   i="+".join(i)
                  # i=str(i)


                   if confidence>77:
                       cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                       cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                       cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                       cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                       self.mark_attendance(i ,r, n, d)
                   else:
                       cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                       cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),2)  

                   coord=[x,y,w,y]

               return coord 


        def recognize(img,clf,faceCascade):
                 coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                 return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        Video_cap=cv2.VideoCapture(0 , cv2.CAP_DSHOW)

        while True:
                ret,img=Video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Fcae Recognition",img)

                if cv2.waitKey(1)==13:
                    break

        Video_cap.release()
        cv2.destroyAllWindows()














 






        
if __name__ == "__main__":
     root = Tk()
     obj=Face_Recognition(root)
     root.mainloop()