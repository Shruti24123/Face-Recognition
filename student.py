from cgitb import text
from tkinter import*
from tkinter import ttk
from tokenize import String
from turtle import title
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("face Recognition System")

        # ===== variables =====

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(
            r"Images\2.jpg")
        img = img.resize((440, 110), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=440, height=110)

        img1 = Image.open(
            r"Images\1.jpg")
        img1 = img1.resize((440, 110), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=440, y=0, width=440, height=110)

        img2 = Image.open(
            r"Images\3.jpg")
        img2 = img2.resize((440, 110), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=880, y=0, width=440, height=110)

        # bg image

        img3 = Image.open(
            r"Images\bg.jpg")
        img3 = img3.resize((1300, 550), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=110, width=1272, height=550)

        title_lbl = Label(bg_image, text="Student Management System", font=(
            "times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1272, height=40)

        main_frame = Frame(bg_image, bd=2, bg="white")
        main_frame.place(x=15, y=50, width=1240, height=500)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=15, y=10, width=590, height=460)

        img_left = Image.open(
            r"Images\left_frame.jpg")
        img_left = img_left.resize((570, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=570, height=100)

        # current course information

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=10, y=103, width=570, height=95)

          # department

        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 15, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=15, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        dep_combo["values"] = ("Select Department",
                               "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=1, pady=4, sticky=W)

          # course

        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 15, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=15, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=1, pady=4, sticky=W)

           # year

        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 15, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=15, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        year_combo["values"] = (
            "Select Year", "2020--2021", "2021-2022", "2022-2023", "2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=1, pady=4, sticky=W)

           # semester

        sem_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 15, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=15, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=1, pady=4, sticky=W)

          # class student information

        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=10, y=200, width=570, height=235)

        # studentID

        studentId_label = Label(class_Student_frame, text="StudentId:", font=(
            "times new roman", 10, "bold"))
        studentId_label.grid(row=0, column=0, padx=15, pady=3, sticky=W)

        studentId_entry = ttk.Entry(
            class_Student_frame,textvariable=self.var_std_id, width=17, font=("times new roman", 10, "bold"))
        studentId_entry.grid(row=0, column=1, padx=15, pady=3, sticky=W)

       # student name

        name_label = Label(class_Student_frame, text="Student Name:", font=(
            "times new roman", 10, "bold"))
        name_label.grid(row=0, column=2, padx=15, pady=3, sticky=W)

        name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name, width=17, font=(
            "times new roman", 10, "bold"))
        name_entry.grid(row=0, column=3, padx=15, pady=3, sticky=W)

        # class division

        class_div_label = Label(class_Student_frame, text="class Div:", font=(
            "times new roman", 10, "bold"))
        class_div_label.grid(row=1, column=0, padx=15, pady=3, sticky=W)

      #  class_div_entry = ttk.Entry(class_Student_frame,
       #     textvariable=self.var_div, width=17, font=("times new roman", 10, "bold"))
       # class_div_entry.grid(row=1, column=1, padx=15, pady=3, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div, font=(
            "times new roman", 10, "bold"), width=15, state="readonly")
        div_combo["values"] = (
            "A", "B", "C","D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=15, pady=3, sticky=W)

        # roll no.

        Roll_No_label = Label(class_Student_frame, text="Roll No.:", font=(
            "times new roman", 10, "bold"))
        Roll_No_label.grid(row=1, column=2, padx=15, pady=3, sticky=W)

        Roll_No_entry = ttk.Entry(
            class_Student_frame,textvariable=self.var_roll, width=17, font=("times new roman", 10, "bold"))
        Roll_No_entry.grid(row=1, column=3, padx=15, pady=3, sticky=W)

        # gender

        Gender_label = Label(class_Student_frame, text="Gender:",
                             font=("times new roman", 10, "bold"))
        Gender_label.grid(row=2, column=0, padx=15, pady=3, sticky=W)

      #  Gender_entry = ttk.Entry(
       #     class_Student_frame,textvariable=self.var_gender, width=17, font=("times new roman", 10, "bold"))
       # Gender_entry.grid(row=2, column=1, padx=15, pady=3, sticky=W)

        Gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender, font=(
            "times new roman", 10, "bold"), width=15, state="readonly")
        Gender_combo["values"] = (
            "Female", "Male", "Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=1, padx=15, pady=3, sticky=W)

        # dob

        DOB_label = Label(class_Student_frame, text="DOB:",
                          font=("times new roman", 10, "bold"))
        DOB_label.grid(row=2, column=2, padx=15, pady=3, sticky=W)

        DOB_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=17,
                              font=("times new roman", 10, "bold"))
        DOB_entry.grid(row=2, column=3, padx=15, pady=3, sticky=W)

        # email

        Email_label = Label(class_Student_frame, text="Email:",
                            font=("times new roman", 10, "bold"))
        Email_label.grid(row=3, column=0, padx=15, pady=3, sticky=W)

        Email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=17, font=(
            "times new roman", 10, "bold"))
        Email_entry.grid(row=3, column=1, padx=15, pady=3, sticky=W)

        # phone no.

        Phone_No_label = Label(class_Student_frame, text="Phone No.:", font=(
            "times new roman", 10, "bold"))
        Phone_No_label.grid(row=3, column=2, padx=15, pady=3, sticky=W)

        Phone_No_entry = ttk.Entry(
            class_Student_frame,textvariable=self.var_phone, width=17, font=("times new roman", 10, "bold"))
        Phone_No_entry.grid(row=3, column=3, padx=15, pady=3, sticky=W)

         # address

        Address_label = Label(class_Student_frame, text="Address:", font=(
            "times new roman", 10, "bold"))
        Address_label.grid(row=4, column=0, padx=15, pady=3, sticky=W)

        Address_entry = ttk.Entry(
            class_Student_frame,textvariable=self.var_address, width=17, font=("times new roman", 10, "bold"))
        Address_entry.grid(row=4, column=1, padx=15, pady=3, sticky=W)

        # teacher name

        Teacher_name_label = Label(
            class_Student_frame, text="Teacher Name:", font=("times new roman", 10, "bold"))
        Teacher_name_label.grid(row=4, column=2, padx=15, pady=3, sticky=W)

        Teacher_name_entry = ttk.Entry(
            class_Student_frame,textvariable=self.var_teacher, width=17, font=("times new roman", 10, "bold"))
        Teacher_name_entry.grid(row=4, column=3, padx=15, pady=3, sticky=W)

        # radio button

        self.var_radio1=StringVar()
        Radio_button1_entry = ttk.Radiobutton(
            class_Student_frame,variable=self.var_radio1, text="Take photo Sample", value="yes")
        Radio_button1_entry.grid(row=6, column=0, padx=2)


        Radio_button2_entry = ttk.Radiobutton(
            class_Student_frame,variable=self.var_radio1, text="No photo Sample", value="No")
        Radio_button2_entry.grid(row=6, column=1, padx=2)

        # btn frame

        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=160, width=562, height=25)

        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=19, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=19, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,width=19, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=19, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn2_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn2_frame.place(x=2, y=185, width=562, height=25)

        Take_photo_Sample_btn = Button(btn2_frame, text="Take Photo Sample",command=self.generate_dataset, width=39, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        Take_photo_Sample_btn.grid(row=0, column=0)

        Update_Photo_Sample_btn = Button(btn2_frame, text="Update Photo Sample", width=39, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        Update_Photo_Sample_btn.grid(row=0, column=1)

        # right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=630, y=10, width=590, height=460)

        img_right = Image.open(
            r"Images\right_frame.jpg")
        img_right = img_right.resize((570, 100), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=570, height=100)

        # ======== search system ======

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=10, y=103, width=570, height=60)

        search_label = Label(search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=3, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), width=12, state="readonly")
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=1, pady=4, sticky=W)

        Address_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 12, "bold"))
        Address_entry.grid(row=0, column=2, padx=10, pady=3, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=2)

        show_btn = Button(search_frame, text="Show all", width=12, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        show_btn.grid(row=0, column=4, padx=2)

        # ====== table frame =======

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=165, width=570, height=200)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ===== function declaration ======

    def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost",username="root",password="mahakal",database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                       self.var_dep.get(),
                                                                                                       self.var_course.get(),
                                                                                                       self.var_year.get(),
                                                                                                       self.var_sem.get(),
                                                                                                       self.var_std_id.get(),
                                                                                                       self.var_std_name.get(),
                                                                                                       self.var_div.get(),
                                                                                                       self.var_roll.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_dob.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_teacher.get(),
                                                                                                       self.var_radio1.get()
                                                                                                       
                                                                                                       ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  



         # ====== fetch data  ========

    def fetch_data(self):
       conn = mysql.connector.connect(host="localhost",username="root",password="mahakal",database="face_recognizer")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from student")
       data=my_cursor.fetchall()

       if len(data)!=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
               self.student_table.insert("",END,values=i)
           conn.commit() 
       conn.close()      



        # ===== get cursor =====

    def get_cursor(self,event=""):
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]


         self.var_dep.set(data[0]),
         self.var_course.set(data[1]),  
         self.var_year.set(data[2]), 
         self.var_sem.set(data[3]), 
         self.var_std_id.set(data[4]), 
         self.var_std_name.set(data[5]), 
         self.var_div.set(data[6]), 
         self.var_roll.set(data[7]), 
         self.var_gender.set(data[8]), 
         self.var_dob.set(data[9]), 
         self.var_email.set(data[10]), 
         self.var_phone.set(data[11]), 
         self.var_address.set(data[12]), 
         self.var_teacher.set(data[13]), 
         self.var_radio1.set(data[14]), 

       # update 

    def update_data(self):  
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are required",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to update this student deatails",parent=self.root)
                    if Update>0:
                        conn = mysql.connector.connect(host="localhost",username="root",password="mahakal",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("Update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                                            
                                                                                                                                                                                                        ))                
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success","Student deatails successfully update completes",parent=self.root)  
                    conn.commit()
                    conn.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                                                                    

             # ==== delete function =====

    def delete_data(self):
             if self.var_std_id.get()=="":
                 messagebox.showerror("Error","StudentId must be required",parent=self.root)
             else:
                 try:
                     delete=messagebox.askyesno("Student Delete page","Do you want to delete this student profile",parent=self.root)
                     if delete>0:
                        conn = mysql.connector.connect(host="localhost",username="root",password="mahakal",database="face_recognizer")
                        my_cursor=conn.cursor()
                        sql="delete from student where student_id = %s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                     else:
                         if not delete:
                             return
                     conn.commit()
                     self.fetch_data()
                     conn.close()
                     messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                         
                 except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                                                                    

  # reset ======
    def reset_data(self):
     self.var_course.set("Select course")
     self.var_year.set("Select year")
     self.var_sem.set("Select Semester")                                                                                                                                                                                                      
     self.var_std_name.set("")
     self.var_div.set("Select division")
     self.var_roll.set("")
     self.var_gender.set("Female")
     self.var_dob.set("")
     self.var_email.set("")
     self.var_phone.set("")
     self.var_address.set("")
     self.var_teacher.set("")
     self.var_radio1.set("")
     self.var_std_id.set("")
     self.var_dep.set("Select Department")

  # === generate data set or take photo sample ====
    
    def generate_dataset(self):
     if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are required",parent=self.root)
     else:
        try:
             conn = mysql.connector.connect(host="localhost",username="root",password="mahakal",database="face_recognizer")
             my_cursor=conn.cursor()
             my_cursor.execute("Select * from student")
             my_result=my_cursor.fetchall()
             id=0
             for x in my_result:
                 id+=1
             my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                                                                                ))           
             conn.commit()
             self.fetch_data()
             self.reset_data()
             conn.close() 

             # ==== load predefined data on face frontls from opencv ====

             face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

             def face_cropped(img):
               gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
               faces=face_classifier.detectMultiScale(gray,1.3,5)
               # scaling factor =1.3
               #minimum neighbour=5

               for(x,y,w,h) in faces:
                   face_cropped=img[y:y+h,x:x+w]
                   return face_cropped

             cap=cv2.VideoCapture(0)
             img_id=0
             while True:
                 ret,my_frame=cap.read()
                 if face_cropped(my_frame) is not None:

                     img_id+=1
                     face=cv2.resize(face_cropped(my_frame),(400,400))
                     face=cv2.cvtColor(face,cv2.COLOR_BGRA2GRAY)
                     file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" 
                     cv2.imwrite(file_name_path,face)
                     cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                     cv2.imshow("Cropped Face",face)

                 if cv2.waitKey(1)==13 or int(img_id)==100:
                     break
             cap.release()
             cv2.destroyAllWindows()
             messagebox.showinfo("Result","Generating data sets completed!!!",parent=self.root)

        except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                                                                    
     







                                                                                     




 
if __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()