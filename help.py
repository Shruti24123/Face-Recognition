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
class Help_desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognition System")


        title_lbl = Label(self.root, text="HELP DESK", font=(
            "times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1272, height=40)



        img_top = Image.open(
            r"Images\h.jpg")
        img_top = img_top.resize((1275, 600), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1275, height=600)


        dev_label = Label(f_lbl, text="Email:ankita28dubey@gmail.com", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label.place(x=430,y=320)





if __name__ == "__main__":
                           
                           
        root = Tk()
        obj=Help_desk(root)
        root.mainloop()            
