from tkinter import *
import time
import random
from tkinter import Entry,Tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog,messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\Documents\Cafe Management Project\login_background.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1550,height=800)

        frame=Frame(self.root,bg="black")
        frame.place(x=460,y=170,width=540,height=350)

        # ===============label========================
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=100)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=200,y=100)

        passward = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        passward.place(x=70, y=150)
        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=200, y=150)

        #===========login btn=====================
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=230,y=200,width=120,height=35)

        #==============register btn==================
        registerbtn=Button(frame, text="New User? Register",command=self.register_window, font=("times new roman", 10, "bold"),borderwidth=0, bd=3, relief=RIDGE, fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=210, y=280, width=160)

        

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="mini" and self.txtpass.get()=="project":
            messagebox.showinfo("Success","Welcome!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="2004", database="register")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from my_data where username=%s and password=%s",(
                                                                                   self.txtuser.get(),
                                                                                   self.txtpass.get()
                                                                                 ))
            row=my_cursor.fetchone()
            print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=CafeManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()





class Register:

    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===================variables=======================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_username = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ===================bg image======================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\hp\Documents\Cafe Management Project\register_bg.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1660, height=900)

        # =====================main frame========================
        frame=Frame(self.root,bg="white")
        frame.place(x=400,y=200,width=730,height=500)
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=250,y=20)

        # ===================label & entry==================
        fname  = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=80)
        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=110,width=250)

        l_name  = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=350, y=80)
        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=350, y=110, width=250)

        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=150)
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=180, width=250)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white")
        username.place(x=350, y=150)
        self.txt_username = ttk.Entry(frame,textvariable=self.var_username, font=("times new roman", 15, "bold"))
        self.txt_username.place(x=350, y=180, width=250)

        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=220)
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend name","Your pet name")
        self.combo_security_Q.place(x=50, y=250, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=350, y=220)
        self.txt_security_A = ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security_A.place(x=350, y=250, width=250)

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=290)
        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"),show="*")
        self.txt_pswd.place(x=50, y=320, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=350, y=290)
        self.confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"),show="*")
        self.confirm_pswd.place(x=350, y=320, width=250)

        # ==================register & login btn======================

        registerbtn = Button(frame,command=self.register_data, text="Register", font=("times new roman", 15, "bold"), borderwidth=0,bd=3, relief=RIDGE, fg="white", bg="darkgreen", activeforeground="white",activebackground="black")
        registerbtn.place(x=280, y=380, width=120,height=30)

        loginbtn = Button(frame,command=self.login_return, text="Login Now", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="darkblue", activeforeground="white", activebackground="black")
        loginbtn.place(x=520, y=420, width=120, height=30)

    # =======================function declaration===================
    def register_data(self):
            if self.var_fname.get()=="" or self.var_username.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password & confirm Password must be same")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="2004",database="register")
                my_cursor=conn.cursor()
                query=("select * from my_data where username=%s")
                value=(self.var_username.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists,please try another username",parent=self.root)
                else:
                    my_cursor.execute("insert into my_data values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_fname.get(),
                                                                                                            self.var_lname.get(),
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_securityQ.get(),
                                                                                                            self.var_securityA.get(),
                                                                                                            self.var_username.get(),
                                                                                                            self.var_pass.get()

                                                                                                           ))
                    messagebox.showinfo("Success", "Register Successfully", parent=self.root)
                conn.commit()
                conn.close()


    def login_return(self):
        self.root.destroy()


class CafeManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Cafe Management")
        self.root.geometry("1550x800+0+0")

        # ==========1st img==================
        img1=Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img1.jpeg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lglimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lglimg.place(x=0,y=0,width=1550,height=140)

        # ==============logo============================
        img2=Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img2.jpeg")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        # ===============title============================
        lbl_title=Label(self.root,text="CAFE  MANAGEMENT  SYSTEM",font=("times new roman",40,"bold"),bg="tan",fg="Sienna",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ================main frame======================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1980,height=620)

        # ===============menu============================
        lbl_title = Label(self.root, text=" MAIN MENU", font=("times new roman", 20, "bold"), bg="Peru",fg="saddlebrown", bd=4, relief=RIDGE)
        lbl_title.place(x=-250, y=190, width=1980)

        # ================btn frame======================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=1980, height=50)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=40,font=("times new roman", 16, "bold"), bg="SandyBrown",fg="Sienna",bd=1,cursor="hand1")
        cust_btn.grid(row=0,column=0,padx=5)

        order_btn=Button(btn_frame,text="ORDER",command=self.order_details,width=40,font=("times new roman", 16, "bold"), bg="SandyBrown",fg="Sienna",bd=1,cursor="hand1")
        order_btn.grid(row=0,column=1,padx=5)



        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=40,font=("times new roman", 16, "bold"), bg="SandyBrown",fg="Sienna",bd=1,cursor="hand1")
        logout_btn.grid(row=0,column=4,padx=5)






        #===========================right side image===========================

        img3=Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img3.jpeg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=82,width=1310,height=590)



        #==========================down image==================================


        img4=Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img6.jpeg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)


        img5=Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img5.jpeg")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=415,width=230,height=190)

        img6 = Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img4.jpeg")
        img6 = img6.resize((230, 190), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg = Label(main_frame, image=self.photoimg6, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=85, width=230, height=140)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def order_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Order_win(self.new_window)
    def logout(self):
        self.root.destroy()


class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Cafe Management")
        self.root.geometry("1295x475+230+310")

        #==================variables========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.search_var=StringVar()
        self.txt_search=StringVar()

        # ===============title============================
        lbl_title = Label(self.root, text=" ADD CUSTOMER DETAILS", font=("times new roman", 20, "bold"), bg="tan",
                          fg="Sienna", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==============logo============================
        img2 = Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img2.jpeg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=3, width=100, height=40)

        #================LabelFrame=======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 12, "bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #==================labes and entries================
        #CustRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref ID:",font=("ARIAL", 12, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("ARIAL", 13, "bold"),state='readonly')
        entry_ref.grid(row=0,column=1)

        #CustName
        cname = Label(labelframeleft, text="Customer Name:", font=("ARIAL", 12, "bold"), padx=2,pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, width=29, font=("ARIAL", 13, "bold"))
        txtcname.grid(row=1, column=1)

        #CustMobile
        cmobile = Label(labelframeleft, text="Mobile:", font=("ARIAL", 12, "bold"), padx=2, pady=6)
        cmobile.grid(row=2, column=0, sticky=W)

        txtcmobile = ttk.Entry(labelframeleft,textvariable=self.var_cust_mobile, width=29, font=("ARIAL", 13, "bold"))
        txtcmobile.grid(row=2, column=1)

        #CustEmail
        cEmail = Label(labelframeleft, text="Email:", font=("ARIAL", 12, "bold"), padx=2, pady=6)
        cEmail.grid(row=3, column=0, sticky=W)

        txtcEmail = ttk.Entry(labelframeleft,textvariable=self.var_cust_email, width=29, font=("ARIAL", 13, "bold"))
        txtcEmail.grid(row=3, column=1)


        #=============================btns=====================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd= Button(btn_frame, text="ADD",command=self.add_data , width=10,font=("ARIAL", 11, "bold"), bg="chocolate", fg="white")
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="Update",command=self.update, width=10, font=("ARIAL", 11, "bold"), bg="chocolate", fg="white")
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, text="Delete",command=self.delete, width=10, font=("ARIAL", 11, "bold"), bg="chocolate", fg="white")
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="Reset",command=self.reset, width=10, font=("ARIAL", 11, "bold"), bg="chocolate", fg="white")
        btnreset.grid(row=0, column=3, padx=1)

        # ================TableFrame=======================
        Tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                    font=("times new roman", 12, "bold"), padx=2 )
        Tableframe.place(x=435, y=50, width=860, height=490)

        lblsearchby =Label(Tableframe, font=("ARIAL", 12, "bold"),text="Search by:",bg="chocolate",fg="white")
        lblsearchby.grid(row=0, column=0,sticky=W,padx=2)


        commbo_search=ttk.Combobox(Tableframe,textvariable=self.search_var,font=("ARIAL",12,"bold"),width=24,state="readonly")
        commbo_search["value"]=("cust_id","cust_mobile")
        commbo_search.current(0)
        commbo_search.grid(row=0,column=1,padx=2)

        txtsearch = ttk.Entry(Tableframe,textvariable=self.txt_search, width=29, font=("ARIAL", 13, "bold"))
        txtsearch.grid(row=0, column=2,padx=2)

        btnsearch = Button(Tableframe, text="Search",command=self.search, width=10, font=("ARIAL", 11, "bold"), bg="chocolate", fg="white")
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(Tableframe, text="Show All",command=self.fetch_data, width=10, font=("ARIAL", 11, "bold"), bg="chocolate", fg="white")
        btnshowall.grid(row=0, column=4, padx=1)



        #=========================show data table=========================

        details_table = Frame(Tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=320)


        Scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_details_table=ttk.Treeview(details_table,column=("ref","name","mobile","email"), xscrollcommand=Scrollbar_x.set, yscrollcommand=Scrollbar_y.set)


        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)

        Scrollbar_x.config(command=self.Cust_details_table.xview)
        Scrollbar_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("ref",text="Ref ID")
        self.Cust_details_table.heading("name", text="Customer name")
        self.Cust_details_table.heading("mobile", text="Mobile no")
        self.Cust_details_table.heading("email", text="Email")

        self.Cust_details_table["show"]="headings"
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_cust_mobile.get()=="" or self.var_cust_email.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2004",database="register")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(),self.var_cust_mobile.get(),self.var_cust_email.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="register")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_mobile.set(row[2]),
        self.var_cust_email.set(row[3])

    def update(self):
        if self.var_cust_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="register")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set cust_name=%s,cust_mobile=%s,cust_email=%s where cust_id=%s",(self.var_cust_name.get(),self.var_cust_mobile.get(),self.var_cust_email.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully!",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Cafe Management System","Do you want to delete this customer",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="register")
            my_cursor = conn.cursor()
            query="delete from customer where cust_id=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_cust_name.set(""),
        self.var_cust_mobile.set(""),
        self.var_cust_email.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="register")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()



class Order_win:


    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management")
        self.root.geometry("1295x475+230+310")



        # ===============title============================
        lbl_title = Label(self.root, text="Order", font=("times new roman", 20, "bold"), bg="tan",
                          fg="Sienna", bd=6, relief=RIDGE)
        lbl_title.place(x=-250, y=0, width=1980, height=50)

        # ==============logo============================
        img2 = Image.open(r"C:\Users\hp\Documents\Cafe Management Project\img2.jpeg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=3, width=100, height=40)

        # ==================frames============================
        menuframe = Frame(root, bd=10, relief=RIDGE)
        menuframe.pack(side=LEFT)

        costframe = Frame(menuframe, bd=4, relief=RIDGE)
        costframe.pack(side=BOTTOM)

        foodframe = LabelFrame(menuframe, text="Food", font=("ARIAL", 12, "bold"), bd=10, relief=RIDGE)
        foodframe.pack(side=LEFT)

        drinksframe = LabelFrame(menuframe, text="Drinks", font=("ARIAL", 12, "bold"), bd=10, relief=RIDGE)
        drinksframe.pack(side=LEFT)

        desertsframe = LabelFrame(menuframe, text="Deserts", font=("ARIAL", 12, "bold"), bd=10, relief=RIDGE)
        desertsframe.pack(side=LEFT)

        rightframe = Frame(root, bd=15, relief=RIDGE)
        rightframe.pack(side=RIGHT)

        receiptframe = Frame(rightframe, bd=4, relief=RIDGE)
        receiptframe.pack()

        buttonframe = Frame(rightframe, bd=4, relief=RIDGE)
        buttonframe.pack()
        # variable
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()

        e_burger=StringVar()
        e_pizza=StringVar()
        e_frenchfries=StringVar()
        e_sandwich=StringVar()
        e_momos=StringVar()

        e_chocolatemilkshake = StringVar()
        e_mangomilkshake = StringVar()
        e_coffee = StringVar()
        e_sprite = StringVar()
        e_latte = StringVar()

        e_Hotchocolate = StringVar()
        e_Bwaffle = StringVar()
        e_Donuts = StringVar()
        e_cake = StringVar()
        e_icecream = StringVar()


        costoffoodvar=StringVar()
        costofdrinksvar=StringVar()
        costofdesertsvar=StringVar()
        subtotalvar=StringVar()
        servicetaxvar=StringVar()
        totalcostvar=StringVar()

        e_burger.set("0")
        e_pizza .set("0")
        e_frenchfries.set("0")
        e_sandwich.set("0")
        e_momos.set("0")
        e_chocolatemilkshake.set("0")
        e_mangomilkshake.set("0")
        e_coffee.set("0")
        e_sprite.set("0")
        e_latte.set("0")
        e_Hotchocolate.set("0")
        e_Bwaffle.set("0")
        e_Donuts.set("0")
        e_cake.set("0")
        e_icecream.set("0")
        def changeburgerstate():
            if var1.get() == 1:
                textburger.config(state=NORMAL)
                textburger.delete(0,END)
                textburger.focus()
            else:
                textburger.config(state=DISABLED)
                e_burger.set('0')

        def changepizzastate():
           if var2.get() == 1:
               textpizza.config(state=NORMAL)
               textpizza.delete(0, END)
               textpizza.focus()
           else:
               textpizza.config(state=DISABLED)
               e_pizza.set('0')

        def changefrenchfriesstate():
           if var3.get() == 1:
               textfrenchfries.config(state=NORMAL)
               textfrenchfries.delete(0, END)
               textfrenchfries.focus()
           else:
               textfrenchfries.config(state=DISABLED)
               e_frenchfries.set('0')

        def changesandwichstate():
           if var4.get() == 1:
               textsandwich.config(state=NORMAL)
               textsandwich.delete(0, END)
               textsandwich.focus()
           else:
               textsandwich.config(state=DISABLED)
               e_sandwich.set('0')

        def changemomosstate():
           if var5.get() == 1:
               textmomos.config(state=NORMAL)
               textmomos.delete(0, END)
               textmomos.focus()
           else:
               textmomos.config(state=DISABLED)
               e_momos.set('0')

        def changechocolatemilkshakestate():
           if var6.get() == 1:
               textchocolatemilkshake.config(state=NORMAL)
               textchocolatemilkshake.delete(0, END)
               textchocolatemilkshake.focus()
           else:
               textchocolatemilkshake.config(state=DISABLED)
               e_chocolatemilkshake.set('0')

        def changemangomilkshakestate():
           if var7.get() == 1:
               textmangomilkshake.config(state=NORMAL)
               textmangomilkshake.delete(0, END)
               textmangomilkshake.focus()
           else:
               textmangomilkshake.config(state=DISABLED)
               e_mangomilkshake.set('0')

        def changecoffeestate():
           if var8.get() == 1:
               textcoffee.config(state=NORMAL)
               textcoffee.delete(0, END)
               textcoffee.focus()
           else:
               textcoffee.config(state=DISABLED)
               e_coffee.set('0')

        def changespritestate():
           if var9.get() == 1:
               textsprite.config(state=NORMAL)
               textsprite.delete(0, END)
               textsprite.focus()
           else:
               textsprite.config(state=DISABLED)
               e_sprite.set('0')

        def changelattestate():
           if var10.get() == 1:
               textlatte.config(state=NORMAL)
               textlatte.delete(0, END)
               textlatte.focus()
           else:
               textlatte.config(state=DISABLED)
               e_latte.set('0')

        def changeHotchocolatestate():
           if var11.get() == 1:
               textHotchocolate.config(state=NORMAL)
               textHotchocolate.delete(0, END)
               textHotchocolate.focus()
           else:
               textHotchocolate.config(state=DISABLED)
               e_Hotchocolate.set('0')

        def changeBwafflestate():
           if var12.get() == 1:
               textBwaffle.config(state=NORMAL)
               textBwaffle.delete(0, END)
               textBwaffle.focus()
           else:
               textBwaffle.config(state=DISABLED)
               e_Bwaffle.set('0')

        def changeDonutsstate():
           if var13.get() == 1:
               textDonuts.config(state=NORMAL)
               textDonuts.delete(0, END)
               textDonuts.focus()
           else:
               textDonuts.config(state=DISABLED)
               e_Donuts.set('0')

        def changeCakestate():
           if var14.get() == 1:
               textcake.config(state=NORMAL)
               textcake.delete(0, END)
               textcake.focus()
           else:
               textcake.config(state=DISABLED)
               e_cake.set('0')

        def changeicecreamstate():
           if var15.get() == 1:
               texticecream.config(state=NORMAL)
               texticecream.delete(0, END)
               texticecream.focus()
           else:
               texticecream.config(state=DISABLED)
               e_icecream.set('0')

        def totalcost():
            global priceoffood,priceofdrinks,priceofdesserts,subtotalofItems
            if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or \
                var10.get() != 0 or var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 :
                item1=int(e_burger.get())
                item2 = int(e_pizza.get())
                item3 = int(e_frenchfries.get())
                item4 = int(e_sandwich.get())
                item5 = int(e_momos.get())
                item6 = int(e_chocolatemilkshake.get())
                item7 = int(e_mangomilkshake.get())
                item8 = int(e_coffee.get())
                item9 = int(e_sprite.get())
                item10 = int(e_latte.get())
                item11 = int(e_Hotchocolate.get())
                item12 = int(e_Bwaffle.get())
                item13 = int(e_Donuts.get())
                item14 = int(e_cake.get())
                item15 = int(e_icecream.get())

                priceoffood=(item1*80)+(item2*150)+(item3*120)+(item4*50)+(item5*80)
                priceofdrinks=(item6*90)+(item7*70)+(item8*45)+(item9*20)+(item10*100)
                priceofdesserts=(item11*70)+(item12*120)+(item13*100)+(item14*90)+(item15*50)

                costoffoodvar.set(str(priceoffood)+' Rs')
                costofdrinksvar.set(str(priceofdrinks) + ' Rs')
                costofdesertsvar.set(str(priceofdesserts) + ' Rs')

                subtotalofItems=priceoffood+priceofdrinks+priceofdesserts
                subtotalvar.set(str(subtotalofItems)+' Rs')

                servicetaxvar.set('50 Rs')

                totalcost=subtotalofItems+50
                totalcostvar.set(str(totalcost)+' Rs')

            else:
                messagebox.showerror('Error','No item is selected')

        def receipt():
            global billnumber,date
            if costoffoodvar.get()!='' or costofdrinksvar.get()!='' or costofdesertsvar.get()!='':
                textreceipt.delete(1.0,END)
                x=random.randint(100,10000)
                billnumber='BILL'+str(x)
                date=time.strftime('%d/%m/%y')
                textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
                textreceipt.insert(END,'*********************************************************\n')
                textreceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')
                textreceipt.insert(END, '*********************************************************\n')
                if e_burger.get()!='0':
                    textreceipt.insert(END,f'Burger\t\t\t{int(e_burger.get())*80}\n\n')
                if e_pizza.get()!='0':
                    textreceipt.insert(END,f'Pizza\t\t\t{int(e_pizza.get())*150}\n\n')
                if e_frenchfries.get()!='0':
                    textreceipt.insert(END,f'French fries\t\t\t{int(e_frenchfries.get())*120}\n\n')
                if e_sandwich.get()!='0':
                    textreceipt.insert(END,f'sandwich\t\t\t{int(e_sandwich.get())*50}\n\n')
                if e_momos.get()!='0':
                    textreceipt.insert(END,f'Momos\t\t\t{int(e_momos.get())*80}\n\n')
                if e_chocolatemilkshake.get()!='0':
                    textreceipt.insert(END,f'Chocolate milkshake\t\t\t{int(e_chocolatemilkshake.get())*90}\n\n')
                if e_mangomilkshake.get()!='0':
                    textreceipt.insert(END,f'Mango milkshake\t\t\t{int(e_mangomilkshake.get())*70}\n\n')
                if e_coffee.get()!='0':
                    textreceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*45}\n\n')
                if e_sprite.get()!='0':
                    textreceipt.insert(END,f'Sprite\t\t\t{int(e_sprite.get())*20}\n\n')
                if e_latte.get()!='0':
                    textreceipt.insert(END,f'Latte\t\t\t{int(e_latte.get())*100}\n\n')
                if e_Hotchocolate.get()!='0':
                    textreceipt.insert(END,f'Hotchocolate\t\t\t{int(e_Hotchocolate.get())*70}\n\n')
                if e_Bwaffle.get()!='0':
                    textreceipt.insert(END,f'Belgian waffle\t\t\t{int(e_Bwaffle.get())*120}\n\n')
                if e_Donuts.get()!='0':
                    textreceipt.insert(END,f'Donuts\t\t\t{int(e_Donuts.get())*100}\n\n')
                if e_cake.get()!='0':
                    textreceipt.insert(END,f'cake\t\t\t{int(e_cake.get())*90}\n\n')
                if e_icecream.get()!='0':
                    textreceipt.insert(END,f'icecream\t\t\t{int(e_icecream.get())*50}\n\n')

                textreceipt.insert(END, '*********************************************************\n')
                if costoffoodvar.get()!='0 Rs':
                    textreceipt.insert(END, f'Cost of Food\t\t\t{priceoffood}Rs\n\n')
                if costofdrinksvar.get() != '0 Rs':
                    textreceipt.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}Rs\n\n')
                if costofdesertsvar.get() != '0 Rs':
                    textreceipt.insert(END, f'Cost of Desserts\t\t\t{priceofdesserts}Rs\n\n')
                textreceipt.insert(END, '*********************************************************\n')

            else:
                messagebox.showerror('Error','No item selected')

        def save():
            if textreceipt.get(1.0,END)=='\n':
                pass
            else:
                url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',parent=self.root)
                if url==None:
                    pass
                else:
                    bill_data=textreceipt.get(1.0,END)
                    url.write(bill_data)
                    url.close()
                    messagebox.showinfo('Information','Your Bill is saved successfully',parent=self.root)

        def reset():
            textreceipt.delete(1.0,END)
            e_burger.set('0')
            e_pizza.set("0")
            e_frenchfries.set("0")
            e_sandwich.set("0")
            e_momos.set("0")
            e_chocolatemilkshake.set("0")
            e_mangomilkshake.set("0")
            e_coffee.set("0")
            e_sprite.set("0")
            e_latte.set("0")
            e_Hotchocolate.set("0")
            e_Bwaffle.set("0")
            e_Donuts.set("0")
            e_cake.set("0")
            e_icecream.set("0")

            textburger.config(state=DISABLED)
            textpizza.config(state=DISABLED)
            textfrenchfries.config(state=DISABLED)
            textsandwich.config(state=DISABLED)
            textmomos.config(state=DISABLED)
            textchocolatemilkshake.config(state=DISABLED)
            textmangomilkshake.config(state=DISABLED)
            textcoffee.config(state=DISABLED)
            textsprite.config(state=DISABLED)
            textlatte.config(state=DISABLED)
            textHotchocolate.config(state=DISABLED)
            textBwaffle.config(state=DISABLED)
            textDonuts.config(state=DISABLED)
            textcake.config(state=DISABLED)
            texticecream.config(state=DISABLED)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)

            costoffoodvar.set('')
            costofdrinksvar.set('')
            costofdesertsvar.set('')
            subtotalvar.set('')
            servicetaxvar.set('')
            totalcostvar.set('')


        # =============Food================

        burger = Checkbutton(foodframe, text="Burger", font=("ARIAL", 18, "bold"), onvalue=1, offvalue=0, variable=var1,command=changeburgerstate)
        burger.grid(row=0, column=0,sticky=W)

        pizza = Checkbutton(foodframe, text="Pizza", font=("ARIAL", 18, "bold"), onvalue=1, offvalue=0, variable=var2,command=changepizzastate)
        pizza.grid(row=1, column=0,sticky=W)

        frenchfries = Checkbutton(foodframe, text="Frenchfries", font=("ARIAL", 18, "bold"), onvalue=1, offvalue=0,variable=var3,command=changefrenchfriesstate)
        frenchfries.grid(row=2, column=0,sticky=W)

        sandwich = Checkbutton(foodframe, text="sandwich", font=("ARIAL", 18, "bold"), onvalue=1, offvalue=0,variable=var4,command=changesandwichstate)
        sandwich.grid(row=3, column=0,sticky=W)

        momos = Checkbutton(foodframe, text="Momos", font=("ARIAL", 18, "bold"), onvalue=1, offvalue=0, variable=var5,command=changemomosstate)
        momos.grid(row=4, column=0,sticky=W)



        #========================food entry===============================
        textburger=Entry(foodframe,font=("Arial",18,"bold"), bd=7,width=6,state=DISABLED,textvariable=e_burger)
        textburger.grid(row=0,column=1)

        textpizza = Entry(foodframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_pizza)
        textpizza.grid(row=1, column=1)

        textfrenchfries = Entry(foodframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_frenchfries)
        textfrenchfries.grid(row=2, column=1)

        textsandwich = Entry(foodframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_sandwich)
        textsandwich.grid(row=3, column=1)

        textmomos = Entry(foodframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_momos)
        textmomos.grid(row=4, column=1)

        # ==========================Drinks===================================

        chocolatemilkshake = Checkbutton(drinksframe, text="Chocolate Milkshake", font=("ARIAL", 18, "bold"), onvalue=1,
                                         offvalue=0, variable=var6,command=changechocolatemilkshakestate)
        chocolatemilkshake.grid(row=0, column=1,sticky=W)

        mangomilkshake = Checkbutton(drinksframe, text="Mango Milkshake", font=("ARIAL", 18, "bold"), onvalue=1,
                                     offvalue=0, variable=var7,command=changemangomilkshakestate)
        mangomilkshake.grid(row=1, column=1,sticky=W)

        coffee = Checkbutton(drinksframe, text="Coffee", font=("ARIAL", 18, "bold"), onvalue=1,
                             offvalue=0, variable=var8,command=changecoffeestate)
        coffee.grid(row=2, column=1,sticky=W)

        sprite = Checkbutton(drinksframe, text="Sprite", font=("ARIAL", 18, "bold"), onvalue=1,
                             offvalue=0, variable=var9,command=changespritestate)
        sprite.grid(row=3, column=1,sticky=W)

        latte = Checkbutton(drinksframe, text="Latte", font=("ARIAL", 18, "bold"), onvalue=1,
                            offvalue=0, variable=var10,command=changelattestate)
        latte.grid(row=4, column=1,sticky=W)



        #============================Drinks Entry==========================

        textchocolatemilkshake = Entry(drinksframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_chocolatemilkshake)
        textchocolatemilkshake.grid(row=0, column=2)

        textmangomilkshake = Entry(drinksframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_mangomilkshake)
        textmangomilkshake.grid(row=1, column=2)

        textcoffee = Entry(drinksframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                                textvariable=e_coffee)
        textcoffee.grid(row=2, column=2)

        textsprite = Entry(drinksframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                             textvariable=e_sprite)
        textsprite.grid(row=3, column=2)

        textlatte = Entry(drinksframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_latte)
        textlatte.grid(row=4, column=2)

        #==========================Desserts Entry==========================



        textHotchocolate = Entry(desertsframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Hotchocolate)
        textHotchocolate.grid(row=0, column=3)

        textBwaffle = Entry(desertsframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Bwaffle)
        textBwaffle.grid(row=1, column=3)

        textDonuts = Entry(desertsframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                                textvariable=e_Donuts)
        textDonuts.grid(row=2, column=3)

        textcake = Entry(desertsframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                             textvariable=e_cake)
        textcake.grid(row=3, column=3)

        texticecream = Entry(desertsframe, font=("Arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_icecream)
        texticecream.grid(row=4, column=3)




        # ============================Deserts==============================

        Hotchocolate = Checkbutton(desertsframe, text="Hot Chocolate", font=("ARIAL", 18, "bold"), onvalue=1,
                                   offvalue=0, variable=var11,command=changeHotchocolatestate)
        Hotchocolate.grid(row=0, column=2,sticky=W)

        Bwaffle = Checkbutton(desertsframe, text="Belgian Waffle", font=("ARIAL", 18, "bold"), onvalue=1,
                              offvalue=0, variable=var12,command=changeBwafflestate)
        Bwaffle.grid(row=1, column=2,sticky=W)

        Donuts = Checkbutton(desertsframe, text="Donuts", font=("ARIAL", 18, "bold"), onvalue=1,
                             offvalue=0, variable=var13,command=changeDonutsstate)
        Donuts.grid(row=2, column=2,sticky=W)

        Cake = Checkbutton(desertsframe, text="Cake", font=("ARIAL", 18, "bold"), onvalue=1,
                           offvalue=0, variable=var14,command=changeCakestate)
        Cake.grid(row=3, column=2,sticky=W)

        icecream = Checkbutton(desertsframe, text="Icecream", font=("ARIAL", 18, "bold"), onvalue=1,
                               offvalue=0, variable=var15,command=changeicecreamstate)
        icecream.grid(row=4, column=2,sticky=W)


        #=================costlabels & entry fields=============================
        labelcostoffood=Label(costframe,text='cost of Foods',font=("ARIAL",16,"bold"))
        labelcostoffood.grid(row=0,column=0)

        textcostoffood=Entry(costframe,font=("Arial",16,"bold"),state="readonly",bd=6,width=14,textvariable=costoffoodvar)
        textcostoffood.grid(row=0,column=1,padx=41)

        labelcostofdrinks = Label(costframe, text='cost of Drinks', font=("ARIAL", 16, "bold"))
        labelcostofdrinks.grid(row=1, column=0)

        textcostofdrinks = Entry(costframe, font=("Arial", 16, "bold"),state="readonly",bd=6, width=14,textvariable=costofdrinksvar)
        textcostofdrinks.grid(row=1, column=1,padx=41)

        labelcostodeserts = Label(costframe, text='cost of Deserts', font=("ARIAL", 16, "bold"))
        labelcostodeserts.grid(row=2, column=0)

        textcostodeserts = Entry(costframe, font=("Arial", 16, "bold"),state="readonly",bd=6, width=14,textvariable=costofdesertsvar)
        textcostodeserts.grid(row=2, column=1,padx=41)

        labelsubtotal = Label(costframe, text='Sub Total', font=("ARIAL", 16, "bold"))
        labelsubtotal.grid(row=0, column=2)

        textsubtotal = Entry(costframe, font=("Arial", 16, "bold"),state="readonly",bd=6, width=14,textvariable=subtotalvar)
        textsubtotal.grid(row=0, column=3,padx=41)

        labelservicetax = Label(costframe, text='Service Tax', font=("ARIAL", 16, "bold"))
        labelservicetax.grid(row=1, column=2)

        textservicetax = Entry(costframe, font=("Arial", 16, "bold"),state="readonly",bd=6, width=14,textvariable=servicetaxvar)
        textservicetax.grid(row=1, column=3,padx=41)

        labeltotalcost = Label(costframe, text='Total cost', font=("ARIAL", 16, "bold"))
        labeltotalcost.grid(row=2, column=2)

        texttotalcost = Entry(costframe, font=("Arial", 16, "bold"),state="readonly",bd=6, width=14,textvariable=totalcostvar)
        texttotalcost.grid(row=2, column=3,padx=41)

        #=============================Buttons===============================

        buttontotal=Button(buttonframe,text="Total",font=('arial',14,"bold"),fg="sienna",bg="chocolate",bd=3,padx=5,command=totalcost)
        buttontotal.grid(row=0,column=0)

        buttonreceipt= Button(buttonframe, text="Receipt", font=('arial', 14, "bold"), fg="sienna", bg="chocolate", bd=3,padx=5,command=receipt)
        buttonreceipt.grid(row=0, column=1)

        buttonsave = Button(buttonframe, text="save", font=('arial', 14, "bold"), fg="sienna", bg="chocolate", bd=3,padx=5,command=save)
        buttonsave.grid(row=0, column=2)

        buttonreset = Button(buttonframe, text="Reset", font=('arial', 14, "bold"), fg="sienna", bg="chocolate", bd=3,padx=5,command=reset)
        buttonreset.grid(row=0, column=3)

        #========================text area for receipt=============================

        textreceipt=Text(receiptframe,font=("arial",12,"bold"),bd=3,width=42,height=14)
        textreceipt.grid(row=0,column=0)



if __name__ == "__main__":
    main()









