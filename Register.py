from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:

    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===================variables=======================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
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

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=350, y=150)
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=350, y=180, width=250)

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

        pswd = Label(frame, text="Passward", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=290)
        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=320, width=250)

        confirm_pswd = Label(frame, text="Confirm Passward", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=350, y=290)
        self.confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.confirm_pswd.place(x=350, y=320, width=250)

        # ==================register & login btn======================

        registerbtn = Button(frame,command=self.register_data, text="Register", font=("times new roman", 15, "bold"), borderwidth=0,bd=3, relief=RIDGE, fg="white", bg="darkgreen", activeforeground="white",activebackground="black")
        registerbtn.place(x=280, y=380, width=120,height=30)

        loginbtn = Button(frame, text="Login Now", font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white", bg="darkblue", activeforeground="white", activebackground="black")
        loginbtn.place(x=520, y=420, width=120, height=30)

    # =======================function declaration===================
    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Passward & confirm Passward must be same")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="2004",database="register")
                my_cursor=conn.cursor()
                query=("select * from data where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists,please try another email")
                else: my_cursor.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_fname.get(),
                                                                                                            self.var_lname.get(),
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_securityQ.get(),
                                                                                                            self.var_securityA.get(),
                                                                                                            self.var_pass.get(),
                                                                                                            self.var_email.get()
                                                                                                           ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")

if __name__ == '__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()