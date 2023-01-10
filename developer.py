from cgitb import text
from tkinter import*
from tkinter import ttk
from tokenize import String
from turtle import title
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognition System")


        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1272, height=40)



        img_top = Image.open(
            r"Images\d2.jpg")
        img_top = img_top.resize((1275, 600), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1275, height=600)


        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=800, y=0, width=400, height=500)


        
        img_top1 = Image.open(
            r"Images\d3.jpg")
        img_top1 = img_top1.resize((250, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=215, y=0, width=250, height=200)


          # developer info

        dev_label = Label(main_frame, text="Hello my name is Ankita", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I am full stack developer", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label.place(x=0,y=40)


        img_top2 = Image.open(
            r"Images\d.jpg")
        img_top2 = img_top2.resize((398, 325), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame, image=self.photoimg_top2)
        f_lbl.place(x=0, y=180
        , width=395, height=325)












if __name__ == "__main__":
                           
                           
        root = Tk()
        obj=Developer(root)
        root.mainloop()        
