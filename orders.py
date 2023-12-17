import time
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import random



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
                url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
                if url==None:
                    pass
                else:
                    bill_data=textreceipt.get(1.0,END)
                    url.write(bill_data)
                    url.close()
                    messagebox.showinfo('Information','Your Bill is saved successfully')

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


if __name__ == '__main__':
    root = Tk()
    obj = Order_win(root)
    root.config(bg="brown")
    root.mainloop()
