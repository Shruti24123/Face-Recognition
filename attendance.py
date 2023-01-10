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
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognition System")

         # ===== variables =====

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        img = Image.open(
            r"Images\a1.jpg")
        img = img.resize((640, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=640, height=200)

        img1 = Image.open(
            r"Images\a2.jpg")
        img1 = img1.resize((640, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=640, y=0, width=640, height=200)


        img3=Image.open(r"Images\bg.jpg")
        img3=img3.resize((1280,550),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=120,width=1280,height=550)


        title_lbl = Label(bg_image, text="ATTENDANCE MANAGEMENT SYSTEM", font=(
            "times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1272, height=40)


        
        main_frame = Frame(bg_image, bd=2, bg="white")
        main_frame.place(x=15, y=50, width=1240, height=500)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=15, y=10, width=590, height=460)


        img_left = Image.open(
            r"Images\left_frame.jpg")
        img_left = img_left.resize((570, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=570, height=150)


        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=155, width=570, height=280)

        # labels and entry
        # attendattendance

        attendanceId_label = Label(left_inside_frame, text="Attendance Id:", font=(
            "times new roman", 10, "bold"))
        attendanceId_label.grid(row=0, column=0, padx=15, pady=6, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_atten_id, font=("times new roman", 10, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=15, pady=6, sticky=W)

        #name

        
        attendanceId_label = Label(left_inside_frame, text="Name:", font=(
            "times new roman", 10, "bold"))
        attendanceId_label.grid(row=0, column=2, padx=15, pady=6, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_atten_name, font=("times new roman", 10, "bold"))
        attendanceId_entry.grid(row=0, column=3, padx=15, pady=3, sticky=W)

        #roll

        
        attendanceId_label = Label(left_inside_frame, text="Roll No.:", font=(
            "times new roman", 10, "bold"))
        attendanceId_label.grid(row=1, column=0, padx=15, pady=6, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_atten_roll, font=("times new roman", 10, "bold"))
        attendanceId_entry.grid(row=1, column=1, padx=15, pady=6, sticky=W)

        #dep

        
        attendanceId_label = Label(left_inside_frame, text="Department:", font=(
            "times new roman", 10, "bold"))
        attendanceId_label.grid(row=1, column=2, padx=15, pady=6, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_atten_dep, font=("times new roman", 10, "bold"))
        attendanceId_entry.grid(row=1, column=3, padx=15, pady=6, sticky=W)

        #time

        
        attendanceId_label = Label(left_inside_frame, text="Time:", font=(
            "times new roman", 10, "bold"))
        attendanceId_label.grid(row=2, column=0, padx=15, pady=6, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_atten_time, font=("times new roman", 10, "bold"))
        attendanceId_entry.grid(row=2, column=1, padx=15, pady=6, sticky=W)

        #date

        
        attendanceId_label = Label(left_inside_frame, text="Date:", font=(
            "times new roman", 10, "bold"))
        attendanceId_label.grid(row=2, column=2, padx=15, pady=6, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=17,textvariable=self.var_atten_date, font=("times new roman", 10, "bold"))
        attendanceId_entry.grid(row=2, column=3, padx=15, pady=6, sticky=W)

        #attendence status

        
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=(
            "comicsansns 9 bold"))#state="readonly")
        attendanceLabel.grid(row=3, column=0)# padx=15, pady=3, sticky=W)

        self.atten_status = ttk.Combobox(
            left_inside_frame, width=13,textvariable=self.var_atten_attendance, font=("times new roman", 11, "bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3, column=1, padx=15, pady=3, sticky=W)
        self.atten_status.current(0)


        # btn frame

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=562, height=40)

        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv,width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update",width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)




















        
        # right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=630, y=10, width=590, height=460)


        right_inside_frame = Frame(right_frame, bd=2,relief=RIDGE, bg="white")
        right_inside_frame.place(x=7, y=2, width=570, height=380)

        # scroll bar 

        scroll_x=ttk.Scrollbar(right_inside_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_inside_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(right_inside_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")


        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)#tendance ID")
        self.AttendanceReportTable.column("roll",width=100)#Roll")
        self.AttendanceReportTable.column("name",width=100)#Name")
        self.AttendanceReportTable.column("department",width=100)#text="Department")
        self.AttendanceReportTable.column("time",width=100)#Time")
        self.AttendanceReportTable.column("date",width=100)#Date")
        self.AttendanceReportTable.column("attendance",width=100)#text="Attendance")

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)


    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)    


              # export csv


    def exportCsv(self):    
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return FALSE
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)  
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                



    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      row=content['values']
      self.var_atten_id.set(row[0])
      self.var_atten_roll.set(row[1])
      self.var_atten_name.set(row[2])
      self.var_atten_dep.set(row[3])
      self.var_atten_time.set(row[4])
      self.var_atten_date.set(row[5])
      self.var_atten_attendance.set(row[6])


    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")



















if __name__ == "__main__":                
             root = Tk()
             obj=Attendance(root)
             root.mainloop()
