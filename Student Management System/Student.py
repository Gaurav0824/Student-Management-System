from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
        def __init__(self, root):

                self.root=root
                self.root.title("Student Management System".center(420))
                self.root.geometry("1350x700+0+0")
                self.root.configure(background = "black")
                bg_color="#074463"

                title=Label(self.root, bd=10, relief=GROOVE, text="Student Management System",font=("times new roman", 40, "bold"),bg="yellow",fg="red")
                title.pack(side=TOP,  fill=X)

                #------------Variables--------------#

                self.name_var=StringVar()
                self.Roll_No_var=StringVar()
                self.email_var=StringVar()
                self.gender_var=StringVar()
                self.contact_var=StringVar()
                self.dob_var=StringVar()
                self.search_by=StringVar()
                self.search_txt=StringVar()

                #-------Manage Frame----------------#

                Manage_Frame=Frame(self.root,bd=4, relief=RIDGE,bg=bg_color)
                Manage_Frame.place(x=20,y=100,width=450,height=590)

                m_title=Label(Manage_Frame,text="Manage Students",bg=bg_color,fg="white",font=("times new roman",30,"bold"))
                m_title.grid(row=0, columnspan=2,pady=20)

                #   ----------------------------------------------------------------------------

                lbl_roll=Label(Manage_Frame,text="Name",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=1, column=0,padx=20,pady=10,sticky="w")

                txt_roll=Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=1, column=1,padx=20,pady=10,sticky="w")

                #   ---------------------------------------------------------------------------- 

                lbl_roll=Label(Manage_Frame, text="Roll No.",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=2, column=0,padx=20,pady=10,sticky="w")

                txt_roll=Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=2, column=1,padx=20,pady=10,sticky="w")

                #   ----------------------------------------------------------------------------

                lbl_roll=Label(Manage_Frame,text="Email",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=3, column=0,padx=20,pady=10,sticky="w")

                txt_roll=Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=3, column=1,padx=20,pady=10,sticky="w")

                #   ----------------------------------------------------------------------------

                lbl_roll=Label(Manage_Frame,text="Gender",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=4, column=0,padx=20,pady=10,sticky="w")

                combo_gender=ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman",13,"bold"),state='readonly')
                combo_gender['values']=("Male","Female","Others")
                combo_gender.grid(row=4, column=1,padx=20,pady=10)

                #   ----------------------------------------------------------------------------

                lbl_roll=Label(Manage_Frame,text="Contact",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=5, column=0,padx=20,pady=10,sticky="w")

                txt_roll=Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=5, column=1,padx=20,pady=10,sticky="w")

                #   ----------------------------------------------------------------------------

                lbl_roll=Label(Manage_Frame,text="D.O.B",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=6, column=0,padx=20,pady=10,sticky="w")

                txt_roll=Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=6, column=1,padx=20,pady=10,sticky="w")

                #   ----------------------------------------------------------------------------        

                lbl_roll=Label(Manage_Frame,text="Address",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=7, column=0,padx=20,pady=10,sticky="w")

                self.txt_Address=Text(Manage_Frame, width=23,height=4, font=("",12))
                self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

                #-------Button Frame-------------#

                btn_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
                btn_Frame.place(x=10,y=520,width=425)

                Addbtn=Button(btn_Frame, command=self.add_students, text="Add", font="bold", width=8).grid(row=0,column=0,padx=15, pady=10)
                Updatebtn=Button(btn_Frame, command=self.update, text="Update", font="bold", width=8).grid(row=0,column=1,padx=10, pady=10)
                Clearbtn=Button(btn_Frame,command=self.clear,text="Clear", font="bold", width=8).grid(row=0,column=2,padx=10, pady=10)
                Deletebtn=Button(btn_Frame,command=self.Delete_data, text="Delete", font="bold", width=8).grid(row=0,column=3,padx=10, pady=10)

                #-------Detail Frame----------------#

                Detail_Frame=Frame(self.root,bd=4, relief=RIDGE,bg=bg_color)
                Detail_Frame.place(x=500,y=100,width=820,height=590)


                lbl_Search=Label(Detail_Frame,text="Search",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
                lbl_Search.grid(row=0, column=0,padx=20,pady=10,sticky="w")

                combo_Search=ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman",15,"bold"),state='readonly')
                combo_Search['values']=("Name","Roll No.","Contact")
                combo_Search.grid(row=0, column=1,padx=20,pady=10)

                txt_Search=Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
                txt_Search.grid(row=0, column=2,padx=20,pady=10,sticky="w")

                searchbtn=Button(Detail_Frame,command=self.search_data, text="Search", width=10,pady=5).grid(row=0,column=3,padx=10, pady=10)
                showbtn=Button(Detail_Frame, command=self.fetch_data, text="Show All", width=10,pady=5).grid(row=0,column=4,padx=10, pady=10)

                #---------Table Frame-------------#

                Table_Frame=Frame(Detail_Frame,bd=4, relief=RIDGE,bg=bg_color)
                Table_Frame.place(x=25,y=70,width=760,height=500)

                scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
                scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
                self.Student_table=ttk.Treeview(Table_Frame,columns=("Name","Roll No.","Email","Gender","Contact","D.O.B", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.Student_table.xview)
                scroll_y.config(command=self.Student_table.yview)

                self.Student_table.heading("Name", text="Name")
                self.Student_table.heading("Roll No.", text="Roll No.")
                self.Student_table.heading("Email", text="Email")
                self.Student_table.heading("Gender", text="Gender")
                self.Student_table.heading("Contact", text="Contact")
                self.Student_table.heading("D.O.B", text="D.O.B")
                self.Student_table.heading("Address", text="Address")
                self.Student_table.column("Name", width=100)
                self.Student_table.column("Roll No.", width=100)
                self.Student_table.column("Email", width=200)
                self.Student_table.column("Gender", width=70)
                self.Student_table.column("Contact", width=100)
                self.Student_table.column("D.O.B", width=70)
                self.Student_table.column("Address", width=500)
                self.Student_table['show']='headings'

                self.Student_table.pack(fill=BOTH,expand=1)
                self.Student_table.bind("<ButtonRelease-1>",self.getcursor)
                self.fetch_data()


        def add_students(self):
                if self.Roll_No_var.get()==""or self.name_var.get()=="":
                        messagebox.showerror("Erroe","All Fields are required")
                else:

                        con=pymysql.connect(host="127.0.0.1", user="root", password="",database="std_management")
                        cur=con.cursor() 
                        cur.execute("insert into std values(%s,%s,%s,%s,%s,%s,%s)",(    self.name_var.get(),
                                                                                        self.Roll_No_var.get(),
                                                                                        self.email_var.get(),
                                                                                        self.gender_var.get(),
                                                                                        self.contact_var.get(),
                                                                                        self.dob_var.get(), 
                                                                                        self.txt_Address.get('1.0',END))
                                                                                )
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        con.close()
                        messagebox.showinfo("Success","Record has been inserted!!")


        def search_data(self):

                con=pymysql.connect(host="127.0.0.1", user="root", password="",database="std_management")
                cur=con.cursor()

                cur.execute(""" select * from std where"""+ str(self.search_by.get())+"""  like "%""" +str(self.search_txt.get())+"""%" ;""")
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Student_table.delete(*self.Student_table.get_children())
                        for row in rows:
                                self.Student_table.insert('',END,values=row)
                        con.commit()
                con.close()

        def fetch_data(self):
                con=pymysql.connect(host="127.0.0.1", user="root", password="",database="std_management")
                cur=con.cursor()
                cur.execute("select * from std")
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Student_table.delete(*self.Student_table.get_children())
                        for row in rows:
                                self.Student_table.insert('',END,values=row)
                        con.commit()
                con.close()

        def clear(self):
                self.name_var.set("")
                self.Roll_No_var.set("")
                self.email_var.set("")
                self.gender_var.set("")
                self.contact_var.set("")
                self.dob_var.set("")
                self.txt_Address.delete("1.0",END)

        def getcursor(self,ev):
                cursor_row=self.Student_table.focus()
                Content=self.Student_table.item(cursor_row)
                row=Content['values']
                #print(row)
                self.name_var.set(row[0])
                self.Roll_No_var.set(row[1])
                self.email_var.set(row[2])
                self.gender_var.set(row[3])
                self.contact_var.set(row[4])
                self.dob_var.set(row[5])
                self.txt_Address.delete(END,row[6])

        def update(self):

                con=pymysql.connect(host="127.0.0.1", user="root", password="",database="std_management")
                cur=con.cursor() 
                cur.execute("update std set Name=%s, Email=%s, Gender=%s, Contact=%s, DOB=%s, Address=%s where Roll_No=%s",( self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.dob_var.get(), 
                                                                                self.txt_Address.get('1.0',END),
                                                                                self.Roll_No_var.get())
                                                                                )
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()  

        def Delete_data(self):
                con=pymysql.connect(host="127.0.0.1", user="root", password="",database="std_management")
                cur=con.cursor()
                cur.execute("delete from std where Roll_No=%s",self.Roll_No_var.get())
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()

        
           
         
                     
root=Tk()
obj=Student(root)
root.mainloop()