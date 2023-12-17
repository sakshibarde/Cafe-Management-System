import random
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector


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




if __name__ == '__main__':
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
