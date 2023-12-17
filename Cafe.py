
from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win
from orders import Order_win


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



        logout_btn=Button(btn_frame,text="LOGOUT",width=40,font=("times new roman", 16, "bold"), bg="SandyBrown",fg="Sienna",bd=1,cursor="hand1")
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




        




        


if __name__ == "__main__":
    root=Tk()
    obj=CafeManagementSystem(root)
    root.mainloop()
