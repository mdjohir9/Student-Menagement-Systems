from distutils import command
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
import mysql.connector
from tkinter import messagebox
from turtle import up, update

class Students_menagement:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Lakshmipur Polytechnic institute")

        ###variable
        self.var_department=StringVar()
        self.var_year=StringVar()
        self.var_semister=StringVar()
        self.var_shift=StringVar()

        self.var_stu_name=StringVar()
        self.var_father_name=StringVar()
        self.var_mothers_name=StringVar()
        self.var_reg_no=StringVar()
        self.var_roll_no=StringVar()
        self.var_nid_idno=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_email_address=StringVar()


        #header Image Section

        img1=Image.open("images/headerimage1.jpg")
        img1=img1.resize((517,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1)
        lblimg.place(x=0,y=0,width=517,height=140)

        img2=Image.open("images/headerimage3.jpg")
        img2=img2.resize((517,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2)
        lblimg.place(x=516,y=0,width=517,height=140)

        img3=Image.open("images/hederimage2.jpg")
        img3=img3.resize((517,140),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3)
        lblimg.place(x=1031,y=0,width=517,height=140)

        lbl_title=Label(self.root,text="LAKSHMIPUR  POLYTECHNIC  INSTITUTE",bg="white",fg="green",font=("times new roman","35","bold"))
        lbl_title.place(x=0,y=139, width=1550,height=45)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(lbl_title, font=("times new roman","20","bold"),background="white",foreground="green")
        lbl.place(x=5,y=(-10),width=150,height=50)
        time()

        main_image_frame=Frame(self.root,bg="white",)
        main_image_frame.place(x=0,y=185,width=1550,height=615)

        img4=Image.open("images/bagkground.jpeg")
        img4=img4.resize((1550,715),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_image_frame,image=self.photoimg4)
        lblimg.place(x=0,y=0,width=1550,height=615)


        main_frame=Frame(main_image_frame,bg="white",relief=RIDGE,bd=5)
        main_frame.place(x=20,y=15,width=1500,height=590)


        student_imf_frame=LabelFrame(main_frame,text="Student Information",font=("times new roman",12,"bold"),bg="white",fg="red",relief=RIDGE,bd=5)
        student_imf_frame.place(x=10,y=5,width=675,height=570)

        img5=Image.open("images/hederimage2.jpg")
        img5=img5.resize((665,120),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(student_imf_frame,image=self.photoimg5)
        lblimg.place(x=1,y=1,width=665,height=120)
        ##students course imformetions
        course_inf_frame=LabelFrame(student_imf_frame,text="Student course Information",font=("times new roman",12,"bold"),fg="green",bg="white",relief=RIDGE,bd=2)
        course_inf_frame.place(x=2,y=122,width=655,height=100)

        department = Label(course_inf_frame, text='Department:', font=('arial', 11, 'bold'),bg='white',fg='black')
        department.grid(row=0, column=0, sticky=W, padx=5,)

        combo_department=ttk.Combobox(course_inf_frame,textvariable=self.var_department,font=('arial',11,'bold'),width=25,state='readonly')
        combo_department['value']=('Select options','Computer','Civil',"Electrical","Electronics","Arcitructaar")
        combo_department.current(0)
        combo_department.grid(row=0,column=1,sticky=W,padx=5)


        year_lavel = Label(course_inf_frame, text='Year:', font=('arial', 11, 'bold'),bg='white',fg='black')
        year_lavel.grid(row=0, column=2, sticky=W, padx=5,)

        combo_year=ttk.Combobox(course_inf_frame,textvariable=self.var_year,font=('arial',11,'bold'),width=25,state='readonly')
        combo_year['value']=('Select options','2020-2021','2021-2022',"2022-2023","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028","2028-2029","2029-2030")
        combo_year.current(0)
        combo_year.grid(row=0,column=3)

        lavel_semister = Label(course_inf_frame, text='Semistar:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_semister.grid(row=1, column=0, sticky=W, padx=5,)

        combo_semister=ttk.Combobox(course_inf_frame,textvariable=self.var_semister,font=('arial',11,'bold'),width=25,state='readonly')
        combo_semister['value']=('Select options','First','Second',"Third","Fourth","Fifth","Sixth","Seventh","Eighth")
        combo_semister.current(0)
        combo_semister.grid(row=1,column=1,sticky=W,padx=5,pady=15)

        lavel_shift = Label(course_inf_frame, text='Shift:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_shift.grid(row=1, column=2, sticky=W, padx=5)

        combo_shift=ttk.Combobox(course_inf_frame,textvariable=self.var_shift,font=('arial',11,'bold'),width=25,state='readonly')
        combo_shift['value']=('Select options',"First shift","Second shift")
        combo_shift.current(0)
        combo_shift.grid(row=1,column=3,sticky=W,padx=5,pady=15)


        ###students class informetions
        stu_inf_frame=LabelFrame(student_imf_frame,text="Student Class Information",font=("times new roman",12,"bold"),fg="green",bg="white",relief=RIDGE,bd=2)
        stu_inf_frame.place(x=2,y=222,width=660,height=320)

        lavel_student_name = Label(stu_inf_frame,text='Student Name:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_student_name.grid(row=0, column=0, sticky=W, padx=5)

        name_text=ttk.Entry(stu_inf_frame, textvariable=self.var_stu_name,font=("times new roman",11,"bold"),width=25)
        name_text.grid(row=0,column=1,padx=5,pady=5)

        lavel_fathers_name = Label(stu_inf_frame, text='Fathers Name:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_fathers_name.grid(row=1, column=0, sticky=W, padx=5)

        fathers_name_txt=ttk.Entry(stu_inf_frame,textvariable=self.var_father_name,font=("times new roman",11,"bold"),width=25)
        fathers_name_txt.grid(row=1,column=1,padx=5,pady=5)


        lavel_mothers_name = Label(stu_inf_frame, text='Moth Name:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_mothers_name.grid(row=0, column=2, sticky=W, padx=5)

        mothers_name_txt=ttk.Entry(stu_inf_frame,textvariable=self.var_mothers_name,font=("times new roman",11,"bold"),width=25)
        mothers_name_txt.grid(row=0,column=3,padx=5,pady=5)


        lavel_reg_no = Label(stu_inf_frame, text='Reg No:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_reg_no.grid(row=1, column=2, sticky=W, padx=5)

        reg_text=ttk.Entry(stu_inf_frame,textvariable=self.var_reg_no,font=("times new roman",11,"bold"),width=25)
        reg_text.grid(row=1,column=3,padx=5,pady=5)

        lavel_student_roll = Label(stu_inf_frame, text='Roll No:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_student_roll.grid(row=2, column=0, sticky=W, padx=5)

        roll_no_text=ttk.Entry(stu_inf_frame,textvariable=self.var_roll_no,font=("times new roman",11,"bold"),width=25)
        roll_no_text.grid(row=2,column=1,padx=5,pady=5)


        lavel_nid_no = Label(stu_inf_frame, text='NID/ID NO:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_nid_no.grid(row=2, column=2, sticky=W, padx=5)

        nid_text=ttk.Entry(stu_inf_frame,textvariable=self.var_nid_idno,font=("times new roman",11,"bold"),width=25)
        nid_text.grid(row=2,column=3,padx=5,pady=5)


        lavel_gender = Label(stu_inf_frame, text='Gender:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_gender.grid(row=3, column=0, sticky=W, padx=5)

        combo_gender=ttk.Combobox(stu_inf_frame,textvariable=self.var_gender,font=('arial',11,'bold'),width=23,state='readonly')
        combo_gender['value']=('Select options',"Meale","Feamle","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1,sticky=W,padx=5,pady=10)


        lavel_phone = Label(stu_inf_frame, text='Phone No:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_phone.grid(row=3, column=2, sticky=W, padx=5)

        phone_text=ttk.Entry(stu_inf_frame,textvariable=self.var_phone,font=("times new roman",11,"bold"),width=25)
        phone_text.grid(row=3,column=3,padx=5,pady=5)

        lavel_adress = Label(stu_inf_frame, text='Address:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_adress.grid(row=4, column=0, sticky=W, padx=5)

        address_text=ttk.Entry(stu_inf_frame,textvariable=self.var_address,font=("times new roman",11,"bold"),width=25)
        address_text.grid(row=4,column=1,padx=5,pady=5)

        lavel_Emali = Label(stu_inf_frame, text='Email Adrs:', font=('arial', 11, 'bold'),bg='white',fg='black')
        lavel_Emali.grid(row=4, column=2, sticky=W, padx=5)

        email_text=ttk.Entry(stu_inf_frame,textvariable=self.var_email_address,font=("times new roman",11,"bold"),width=25)
        email_text.grid(row=4,column=3,padx=5,pady=5)

        ##button section
        button_frame=Frame(stu_inf_frame,bg="white",relief=RIDGE,bd=2)
        button_frame.place(x=2,y=200,width=650,height=100)


        save_btn=Button(button_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),bg="green",fg="white",bd=2,width=15,height=1,cursor="hand1")
        save_btn.grid(row=0,column=0,padx=2,pady=2)

        update_btn=Button(button_frame,command=self.update_data,text="Update",font=("arial",15,"bold"),bg="green",fg="white",bd=2,width=15,height=1,cursor="hand1")
        update_btn.grid(row=0,column=1,padx=2,pady=2)

        delete_btn=Button(button_frame,command=self.delete_data,text="Delete",font=("arial",15,"bold"),bg="green",fg="white",bd=2,width=15,height=1,cursor="hand1")
        delete_btn.grid(row=0,column=2,padx=2,pady=2)

        resat_btn=Button(button_frame,text="Resat",font=("arial",15,"bold"),bg="green",fg="white",bd=2,width=15,height=1,cursor="hand1")
        resat_btn.grid(row=1,column=0,padx=2,pady=2)

        clear_btn=Button(button_frame,command=self.clear_data,text="Clear",font=("arial",15,"bold"),bg="green",fg="white",bd=2,width=15,height=1,cursor="hand1")
        clear_btn.grid(row=1,column=1,padx=2,pady=2)

        exit_btn=Button(button_frame,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="red",fg="white",bd=2,width=15,height=1,cursor="hand1")
        exit_btn.grid(row=1,column=2,padx=2,pady=2)








        #####Students Details Frame
        student_details_frame=LabelFrame(main_frame,text="Students Details",font=("times new roman",12,"bold"),bg="white",fg="red",relief=RIDGE,bd=5)
        student_details_frame.place(x=685,y=5,width=800,height=570)

        img6=Image.open("images/headerimage1.jpg")
        img6=img6.resize((785,160),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lblimg=Label(student_details_frame,image=self.photoimg6)
        lblimg.place(x=1,y=1,width=785,height=160)

        student_details_search_frame=LabelFrame(main_frame,text="View Students Details & search System",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RIDGE,bd=5)
        student_details_search_frame.place(x=695,y=180,width=780,height=65)

        search_by = Label(student_details_search_frame, text = 'Search By', font = ('arial', 11, 'bold'), bg = 'red', fg = 'white')
        search_by.grid(row=0, column=0, sticky=W, padx=5,pady=5 )

        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(student_details_search_frame,textvariable=self.var_com_search, font=('arial', 11, 'bold'),width=18, state='readonly')
        combo_search_box['value'] = ('Select options', 'Reg No', 'Roll No')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5,pady=5)

        self.var_search = StringVar()
        search_text = ttk.Entry(student_details_search_frame,textvariable=self.var_search, width=22, font=('arial', 11, 'bold'))
        search_text.grid(row=0, column=2, sticky=W, padx=5,pady=5)

        serch_btn = Button(student_details_search_frame,command=self.search_data,text='Search', font=('arial', 13, 'bold'), width=14, bg='green', fg='white')
        serch_btn.grid(row=0, column=3, padx=3, pady=4)

        # all button
        show_all_button = Button(student_details_search_frame,text='Show All', font=('arial', 13, 'bold'), width=14, bg='green', fg='white')
        show_all_button.grid(row=0, column=4, padx=3, pady=4)

        ##tabel Frame

        table_frame=Frame(main_frame,bg="white",relief=RIDGE,bd=5)
        table_frame.place(x=695,y=250,width=780,height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=("Department", "Year", "Semistar", "Shift", "Student_Name", "Fathers_Name", "Mothers_Name", "Reg_No", "Roll_No", "NID/ID_No", "Gender", "Phone_No", "Address", "Email_Address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('Department', text='Department')
        self.criminal_table.heading('Year', text='Year')
        self.criminal_table.heading('Semistar', text='Semistar')
        self.criminal_table.heading('Shift', text='Shift')
        self.criminal_table.heading('Student_Name', text='Student Name')
        self.criminal_table.heading('Fathers_Name', text='Fathers Name')
        self.criminal_table.heading('Mothers_Name', text='Mothers Name')
        self.criminal_table.heading('Reg_No', text='Reg No')
        self.criminal_table.heading('Roll_No', text='Roll No')
        self.criminal_table.heading('NID/ID_No', text='NID/ID No')
        self.criminal_table.heading('Gender', text='Gender')
        self.criminal_table.heading('Phone_No', text='Phone No')
        self.criminal_table.heading('Address', text='Address')
        self.criminal_table.heading('Email_Address', text='Email Address')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column('Department', width=100)
        self.criminal_table.column('Year', width=100)
        self.criminal_table.column('Semistar', width=100)
        self.criminal_table.column('Shift', width=100)
        self.criminal_table.column('Student_Name', width=100)
        self.criminal_table.column('Fathers_Name', width=100)
        self.criminal_table.column('Mothers_Name', width=100)
        self.criminal_table.column('Reg_No', width=100)
        self.criminal_table.column('Roll_No', width=100)
        self.criminal_table.column('NID/ID_No', width=100)
        self.criminal_table.column('Gender', width=100)
        self.criminal_table.column('Phone_No', width=100)
        self.criminal_table.column('Address', width=100)
        self.criminal_table.column('Email_Address', width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()


    ###add Functions
    def add_data(self):
        if self.var_department.get()=="":
            messagebox.showerror("Error","All Fields are requride")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="lakshmipur_polytechnic_institute")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_inf values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_department.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semister.get(),
                                                                                                                self.var_shift.get(),

                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_father_name.get(),
                                                                                                                self.var_mothers_name.get(),
                                                                                                                self.var_reg_no.get(),
                                                                                                                self.var_roll_no.get(),
                                                                                                                self.var_nid_idno.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_email_address.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Record hase been added")
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}")

    ###fetch data

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="lakshmipur_polytechnic_institute")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_inf")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    ###get Cursor

    def get_cursor(self,events=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content["values"]

        self.var_department.set(data[0])
        self.var_year.set(data[1])
        self.var_semister.set(data[2])
        self.var_shift.set(data[3])

        self.var_stu_name.set(data[4])
        self.var_father_name.set(data[5])
        self.var_mothers_name.set(data[6])
        self.var_reg_no.set(data[7])
        self.var_roll_no.set(data[8])
        self.var_nid_idno.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_email_address.set(data[13])


    ##update finctions

    def update_data(self):
        if self.var_reg_no.get() == "":
            messagebox.showerror("Error", "All Fields are requride")
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure update this criminal record')
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="lakshmipur_polytechnic_institute")
                    my_cursor = conn.cursor()
                    my_cursor.execute('update student_inf set Department=%s,Year=%s,Semistar=%s,Shift=%s,Student_Name=%s,Fathers_Name=%s,Mothers_Name=%s,=%s,Roll_No=%s,NID/ID_No=%s,Gender=%s,Phone_No=%s,Address=%s,Email_Address where Reg_No=%s ',
                        (

                            self.var_department.get(),
                            self.var_year.get(),
                            self.var_semister.get(),
                            self.var_shift.get(),

                            self.var_stu_name.get(),
                            self.var_father_name.get(),
                            self.var_mothers_name.get(),
                            self.var_roll_no.get(),
                            self.var_nid_idno.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_email_address.get(),
                            self.var_reg_no.get()


                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Crime record Successfully updated')
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")

    ###dellate functions
    def delete_data(self):
        if self.var_reg_no.get() == "":
            messagebox.showerror("Error", "All Fields are requrided")
        else:
            try:
                Delete = messagebox.askyesno('Delete', 'Are you sure delete this criminal record')
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="lakshmipur_polytechnic_institute")
                    my_cursor = conn.cursor()

                    sql='delete from student_inf where Reg_No=%s'
                    value=(self.var_reg_no.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Crime record Successfully deleted ')
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")

    ###clear Data

    def clear_data(self):

        self.var_department.set("")
        self.var_year.set("")
        self.var_semister.set("")
        self.var_shift.set("")

        self.var_stu_name.set("")
        self.var_father_name.set("")
        self.var_mothers_name.set("")
        self.var_roll_no.set("")
        self.var_nid_idno.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_email_address.set("")
        self.var_reg_no.set("")


    ###search data
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror("Error", "All Fields are requrided")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="lakshmipur_polytechnic_institute")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student_inf where ' +str(self.var_com_search.get())+" LIKE'"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!= 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")











if __name__=="__main__":
    root=Tk()
    obj=Students_menagement(root)
    root.mainloop()