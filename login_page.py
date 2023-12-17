from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\hp\Documents\Cafe Management Project\login_background.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550, height=800)

        frame = Frame(self.root, bg="black")
        frame.place(x=460, y=170, width=540, height=350)

        # ===============label========================
        username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=100)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=200, y=100)

        passward = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        passward.place(x=70, y=150)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=200, y=150)

        # ===========login btn=====================
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=230, y=200, width=120, height=35)

        # ==============register btn==================
        registerbtn = Button(frame, text="New User? Register", command=self.register_window,
                             font=("times new roman", 10, "bold"), borderwidth=0, bd=3, relief=RIDGE, fg="white",
                             bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=210, y=280, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "mini" and self.txtpass.get() == "project":
            messagebox.showinfo("Success", "Welcome!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="2004", database="register")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from my_data where username=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid Username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = CafeManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()



if __name__ == '__main__':
    root=Tk()
    app=Login_Window(root)
    root.mainloop()