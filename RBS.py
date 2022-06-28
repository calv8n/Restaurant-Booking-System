from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector as my
import os
global a,b,r1

a=""
b=""
r1=open("Recipt.txt","a+")
def indian():
    window = Toplevel(root1)
    window.title('INDIAN CUISINE')
    #window.geometry("675x500")
    #ind = Frame(window,width=335,height=570)
    frame = Frame(window, bg="dark slate blue")
    frame.grid()
    global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10,spin11,spin12,spin13,spin14
    global spn1,spn2,spn3,spn4,spn5,spn6,spn7,spn8,spn9,spn10,spn11,spn12,spn13,spn14
    global spinn1,spinn2,spinn3,spinn4,spinn5,spinn6,spinn7,spinn8,spinn9,spinn10,spinn11,spinn12,spinn13,spinn14
    global sppin1,sppin2,sppin3,sppin4,sppin5,sppin6,sppin7,sppin8,sppin9,sppin10,sppin11,sppin12,sppin13,sppin14
    labl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Trebuchet MS", 25), bg="dark slate blue",
                 fg="springgreen")
    labl1.grid(column=1, columnspan=2)

    labl2 = Label(frame, text="Indian Cuisine", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="goldenrod",
                 padx=20)
    labl2.grid(row=1, column=1, columnspan=2)

    labl3 = Label(frame, text="Items", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl3.grid(row=2)

    labl4 = Label(frame, text="Price(₹)", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl4.grid(row=2, column=1)

    labl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl5.grid(row=2, column=2)

    labl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl6.grid(row=2, column=3)

    category1 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category1.grid(row=3, columnspan=4)

    item1 = Label(frame, text="Veg. Kolhapuri", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item1.grid(row=4, sticky=W)

    item2 = Label(frame, text="Veg. Jaipuri", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item2.grid(row=5, sticky=W)

    item3 = Label(frame, text="Paneer Tikka Masala", fg="springgreen", bg="dark slate blue",
                  font=("Trebuchet MS", 12))
    item3.grid(row=6, sticky=W)

    item4 = Label(frame, text="Veg. Malai Kofta", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item4.grid(row=7, sticky=W)

    item5 = Label(frame, text="Veg. Palak Paneer", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item5.grid(row=8, sticky=W)

    item6 = Label(frame, text="Mix Vegetable", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item6.grid(row=9, sticky=W)

    Label(frame, text="Spl. Chicken Curry", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, sticky=W)
	
    Label(frame, text="Spl. Fish Fry (2 pcs)", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, sticky=W)
	
    Label(frame, text="Spl. Fish Curry", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, sticky=W)
	
    Label(frame, text="Spl. Mutton Korma", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, sticky=W)
	
    price1 = Label(frame, text="180.00", pady=5, fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price1.grid(row=4, column=1)

    price2 = Label(frame, text="180.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price2.grid(row=5, column=1)

    price3 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price3.grid(row=6, column=1)

    price4 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price4.grid(row=7, column=1)

    price5 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price5.grid(row=8, column=1)

    price6 = Label(frame, text="220.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price6.grid(row=9, column=1)

    Label(frame, text="240.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, column=1)

    Label(frame, text="290.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, column=1)
	
    spin1 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check1)
    spin1.grid(row=4, column=3)

    spin2 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check2)
    spin2.grid(row=5, column=3)

    spin3 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check3)
    spin3.grid(row=6, column=3)

    spin4 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check4)
    spin4.grid(row=7, column=3)

    spin5 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check5)
    spin5.grid(row=8, column=3)

    spin6 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check6)
    spin6.grid(row=9, column=3)
	
    spin7 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check7)
    spin7.grid(row=10, column=3)

    spin8 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check8)
    spin8.grid(row=11, column=3)

    spin9 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check9)
    spin9.grid(row=12, column=3)

    spin10 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check10)
    spin10.grid(row=13, column=3)

    check1 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var1)
    check1.grid(row=4, column=2)

    check2 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var2)
    check2.grid(row=5, column=2)

    check3 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var3)
    check3.grid(row=6, column=2)

    check4 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var4)
    check4.grid(row=7, column=2)

    check5 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var5)
    check5.grid(row=8, column=2)

    check6 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var6)
    check6.grid(row=9, column=2)
	
    check7 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var7)
    check7.grid(row=10, column=2)

    check8 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var8)
    check8.grid(row=11, column=2)

    check9 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var9)
    check9.grid(row=12, column=2)

    check10 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var10)
    check10.grid(row=13, column=2)

    category2 = Label(frame, text="TANDOOR", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category2.grid(row=14, columnspan=4)

    item7 = Label(frame, text="Roti", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item7.grid(row=15, sticky=W)

    item8 = Label(frame, text="Butter Roti", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item8.grid(row=16, sticky=W)

    item9 = Label(frame, text="Butter Naan", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item9.grid(row=17, sticky=W)

    item10 = Label(frame, text="Butter Kulcha", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item10.grid(row=18, sticky=W)

    price7 = Label(frame, text="30.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price7.grid(row=15, column=1)

    price8 = Label(frame, text="40.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price8.grid(row=16, column=1)

    price9 = Label(frame, text="45.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price9.grid(row=17, column=1)

    price10 = Label(frame, text="55.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price10.grid(row=18, column=1)

    spin11 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check11)
    spin11.grid(row=15, column=3)

    spin12 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check12)
    spin12.grid(row=16, column=3)

    spin13 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check13)
    spin13.grid(row=17, column=3)

    spin14 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check14)
    spin14.grid(row=18, column=3)

    check11 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var11)
    check11.grid(row=15, column=2)

    check12 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var12)
    check12.grid(row=16, column=2)

    check13 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var13)
    check13.grid(row=17, column=2)

    check14 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                          selectcolor="springgreen", variable=var14)
    check14.grid(row=18, column=2)
	
    def hide():
	    window.withdraw()
    btn1 = Button(frame, bg="dark slate blue", command=hide, padx=5, fg="springgreen", activebackground="springgreen",font=("Trebuchet MS", 12),activeforeground="goldenrod", text="PROCEED").grid(row=19, columnspan=4)
    labltp = Label(frame, text="", bg="dark slate blue").grid(row=20, columnspan=4)
    frame.pack()

def chinese():
    window = Toplevel(root1)
    window.title('CHINESE CUISINE')
    #window.geometry("675x570")
    #ind = Frame(window,width=335,height=570)
    frame = Frame(window, bg="dark slate blue")
    frame.grid()
    
    global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10,spin11,spin12,spin13,spin14
    global spn1,spn2,spn3,spn4,spn5,spn6,spn7,spn8,spn9,spn10,spn11,spn12,spn13,spn14
    global spinn1,spinn2,spinn3,spinn4,spinn5,spinn6,spinn7,spinn8,spinn9,spinn10,spinn11,spinn12,spinn13,spinn14
    global sppin1,sppin2,sppin3,sppin4,sppin5,sppin6,sppin7,sppin8,sppin9,sppin10,sppin11,sppin12,sppin13,sppin14
    lbl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Trebuchet MS", 25), bg="dark slate blue",
                 fg="springgreen")
    lbl1.grid(column=1, columnspan=2)

    lbl2 = Label(frame, text="Chinese Cuisine", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="goldenrod",
                 padx=20)
    lbl2.grid(row=1, column=1, columnspan=2)

    lbl3 = Label(frame, text="Items", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbl3.grid(row=2)

    lbl4 = Label(frame, text="prc(₹)", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbl4.grid(row=2, column=1)

    lbl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbl5.grid(row=2, column=2)

    lbl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbl6.grid(row=2, column=3)

    category12 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",font=("Trebuchet MS", 15))
    category12.grid(row=3, columnspan=4)

    Label(frame, text="Egg Fried Rice", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=4, sticky=W)

    Label(frame, text="Eight Delicacies Rice ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=5, sticky=W)

    Label(frame, text="Schezwan Fried Rice", fg="springgreen", bg="dark slate blue",font=("Trebuchet MS", 12)).grid(row=6, sticky=W)
   
    Label(frame, text="Fried leek dumplings", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=7, sticky=W)

    Label(frame, text="Steamed dumplings", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=8, sticky=W)

    Label(frame, text="Sliced Noodles", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=9, sticky=W)

    Label(frame, text="Spicy hot Noodles", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, sticky=W)
	
    Label(frame, text="Sesame paste Noodles", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, sticky=W)
	
    Label(frame, text="Eel Noodles", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, sticky=W)
	
    Label(frame, text="Seafood Noodles", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, sticky=W)
	
    prc1 = Label(frame, text="180.00", pady=5, fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc1.grid(row=4, column=1)

    prc2 = Label(frame, text="180.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc2.grid(row=5, column=1)

    prc3 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc3.grid(row=6, column=1)

    prc4 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc4.grid(row=7, column=1)

    prc5 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc5.grid(row=8, column=1)

    prc6 = Label(frame, text="220.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc6.grid(row=9, column=1)

    Label(frame, text="240.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, column=1)

    Label(frame, text="290.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, column=1)
	
    spn1 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check15)
    spn1.grid(row=4, column=3)

    spn2 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check16)
    spn2.grid(row=5, column=3)

    spn3 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check17)
    spn3.grid(row=6, column=3)

    spn4 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check18)
    spn4.grid(row=7, column=3)

    spn5 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check19)
    spn5.grid(row=8, column=3)

    spn6 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check20)
    spn6.grid(row=9, column=3)
	
    spn7 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check21)
    spn7.grid(row=10, column=3)

    spn8 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check22)
    spn8.grid(row=11, column=3)

    spn9 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check23)
    spn9.grid(row=12, column=3)

    spn10 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check24)
    spn10.grid(row=13, column=3)

    chck1 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var15)
    chck1.grid(row=4, column=2)

    chck2 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var16)
    chck2.grid(row=5, column=2)

    chck3 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var17)
    chck3.grid(row=6, column=2)

    chck4 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var18)
    chck4.grid(row=7, column=2)

    chck5 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var19)
    chck5.grid(row=8, column=2)

    chck6 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var20)
    chck6.grid(row=9, column=2)
	
    chck7 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var21)
    chck7.grid(row=10, column=2)

    chck8 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var22)
    chck8.grid(row=11, column=2)

    chck9 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var23)
    chck9.grid(row=12, column=2)

    chck10 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var24)
    chck10.grid(row=13, column=2)

    category2 = Label(frame, text="Soups and Serves", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category2.grid(row=14, columnspan=4)

    Label(frame, text="Fish ball Soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=15, sticky=W)

    Label(frame, text="Egg & Vegetable Soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=16, sticky=W)

    Label(frame, text="Meat ball soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=17, sticky=W)

    Label(frame, text="Oyster Soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=18, sticky=W)

    prc7 = Label(frame, text="30.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc7.grid(row=15, column=1)

    prc8 = Label(frame, text="40.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc8.grid(row=16, column=1)

    prc9 = Label(frame, text="45.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc9.grid(row=17, column=1)

    prc10 = Label(frame, text="55.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    prc10.grid(row=18, column=1)

    spn11 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check25)
    spn11.grid(row=15, column=3)

    spn12 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check26)
    spn12.grid(row=16, column=3)

    spn13 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check27)
    spn13.grid(row=17, column=3)

    spn14 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check28)
    spn14.grid(row=18, column=3)

    chck11 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var25)
    chck11.grid(row=15, column=2)

    chck12 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var26)
    chck12.grid(row=16, column=2)

    chck13 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var27)
    chck13.grid(row=17, column=2)

    chck14 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value1, pady=5, highlightcolor="goldenrod",
                          selectcolor="springgreen", variable=var28)
    chck14.grid(row=18, column=2)
	
    def hide():
	    window.withdraw()
    btn1 = Button(frame, bg="dark slate blue", command=hide, padx=5, fg="springgreen", activebackground="springgreen",font=("Trebuchet MS", 12),activeforeground="goldenrod", text="PROCEED").grid(row=19, columnspan=4)
    lbltp = Label(frame, text="", bg="dark slate blue").grid(row=20, columnspan=4)
    frame.pack()

def italian():
    window = Toplevel(root1)
    window.title('ITALIAN CUISINE')
    #window.geometry("675x570")
    #ind = Frame(window,width=335,height=570)
    frame = Frame(window, bg="dark slate blue")
    frame.grid()
    #global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10,spin11,spin12,spin13,spin14
    #global spn1,spn2,spn3,spn4,spn5,spn6,spn7,spn8,spn9,spn10,spn11,spn12,spn13,spn14
    global spinn1,spinn2,spinn3,spinn4,spinn5,spinn6,spinn7,spinn8,spinn9,spinn10,spinn11,spinn12,spinn13,spinn14
    #global sppin1,sppin2,sppin3,sppin4,sppin5,sppin6,sppin7,sppin8,sppin9,sppin10,sppin11,sppin12,sppin13,sppin14
    lbbl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Trebuchet MS", 25), bg="dark slate blue",
                 fg="springgreen")
    lbbl1.grid(column=1, columnspan=2)

    lbbl2 = Label(frame, text="Italian Cuisine", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="goldenrod",
                 padx=20)
    lbbl2.grid(row=1, column=1, columnspan=2)

    lbbl3 = Label(frame, text="Items", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbbl3.grid(row=2)

    lbbl4 = Label(frame, text="price(₹)", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbbl4.grid(row=2, column=1)

    lbbl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbbl5.grid(row=2, column=2)

    lbbl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    lbbl6.grid(row=2, column=3)

    category12 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",font=("Trebuchet MS", 15))
    category12.grid(row=3, columnspan=4)

    Label(frame, text="Mushroom-Sausage Ragù", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=4, sticky=W)

    Label(frame, text="Three-Cheese Lasagna", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=5, sticky=W)

    Label(frame, text="Grilled Fish", fg="springgreen", bg="dark slate blue",font=("Trebuchet MS", 12)).grid(row=6, sticky=W)
   
    Label(frame, text="Beef Brasato", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=7, sticky=W)

    Label(frame, text="Risotto", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=8, sticky=W)

    Label(frame, text="Swordfish Sicilian-Style", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=9, sticky=W)

    Label(frame, text="Braised Chicken", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, sticky=W)
	
    Label(frame, text="Mushroom Lasagna", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, sticky=W)
	
    Label(frame, text="Italian Meatballs ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, sticky=W)
	
    Label(frame, text=" Farro Soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, sticky=W)
	
    pric1 = Label(frame, text="180.00", pady=5, fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric1.grid(row=4, column=1)

    pric2 = Label(frame, text="180.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric2.grid(row=5, column=1)

    pric3 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric3.grid(row=6, column=1)

    pric4 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric4.grid(row=7, column=1)

    pric5 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric5.grid(row=8, column=1)

    pric6 = Label(frame, text="220.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric6.grid(row=9, column=1)

    Label(frame, text="240.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, column=1)

    Label(frame, text="290.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, column=1)
	
    spinn1 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk1)
    spinn1.grid(row=4, column=3)

    spinn2 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk2)
    spinn2.grid(row=5, column=3)

    spinn3 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk3)
    spinn3.grid(row=6, column=3)

    spinn4 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk4)
    spinn4.grid(row=7, column=3)

    spinn5 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk5)
    spinn5.grid(row=8, column=3)

    spinn6 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk6)
    spinn6.grid(row=9, column=3)
	
    spinn7 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk7)
    spinn7.grid(row=10, column=3)

    spinn8 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk8)
    spinn8.grid(row=11, column=3)

    spinn9 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk9)
    spinn9.grid(row=12, column=3)

    spinn10 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk10)
    spinn10.grid(row=13, column=3)

    chhk1 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr1)
    chhk1.grid(row=4, column=2)

    chhk2 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr2)
    chhk2.grid(row=5, column=2)

    chhk3 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr3)
    chhk3.grid(row=6, column=2)

    chhk4 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr4)
    chhk4.grid(row=7, column=2)

    chhk5 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr5)
    chhk5.grid(row=8, column=2)

    chhk6 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr6)
    chhk6.grid(row=9, column=2)
	
    chhk7 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr7)
    chhk7.grid(row=10, column=2)

    chhk8 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr8)
    chhk8.grid(row=11, column=2)

    chhk9 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr9)
    chhk9.grid(row=12, column=2)

    chhk10 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr10)
    chhk10.grid(row=13, column=2)

    category2 = Label(frame, text="Soups and Serves", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category2.grid(row=14, columnspan=4)

    Label(frame, text="POMODORI FRITTI", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=15, sticky=W)

    Label(frame, text="INSALATA MISTA", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=16, sticky=W)

    Label(frame, text="INSALATA VERDE", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=17, sticky=W)

    Label(frame, text="INSALATA DI POMODORI", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=18, sticky=W)

    pric7 = Label(frame, text="30.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric7.grid(row=15, column=1)

    pric8 = Label(frame, text="40.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric8.grid(row=16, column=1)

    pric9 = Label(frame, text="45.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric9.grid(row=17, column=1)

    pric10 = Label(frame, text="55.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    pric10.grid(row=18, column=1)

    spinn11 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk11)
    spinn11.grid(row=15, column=3)

    spinn12 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk12)
    spinn12.grid(row=16, column=3)

    spinn13 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk13)
    spinn13.grid(row=17, column=3)

    spinn14 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk14)
    spinn14.grid(row=18, column=3)

    chhk11 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr11)
    chhk11.grid(row=15, column=2)

    chhk12 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr12)
    chhk12.grid(row=16, column=2)

    chhk13 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr13)
    chhk13.grid(row=17, column=2)

    chhk14 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value2, pady=5, highlightcolor="goldenrod",
                          selectcolor="springgreen", variable=varr14)
    chhk14.grid(row=18, column=2)
	
    def hide():
	    window.withdraw()
    btn1 = Button(frame, bg="dark slate blue", command=hide, padx=5, fg="springgreen", activebackground="springgreen",font=("Trebuchet MS", 12),activeforeground="goldenrod", text="PROCEED").grid(row=19, columnspan=4)
    lbbltp = Label(frame, text="", bg="dark slate blue").grid(row=20, columnspan=4)
    frame.pack()

def mediterranean():
    window = Toplevel(root1)
    window.title('MEDITERRANEAN CUISINE')
    #window.geometry("675x570")
    #ind = Frame(window,width=335,height=570)
    frame = Frame(window, bg="dark slate blue")
    frame.grid()
    global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10,spin11,spin12,spin13,spin14
    global spn1,spn2,spn3,spn4,spn5,spn6,spn7,spn8,spn9,spn10,spn11,spn12,spn13,spn14
    global spinn1,spinn2,spinn3,spinn4,spinn5,spinn6,spinn7,spinn8,spinn9,spinn10,spinn11,spinn12,spinn13,spinn14
    global sppin1,sppin2,sppin3,sppin4,sppin5,sppin6,sppin7,sppin8,sppin9,sppin10,sppin11,sppin12,sppin13,sppin14
    llbl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Trebuchet MS", 25), bg="dark slate blue",
                 fg="springgreen")
    llbl1.grid(column=1, columnspan=2)

    llbl2 = Label(frame, text="Mediterranean Cuisine", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="goldenrod",
                 padx=20)
    llbl2.grid(row=1, column=1, columnspan=2)

    llbl3 = Label(frame, text="Items", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    llbl3.grid(row=2)

    llbl4 = Label(frame, text="ppric(₹)", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    llbl4.grid(row=2, column=1)

    llbl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    llbl5.grid(row=2, column=2)

    llbl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    llbl6.grid(row=2, column=3)

    category12 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",font=("Trebuchet MS", 15))
    category12.grid(row=3, columnspan=4)

    Label(frame, text="Chicken Medallions ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=4, sticky=W)

    Label(frame, text="Mediterranean Lettuce Wraps ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=5, sticky=W)

    Label(frame, text="Lemon Greek Chicken", fg="springgreen", bg="dark slate blue",font=("Trebuchet MS", 12)).grid(row=6, sticky=W)
   
    Label(frame, text="Mediterranean Hummus Pizza", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=7, sticky=W)

    Label(frame, text="Red Pepper Pizza", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=8, sticky=W)

    Label(frame, text="Chicken & Orzo Soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=9, sticky=W)

    Label(frame, text="Greek Lemon Chicken Soup", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, sticky=W)
	
    Label(frame, text="Griddled chicken", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, sticky=W)
	
    Label(frame, text="chicken tray bake ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, sticky=W)
	
    Label(frame, text="Crunchy baked mussels ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, sticky=W)
	
    ppric1 = Label(frame, text="180.00", pady=5, fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric1.grid(row=4, column=1)

    ppric2 = Label(frame, text="180.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric2.grid(row=5, column=1)

    ppric3 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric3.grid(row=6, column=1)

    ppric4 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric4.grid(row=7, column=1)

    ppric5 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric5.grid(row=8, column=1)

    ppric6 = Label(frame, text="220.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric6.grid(row=9, column=1)

    Label(frame, text="240.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, column=1)

    Label(frame, text="290.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, column=1)
	
    sppin1 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk15)
    sppin1.grid(row=4, column=3)

    sppin2 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk16)
    sppin2.grid(row=5, column=3)

    sppin3 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk17)
    sppin3.grid(row=6, column=3)

    sppin4 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk18)
    sppin4.grid(row=7, column=3)

    sppin5 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk19)
    sppin5.grid(row=8, column=3)

    sppin6 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk20)
    sppin6.grid(row=9, column=3)
	
    sppin7 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk21)
    sppin7.grid(row=10, column=3)

    sppin8 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk22)
    sppin8.grid(row=11, column=3)

    sppin9 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk23)
    sppin9.grid(row=12, column=3)

    sppin10 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk24)
    sppin10.grid(row=13, column=3)

    chkk1 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr15)
    chkk1.grid(row=4, column=2)

    chkk2 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr16)
    chkk2.grid(row=5, column=2)

    chkk3 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr17)
    chkk3.grid(row=6, column=2)

    chkk4 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr18)
    chkk4.grid(row=7, column=2)

    chkk5 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr19)
    chkk5.grid(row=8, column=2)

    chkk6 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr20)
    chkk6.grid(row=9, column=2)
	
    chkk7 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr21)
    chkk7.grid(row=10, column=2)

    chkk8 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr22)
    chkk8.grid(row=11, column=2)

    chkk9 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr23)
    chkk9.grid(row=12, column=2)

    chkk10 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr24)
    chkk10.grid(row=13, column=2)

    category2 = Label(frame, text="Soups and Serves", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category2.grid(row=14, columnspan=4)

    Label(frame, text="potato salad ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=15, sticky=W)

    Label(frame, text="summer salad ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=16, sticky=W)

    Label(frame, text="feta cheese toasts ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=17, sticky=W)

    Label(frame, text="mozzarella salad ", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=18, sticky=W)

    ppric7 = Label(frame, text="30.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric7.grid(row=15, column=1)

    ppric8 = Label(frame, text="40.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric8.grid(row=16, column=1)

    ppric9 = Label(frame, text="45.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric9.grid(row=17, column=1)

    ppric10 = Label(frame, text="55.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    ppric10.grid(row=18, column=1)

    sppin11 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk25)
    sppin11.grid(row=15, column=3)

    sppin12 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk26)
    sppin12.grid(row=16, column=3)

    sppin13 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk27)
    sppin13.grid(row=17, column=3)

    sppin14 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_checkk28)
    sppin14.grid(row=18, column=3)

    chkk11 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr25)
    chkk11.grid(row=15, column=2)

    chkk12 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr26)
    chkk12.grid(row=16, column=2)

    chkk13 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=varr27)
    chkk13.grid(row=17, column=2)

    chkk14 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value3, pady=5, highlightcolor="goldenrod",
                          selectcolor="springgreen", variable=varr28)
    chkk14.grid(row=18, column=2)
	
    def hide():
	    window.withdraw()
    btn1 = Button(frame, bg="dark slate blue", command=hide, padx=5, fg="springgreen", activebackground="springgreen",font=("Trebuchet MS", 12),activeforeground="goldenrod", text="PROCEED").grid(row=19, columnspan=4)
    llbltp = Label(frame, text="", bg="dark slate blue").grid(row=20, columnspan=4)
    frame.pack()
	
	
# -----------------creating window---------------
root1 = Tk()
root1.geometry("1350x750")
root1.title("Muffada Allah Halal Kitchen")
root1.configure(background="dark slate blue")

# -----------------creating frames------------------
Tops = Frame(root1, bg="dark slate blue", width=1350, height=75, bd=14)
Tops.pack(side=TOP)
f1 = Frame(root1, bg="dark slate blue", width=900, height=650, bd=8)
f1.pack(side=LEFT)
f2 = Frame(root1, bg="dark slate blue", width=440, height=650, bd=8)
f2.pack(side=RIGHT)

# ------------subpart of the frames---------------
f1a = Frame(f1, bg="dark slate blue", width=900, height=330, bd=8,)
f1a.pack(side=TOP)
f2a = Frame(f1, bg="dark slate blue", width=900, height=320, bd=6)
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, bg="dark slate blue", width=300, height=400, bd=12)
ft2.pack(side=TOP)
fb2 = Frame(f2, bg="dark slate blue", width=440, height=250, bd=16)
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, bg="dark slate blue", width=400, height=330, bd=16)
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, bg="dark slate blue", width=400, height=330, bd=16)
f1ab.pack(side=RIGHT)

f1aaa = Frame(f1aa, width=400, height=165,bg="dark slate blue",  bd=16)
f1aaa.pack(side=TOP)
f1aab = Frame(f1aa, width=400, height=165, bd=16, bg="dark slate blue")
f1aab.pack(side=BOTTOM)
f1aba = Frame(f1ab, width=400, height=165, bd=16, bg="dark slate blue")
f1aba.pack(side=TOP)
f1abb = Frame(f1ab, width=400, height=165, bd=16, bg="dark slate blue")
f1abb.pack(side=BOTTOM)

f2aa = Frame(f2a, width=450, height=330, bg="dark slate blue", bd=14)
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bg="dark slate blue", bd=14)
f2ab.pack(side=RIGHT)

# -----------------setting background color ---------------
#Tops.configure(background='dark slate blue')
#f1.configure(background='dark slate blue')
#f2.configure(background='dark slate blue')

# -------------------creating labels-----------------------
lb1Info = Label(Tops, font=('Trebuchet MS', 45, 'bold'), bg="dark slate blue", fg="goldenrod", text="LUXURY ROYALE", bd=5)
lb1Info.grid()
Label(Tops, text="Deluxe A/C Restaurant (Veg & Non-Veg)", font=("Trebuchet MS", 15), bg="dark slate blue", fg="goldenrod").grid(row=1)
Label(Tops, text="--------------------------------------------------------------------------------------------------------------------------------------------------------", font=("Trebuchet MS", 15), bg="dark slate blue", fg="goldenrod").grid(row=2)
# -------------------for exit button------------------

def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root1.destroy()
        return


# ------------------for reset button------------------

def Reset():
    global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10,spin11,spin12,spin13,spin14
    global spn1,spn2,spn3,spn4,spn5,spn6,spn7,spn8,spn9,spn10,spn11,spn12,spn13,spn14
    global spinn1,spinn2,spinn3,spinn4,spinn5,spinn6,spinn7,spinn8,spinn9,spinn10,spinn11,spinn12,spinn13,spinn14
    global sppin1,sppin2,sppin3,sppin4,sppin5,sppin6,sppin7,sppin8,sppin9,sppin10,sppin11,sppin12,sppin13,sppin14
    txtReceipt.delete("1.0", END)
    COD.set("")
    COC.set("")
    PT.set("")
    SC.set("")
    T.set("")
    ST.set("")
    global a,b
    a=""
    b=""

    E_check1.set("0")
    E_check2.set("0")
    E_check3.set("0")
    E_check4.set("0")
    E_check5.set("0")
    E_check6.set("0")
    E_check7.set("0")
    E_check8.set("0")
    E_check9.set("0")
    E_check10.set("0")
    E_check11.set("0")
    E_check12.set("0")
    E_check13.set("0")
    E_check14.set("0")
    E_check15.set("0")
    E_check16.set("0")
    E_check17.set("0")
    E_check18.set("0")
    E_check19.set("0")
    E_check20.set("0")
    E_check21.set("0")
    E_check22.set("0")
    E_check23.set("0")
    E_check24.set("0")
    E_check25.set("0")
    E_check26.set("0")
    E_check27.set("0")
    E_check28.set("0")
	
    E_checkk1.set("0")
    E_checkk2.set("0")
    E_checkk3.set("0")
    E_checkk4.set("0")
    E_checkk5.set("0")
    E_checkk6.set("0")
    E_checkk7.set("0")
    E_checkk8.set("0")
    E_checkk9.set("0")
    E_checkk10.set("0")
    E_checkk11.set("0")
    E_checkk12.set("0")
    E_checkk13.set("0")
    E_checkk14.set("0")
    E_checkk15.set("0")
    E_checkk16.set("0")
    E_checkk17.set("0")
    E_checkk18.set("0")
    E_checkk19.set("0")
    E_checkk20.set("0")
    E_checkk21.set("0")
    E_checkk22.set("0")
    E_checkk23.set("0")
    E_checkk24.set("0")
    E_checkk25.set("0")
    E_checkk26.set("0")
    E_checkk27.set("0")
    E_checkk28.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    var17.set("0")
    var18.set("0")
    var19.set("0")
    var20.set("0")
    var21.set("0")
    var22.set("0")
    var23.set("0")
    var24.set("0")
    var25.set("0")
    var26.set("0")
    var27.set("0")
    var28.set("0")
	
    varr1.set("0")
    varr2.set("0")
    varr3.set("0")
    varr4.set("0")
    varr5.set("0")
    varr6.set("0")
    varr7.set("0")
    varr8.set("0")
    varr9.set("0")
    varr10.set("0")
    varr11.set("0")
    varr12.set("0")
    varr13.set("0")
    varr14.set("0")
    varr14.set("0")
    varr15.set("0")
    varr16.set("0")
    varr17.set("0")
    varr18.set("0")
    varr19.set("0")
    varr20.set("0")
    varr21.set("0")
    varr22.set("0")
    varr23.set("0")
    varr24.set("0")
    varr25.set("0")
    varr26.set("0")
    varr27.set("0")
    varr28.set("0")


    spin1.configure(state=DISABLED)
    spin2.configure(state=DISABLED)
    spin3.configure(state=DISABLED)
    spin4.configure(state=DISABLED)
    spin5.configure(state=DISABLED)
    spin6.configure(state=DISABLED)
    spin7.configure(state=DISABLED)
    spin8.configure(state=DISABLED)
    spin9.configure(state=DISABLED)
    spin10.configure(state=DISABLED)
    spin11.configure(state=DISABLED)
    spin12.configure(state=DISABLED)
    spin13.configure(state=DISABLED)
    spin14.configure(state=DISABLED)

    spn1.configure(state=DISABLED)
    spn2.configure(state=DISABLED)
    spn3.configure(state=DISABLED)
    spn4.configure(state=DISABLED)
    spn5.configure(state=DISABLED)
    spn6.configure(state=DISABLED)
    spn7.configure(state=DISABLED)
    spn8.configure(state=DISABLED)
    spn9.configure(state=DISABLED)
    spn10.configure(state=DISABLED)
    spn11.configure(state=DISABLED)
    spn12.configure(state=DISABLED)
    spn13.configure(state=DISABLED)
    spn14.configure(state=DISABLED)
	
    sppin1.configure(state=DISABLED)
    sppin2.configure(state=DISABLED)
    sppin3.configure(state=DISABLED)
    sppin4.configure(state=DISABLED)
    sppin5.configure(state=DISABLED)
    sppin6.configure(state=DISABLED)
    sppin7.configure(state=DISABLED)
    sppin8.configure(state=DISABLED)
    sppin9.configure(state=DISABLED)
    sppin10.configure(state=DISABLED)
    sppin11.configure(state=DISABLED)
    sppin12.configure(state=DISABLED)
    sppin13.configure(state=DISABLED)
    sppin14.configure(state=DISABLED)
	
    spinn1.configure(state=DISABLED)
    spinn2.configure(state=DISABLED)
    spinn3.configure(state=DISABLED)
    spinn4.configure(state=DISABLED)
    spinn5.configure(state=DISABLED)
    spinn6.configure(state=DISABLED)
    spinn7.configure(state=DISABLED)
    spinn8.configure(state=DISABLED)
    spinn9.configure(state=DISABLED)
    spinn10.configure(state=DISABLED)
    spinn11.configure(state=DISABLED)
    spinn12.configure(state=DISABLED)
    spinn13.configure(state=DISABLED)
    spinn14.configure(state=DISABLED)
	


# ---------------Checkbutton changes-----------------

def chkbutton_value():
    if (var1.get() == 1):
        spin1.configure(state=NORMAL)
    elif var1.get() == 0:
        spin1.configure(state=DISABLED)
        E_check1.set("0")

    if (var2.get() == 1):
        spin2.configure(state=NORMAL)
    elif var2.get() == 0:
        spin2.configure(state=DISABLED)
        E_check2.set("0")

    if (var3.get() == 1):
        spin3.configure(state=NORMAL)
    elif var3.get() == 0:
        spin3.configure(state=DISABLED)
        E_check3.set("0")

    if (var4.get() == 1):
        spin4.configure(state=NORMAL)
    elif var4.get() == 0:
        spin4.configure(state=DISABLED)
        E_check4.set("0")

    if (var5.get() == 1):
        spin5.configure(state=NORMAL)
    elif var5.get() == 0:
        spin5.configure(state=DISABLED)
        E_check5.set("0")

    if (var6.get() == 1):
        spin6.configure(state=NORMAL)
    elif var6.get() == 0:
        spin6.configure(state=DISABLED)
        E_check6.set("0")

    if (var7.get() == 1):
        spin7.configure(state=NORMAL)
    elif var7.get() == 0:
        spin7.configure(state=DISABLED)
        E_check7.set("0")

    if (var8.get() == 1):
        spin8.configure(state=NORMAL)
    elif var8.get() == 0:
        spin8.configure(state=DISABLED)
        E_check8.set("0")

    if (var9.get() == 1):
        spin9.configure(state=NORMAL)
    elif var9.get() == 0:
        spin9.configure(state=DISABLED)
        E_check9.set("0")

    if (var10.get() == 1):
        spin10.configure(state=NORMAL)
    elif var10.get() == 0:
        spin10.configure(state=DISABLED)
        E_check10.set("0")

    if (var11.get() == 1):
        spin11.configure(state=NORMAL)
    elif var11.get() == 0:
        spin11.configure(state=DISABLED)
        E_check11.set("0")
	
    if (var12.get() == 1):
        spin12.configure(state=NORMAL)
    elif var12.get() == 0:
        spin12.configure(state=DISABLED)
        E_check12.set("0")
		
    if (var13.get() == 1):
        spin13.configure(state=NORMAL)
    elif var13.get() == 0:
        spin13.configure(state=DISABLED)
        E_check13.set("0")
		
    if (var14.get() == 1):
        spin14.configure(state=NORMAL)
    elif var14.get() == 0:
        spin14.configure(state=DISABLED)
        E_check14.set("0")
		
def chkbutton_value1() :
    if (var15.get() == 1):
        spn1.configure(state=NORMAL)
    elif var15.get() == 0:
        spn1.configure(state=DISABLED)
        E_check15.set("0")

    if (var16.get() == 1):
        spn2.configure(state=NORMAL)
    elif var16.get() == 0:
        spn2.configure(state=DISABLED)
        E_check16.set("0")

    if (var17.get() == 1):
        spn3.configure(state=NORMAL)
    elif var17.get() == 0:
        spn3.configure(state=DISABLED)
        E_check17.set("0")

    if (var18.get() == 1):
        spn4.configure(state=NORMAL)
    elif var18.get() == 0:
        spn4.configure(state=DISABLED)
        E_check18.set("0")

    if (var19.get() == 1):
        spn5.configure(state=NORMAL)
    elif var19.get() == 0:
        spn5.configure(state=DISABLED)
        E_check19.set("0")

    if (var20.get() == 1):
        spn6.configure(state=NORMAL)
    elif var20.get() == 0:
        spn6.configure(state=DISABLED)
        E_check20.set("0")

    if (var21.get() == 1):
        spn7.configure(state=NORMAL)
    elif var21.get() == 0:
        spn7.configure(state=DISABLED)
        E_check21.set("0")

    if (var22.get() == 1):
        spn8.configure(state=NORMAL)
    elif var22.get() == 0:
        spn8.configure(state=DISABLED)
        E_check22.set("0")

    if (var23.get() == 1):
        spn9.configure(state=NORMAL)
    elif var23.get() == 0:
        spn9.configure(state=DISABLED)
        E_check23.set("0")

    if (var24.get() == 1):
        spn10.configure(state=NORMAL)
    elif var24.get() == 0:
        spn10.configure(state=DISABLED)
        E_check24.set("0")

    if (var25.get() == 1):
        spn11.configure(state=NORMAL)
    elif var25.get() == 0:
        spn11.configure(state=DISABLED)
        E_check25.set("0")
	
    if (var26.get() == 1):
        spn12.configure(state=NORMAL)
    elif var26.get() == 0:
        spn12.configure(state=DISABLED)
        E_check26.set("0")
		
    if (var27.get() == 1):
        spn13.configure(state=NORMAL)
    elif var27.get() == 0:
        spn13.configure(state=DISABLED)
        E_check27.set("0")
		
    if (var28.get() == 1):
        spn14.configure(state=NORMAL)
    elif var28.get() == 0:
        spn14.configure(state=DISABLED)
        E_check28.set("0")

def chkbutton_value2():
    if (varr1.get() == 1):
        spinn1.configure(state=NORMAL)
    elif varr1.get() == 0:
        spinn1.configure(state=DISABLED)
        E_checkk1.set("0")

    if (varr2.get() == 1):
        spinn2.configure(state=NORMAL)
    elif varr2.get() == 0:
        spinn2.configure(state=DISABLED)
        E_checkk2.set("0")

    if (varr3.get() == 1):
        spinn3.configure(state=NORMAL)
    elif varr3.get() == 0:
        spinn3.configure(state=DISABLED)
        E_checkk3.set("0")

    if (varr4.get() == 1):
        spinn4.configure(state=NORMAL)
    elif varr4.get() == 0:
        spinn4.configure(state=DISABLED)
        E_checkk4.set("0")

    if (varr5.get() == 1):
        spinn5.configure(state=NORMAL)
    elif varr5.get() == 0:
        spinn5.configure(state=DISABLED)
        E_checkk5.set("0")

    if (varr6.get() == 1):
        spinn6.configure(state=NORMAL)
    elif varr6.get() == 0:
        spinn6.configure(state=DISABLED)
        E_checkk6.set("0")

    if (varr7.get() == 1):
        spinn7.configure(state=NORMAL)
    elif varr7.get() == 0:
        spinn7.configure(state=DISABLED)
        E_checkk7.set("0")

    if (varr8.get() == 1):
        spinn8.configure(state=NORMAL)
    elif varr8.get() == 0:
        spinn8.configure(state=DISABLED)
        E_checkk8.set("0")

    if (varr9.get() == 1):
        spinn9.configure(state=NORMAL)
    elif varr9.get() == 0:
        spinn9.configure(state=DISABLED)
        E_checkk9.set("0")

    if (varr10.get() == 1):
        spinn10.configure(state=NORMAL)
    elif varr10.get() == 0:
        spinn10.configure(state=DISABLED)
        E_checkk10.set("0")

    if (varr11.get() == 1):
        spinn11.configure(state=NORMAL)
    elif varr11.get() == 0:
        spinn11.configure(state=DISABLED)
        E_checkk11.set("0")
	
    if (varr12.get() == 1):
        spinn12.configure(state=NORMAL)
    elif varr12.get() == 0:
        spinn12.configure(state=DISABLED)
        E_checkk12.set("0")
		
    if (varr13.get() == 1):
        spinn13.configure(state=NORMAL)
    elif varr13.get() == 0:
        spinn13.configure(state=DISABLED)
        E_checkk13.set("0")
		
    if (varr14.get() == 1):
        spinn14.configure(state=NORMAL)
    elif varr14.get() == 0:
        spinn14.configure(state=DISABLED)
        E_checkk14.set("0")

def chkbutton_value3() :
    if (varr15.get() == 1):
        sppin1.configure(state=NORMAL)
    elif varr15.get() == 0:
        sppin1.configure(state=DISABLED)
        E_checkk15.set("0")

    if (varr16.get() == 1):
        sppin2.configure(state=NORMAL)
    elif varr16.get() == 0:
        sppin2.configure(state=DISABLED)
        E_checkk16.set("0")

    if (varr17.get() == 1):
        sppin3.configure(state=NORMAL)
    elif varr17.get() == 0:
        sppin3.configure(state=DISABLED)
        E_checkk17.set("0")

    if (varr18.get() == 1):
        sppin4.configure(state=NORMAL)
    elif varr18.get() == 0:
        sppin4.configure(state=DISABLED)
        E_checkk18.set("0")

    if (varr19.get() == 1):
        sppin5.configure(state=NORMAL)
    elif varr19.get() == 0:
        sppin5.configure(state=DISABLED)
        E_checkk19.set("0")

    if (varr20.get() == 1):
        sppin6.configure(state=NORMAL)
    elif varr20.get() == 0:
        sppin6.configure(state=DISABLED)
        E_checkk20.set("0")

    if (varr21.get() == 1):
        sppin7.configure(state=NORMAL)
    elif varr21.get() == 0:
        sppin7.configure(state=DISABLED)
        E_checkk21.set("0")

    if (varr22.get() == 1):
        sppin8.configure(state=NORMAL)
    elif varr22.get() == 0:
        sppin8.configure(state=DISABLED)
        E_checkk22.set("0")

    if (varr23.get() == 1):
        sppin9.configure(state=NORMAL)
    elif varr23.get() == 0:
        sppin9.configure(state=DISABLED)
        E_checkk23.set("0")

    if (varr24.get() == 1):
        sppin10.configure(state=NORMAL)
    elif varr24.get() == 0:
        sppin10.configure(state=DISABLED)
        E_checkk24.set("0")

    if (varr25.get() == 1):
        sppin11.configure(state=NORMAL)
    elif varr25.get() == 0:
        sppin11.configure(state=DISABLED)
        E_checkk25.set("0")
	
    if (varr26.get() == 1):
        sppin12.configure(state=NORMAL)
    elif varr26.get() == 0:
        sppin12.configure(state=DISABLED)
        E_checkk26.set("0")
		
    if (varr27.get() == 1):
        sppin13.configure(state=NORMAL)
    elif varr27.get() == 0:
        sppin13.configure(state=DISABLED)
        E_checkk27.set("0")
		
    if (varr28.get() == 1):
        sppin14.configure(state=NORMAL)
    elif varr28.get() == 0:
        sppin14.configure(state=DISABLED)
        E_checkk28.set("0")		
# ----------------for TOTAL button--------------------------
def COI():
    ITEM1 = float(E_check1.get())
    ITEM2 = float(E_check2.get())
    ITEM3 = float(E_check3.get())
    ITEM4 = float(E_check4.get())
    ITEM5 = float(E_check5.get())
    ITEM6 = float(E_check6.get())
    ITEM7 = float(E_check7.get())
    ITEM8 = float(E_check8.get())
    ITEM9 = float(E_check9.get())
    ITEM10 = float(E_check10.get())
    ITEM11 = float(E_check11.get())
    ITEM12 = float(E_check12.get())
    ITEM13 = float(E_check13.get())
    ITEM14 = float(E_check14.get())

    ITEM15 = float(E_check15.get())
    ITEM16 = float(E_check16.get())
    ITEM17 = float(E_check17.get())
    ITEM18 = float(E_check18.get())
    ITEM19 = float(E_check19.get())
    ITEM20 = float(E_check20.get())
    ITEM21 = float(E_check21.get())
    ITEM22 = float(E_check22.get())
    ITEM23 = float(E_check23.get())
    ITEM24 = float(E_check24.get())
    ITEM25 = float(E_check25.get())
    ITEM26 = float(E_check26.get())
    ITEM27 = float(E_check27.get())
    ITEM28 = float(E_check28.get())
	
    ITM1 = float(E_checkk1.get())
    ITM2 = float(E_checkk2.get())
    ITM3 = float(E_checkk3.get())
    ITM4 = float(E_checkk4.get())
    ITM5 = float(E_checkk5.get())
    ITM6 = float(E_checkk6.get())
    ITM7 = float(E_checkk7.get())
    ITM8 = float(E_checkk8.get())
    ITM9 = float(E_checkk9.get())
    ITM10 = float(E_checkk10.get())
    ITM11 = float(E_checkk11.get())
    ITM12 = float(E_checkk12.get())
    ITM13 = float(E_checkk13.get())
    ITM14 = float(E_checkk14.get())

    ITM15 = float(E_checkk15.get())
    ITM16 = float(E_checkk16.get())
    ITM17 = float(E_checkk17.get())
    ITM18 = float(E_checkk18.get())
    ITM19 = float(E_checkk19.get())
    ITM20 = float(E_checkk20.get())
    ITM21 = float(E_checkk21.get())
    ITM22 = float(E_checkk22.get())
    ITM23 = float(E_checkk23.get())
    ITM24 = float(E_checkk24.get())
    ITM25 = float(E_checkk25.get())
    ITM26 = float(E_checkk26.get())
    ITM27 = float(E_checkk27.get())
    ITM28 = float(E_checkk28.get())
    POD = (ITEM1 * 180) + (ITEM2 * 180) + (ITEM3 * 200) + (ITEM4 * 200) + (ITEM5 * 200) + (ITEM6 * 220) + (ITEM7 * 240) + (ITEM8 * 260) + (ITEM9 * 260) + (ITEM10 * 290) + (ITEM11 * 30) + (ITEM12 * 40) + (ITEM13 * 45) + (ITEM14 * 55) + (ITEM15 * 180) + (ITEM16 * 180) + (ITEM17 * 200) + (ITEM18 * 200) + (ITEM19 * 200) + (ITEM20 * 220) + (ITEM21 * 240) + (ITEM22 * 260) + (ITEM23 * 260) + (ITEM24	* 290) + (ITEM25 * 30) + (ITEM26 * 40) + (ITEM27 * 45) + (ITEM28 * 55) + (ITM1 * 180) + (ITM2 * 180) + (ITM3 * 200) + (ITM4 * 200) + (ITM5 * 200) + (ITM6 * 220) + (ITM7 * 240) + (ITM8 * 260) + (ITM9 * 260) + (ITM10 * 290) + (ITM11 * 30) + (ITM12 * 40) + (ITM13 * 45) + (ITM14 * 55) + (ITM15 * 180) + (ITM16 * 180) + (ITM17 * 200) + (ITM18 * 200) + (ITM19 * 200) + (ITM20 * 220) + (ITM21 * 240) + (ITM22 * 260) + (ITM23 * 260) + (ITM24	* 290) + (ITM25 * 30) + (ITM26 * 40) + (ITM27 * 45) + (ITM28 * 55)
    GST = POD * 0.025
    global DP,AA,Tax,TOC
    DP = ["₹", float('%.2f' % (POD))]
    COD.set(DP)
    AA = "₹", float('%.2f' % ((POD ) * (0.025)))
    SC.set(AA)

    Tax = "₹", float('%.2f' % ((POD ) * (0.025)))
    PT.set(Tax)
    EX = POD + 2*(GST)
    TOC = "₹", float('%.2f' % (EX))
    global a
    a=str(EX)
    
    T.set(TOC)
# -------------------for report button--------------------
def Report():
    os.system("python report.py")

# -----------------for receipt button---------------------
def Rcpt():
    
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 5000876)
    randomRef = str(x)
    global b
    b=str(x)
   
    
    Receipt_Ref = StringVar()
    Receipt_Ref.set("BILL " + randomRef)
	
    txtReceipt.insert(END, 'Receipt Ref:\t' + Receipt_Ref.get() + '\t\tDate:' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Items \t\t\t Rate      ' + "Quantity\n")
    if (var1.get() == 1):
        
        txtReceipt.insert(END, 'Veg.Kolhapuri: \t\t\t₹180\t' + E_check1.get() + "\n")
        
    if (var2.get() == 1):
        txtReceipt.insert(END, 'Veg.Jaipuri \t\t\t₹180\t' + E_check2.get() + "\n")
    if (var3.get() == 1):
        txtReceipt.insert(END, 'Paneer Tikka Masala: \t\t\t₹200\t' + E_check3.get() + "\n")
    if (var4.get() == 1):
        txtReceipt.insert(END, 'Malai Kofta: \t\t\t₹200\t' + E_check4.get() + "\n")
    if (var5.get() == 1):
        txtReceipt.insert(END, 'Palak Paneer: \t\t\t₹200\t' + E_check5.get() + "\n")
    if (var6.get() == 1):
        txtReceipt.insert(END, 'Mix Vegetable: \t\t\t₹220\t' + E_check6.get() + "\n")
    if (var7.get() == 1):
        txtReceipt.insert(END, 'Spl. Chicken Curry: \t\t\t₹240\t' + E_check7.get() + "\n")
    if (var8.get() == 1):
        txtReceipt.insert(END, 'Spl. Fish Fry (2 pcs): \t\t\t₹260\t' + E_check8.get() + "\n")
    if (var9.get() == 1):
        txtReceipt.insert(END, 'Spl. Fish Curry: \t\t\t₹260\t' + E_check9.get() + "\n")
    if (var10.get() == 1):
        txtReceipt.insert(END, 'Spl. Mutton Korma: \t\t\t₹290\t' + E_check10.get() + "\n")
    if (var11.get() == 1):
        txtReceipt.insert(END, 'Roti: \t\t\t₹30\t' + E_check11.get() + "\n")
    if (var12.get() == 1):
        txtReceipt.insert(END, 'Butter Roti: \t\t\t₹40\t' + E_check12.get() + "\n")
    if (var13.get() == 1):
        txtReceipt.insert(END, 'Butter Naan: \t\t\t₹45\t' + E_check13.get() + "\n")
    if (var14.get() == 1):
        txtReceipt.insert(END, 'Butter Kulcha: \t\t\t₹55\t' + E_check14.get() + "\n")

    if (var15.get() == 1):
        txtReceipt.insert(END, 'Egg Fried Rice: \t\t\t₹180\t' + E_check15.get() + "\n")
    if (var16.get() == 1):
        txtReceipt.insert(END, 'Eight Delicacies Rice: \t\t\t₹180\t' + E_check16.get() + "\n")
    if (var17.get() == 1):
        txtReceipt.insert(END, 'Schezwan Fried Rice : \t\t\t₹200\t' + E_check17.get() + "\n")
    if (var18.get() == 1):
        txtReceipt.insert(END, 'Fried leek dumplings: \t\t\t₹200\t' + E_check18.get() + "\n")
    if (var19.get() == 1):
        txtReceipt.insert(END, 'Steamed dumplings: \t\t\t₹200\t' + E_check19.get() + "\n")
    if (var20.get() == 1):
        txtReceipt.insert(END, 'Sliced Noodles: \t\t\t₹220\t' + E_check20.get() + "\n")
    if (var21.get() == 1):
        txtReceipt.insert(END, 'Spicy hot Noodles:\t\t\t₹240\t' + E_check21.get() + "\n")
    if (var22.get() == 1):
        txtReceipt.insert(END, 'Sesame paste Noodles:\t\t\t₹260\t' + E_check22.get() + "\n")
    if (var23.get() == 1):
        txtReceipt.insert(END, 'Eel Noodles: \t\t\t₹260\t' + E_check23.get() + "\n")
    if (var24.get() == 1):
        txtReceipt.insert(END, 'Seafood Noodles: \t\t\t₹290\t' + E_check24.get() + "\n")
    if (var25.get() == 1):
        txtReceipt.insert(END, 'Fish ball soup: \t\t\t₹30\t' + E_check25.get() + "\n")
    if (var26.get() == 1):
        txtReceipt.insert(END, 'Meat ball soup: \t\t\t₹40\t' + E_check26.get() + "\n")
    if (var27.get() == 1):
        txtReceipt.insert(END, 'Egg & Vegetable soup: \t\t\t₹45\t' + E_check27.get() + "\n")
    if (var28.get() == 1):
        txtReceipt.insert(END, 'Oyster soup:   \t\t\t₹55\t' + E_check28.get() + "\n")

    if (varr1.get() == 1):
        txtReceipt.insert(END, 'Mushroom-Sausage Rag: \t\t\t₹180\t' + E_checkk1.get() + "\n")
    if (varr2.get() == 1):
        txtReceipt.insert(END, 'Three-Cheese Lasagna: \t\t\t₹180\t' + E_checkk2.get() + "\n")
    if (varr3.get() == 1):
        txtReceipt.insert(END, 'Grilled Fish: \t\t\t₹200\t' + E_checkk3.get() + "\n")
    if (varr4.get() == 1):
        txtReceipt.insert(END, 'Beef Brasato: \t\t\t₹200\t' + E_checkk4.get() + "\n")
    if (varr5.get() == 1):
        txtReceipt.insert(END, 'Risotto: \t\t\t₹200\t' + E_checkk5.get() + "\n")
    if (varr6.get() == 1):
        txtReceipt.insert(END, 'Swordfish Sicilian-Style: \t\t\t₹220\t' + E_checkk6.get() + "\n")
    if (varr7.get() == 1):
        txtReceipt.insert(END, 'Braised Chicken: \t\t\t₹240\t' + E_checkk7.get() + "\n")
    if (varr8.get() == 1):
        txtReceipt.insert(END, 'Mushroom Lasagna: \t\t\t₹260\t' + E_checkk8.get() + "\n")
    if (varr9.get() == 1):
        txtReceipt.insert(END, 'Italian Meatballs: \t\t\t₹260\t' + E_checkk9.get() + "\n")
    if (varr10.get() == 1):
        txtReceipt.insert(END, 'Farro Soup: \t\t\t₹290\t' + E_checkk10.get() + "\n")
    if (varr11.get() == 1):
        txtReceipt.insert(END, 'Pomodori Fritti: \t\t\t₹30\t' + E_checkk11.get() + "\n")
    if (varr12.get() == 1):
        txtReceipt.insert(END, 'Insalata Mista: \t\t\t₹40\t' + E_checkk12.get() + "\n")
    if (varr13.get() == 1):
        txtReceipt.insert(END, 'Insalata Verde: \t\t\t₹45\t' + E_checkk13.get() + "\n")
    if (varr14.get() == 1):
        txtReceipt.insert(END, 'Insalata Di Pomodori: \t\t\t₹55\t' + E_checkk14.get() + "\n")

    if (varr15.get() == 1):
        txtReceipt.insert(END, 'Chicken Medallions : \t\t\t₹180\t' + E_checkk15.get() + "\n")
    if (varr16.get() == 1):
        txtReceipt.insert(END, 'Mediterranean Lettuce Wraps:\t\t\t₹180\t' + E_checkk16.get() + "\n")
    if (varr17.get() == 1):
        txtReceipt.insert(END, 'Lemon Greek Chicken: \t\t\t₹200\t' + E_checkk17.get() + "\n")
    if (varr18.get() == 1):
        txtReceipt.insert(END, 'Mediterranean Hummus Pizza:\t\t\t₹200\t' + E_checkk18.get() + "\n")
    if (varr19.get() == 1):
        txtReceipt.insert(END, 'Red Pepper Pizza: \t\t\t₹200\t' + E_checkk19.get() + "\n")
    if (varr20.get() == 1):
        txtReceipt.insert(END, 'Chicken & Orzo Soup:\t\t\t₹220\t' + E_checkk20.get() + "\n")
    if (varr21.get() == 1):
        txtReceipt.insert(END, 'Greek Lemon Chicken Soup:\t\t\t₹240\t' + E_checkk21.get() + "\n")
    if (varr22.get() == 1):
        txtReceipt.insert(END, 'Griddled chicken:\t\t\t₹260\t' + E_checkk22.get() + "\n")
    if (varr23.get() == 1):
        txtReceipt.insert(END, 'chicken tray bake : \t\t\t₹260\t' + E_checkk23.get() + "\n")
    if (varr24.get() == 1):
        txtReceipt.insert(END, 'Crunchy baked mussels : \t\t\t₹290\t' + E_checkk24.get() + "\n")
    if (varr25.get() == 1):
        txtReceipt.insert(END, 'potato salad : \t\t\t₹30\t' + E_checkk25.get() + "\n")
    if (varr26.get() == 1):
        txtReceipt.insert(END, 'summer salad : \t\t\t₹40\t' + E_checkk26.get() + "\n")
    if (varr27.get() == 1):
        txtReceipt.insert(END, 'feta cheese toasts : \t\t\t₹45\t' + E_checkk27.get() + "\n")
    if (varr28.get() == 1):
        txtReceipt.insert(END, 'mozzarella salad : \t\t\t₹55\t' + E_checkk28.get() + "\n")
    
    txtReceipt.insert(END, 'Sub Total:\t\t\t' + DP[0] +' ' +str(DP[1])+ "\n" + 'CGST(2.5%):\t\t\t' + AA[0] +' '+ str(AA[1])	+ "\n")
    txtReceipt.insert(END, 'SGST(2.5%):\t\t\t' + Tax[0] + ' '+str(Tax[1]) + "\n" + 'Total:\t\t\t' + TOC[0] + ' '+str(TOC[1]) + "\n"+'\t\t Thankyou!!\n'+'\t\tVisit Again')
    
# -------------------variables required for program-----------------
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
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()

varr1 = IntVar()
varr2 = IntVar()
varr3 = IntVar()
varr4 = IntVar()
varr5 = IntVar()
varr6 = IntVar()
varr7 = IntVar()
varr8 = IntVar()
varr9 = IntVar()
varr10 = IntVar()
varr11 = IntVar()
varr12 = IntVar()
varr13 = IntVar()
varr14 = IntVar()
varr15 = IntVar()
varr16 = IntVar()
varr17 = IntVar()
varr18 = IntVar()
varr19 = IntVar()
varr20 = IntVar()
varr21 = IntVar()
varr22 = IntVar()
varr23 = IntVar()
varr24 = IntVar()
varr25 = IntVar()
varr26 = IntVar()
varr27 = IntVar()
varr28 = IntVar()

DateOfOrder = StringVar()
Receipt = StringVar()
COD = StringVar()
COC = StringVar()
PT = StringVar()
SC = StringVar()
T = StringVar()
ST = StringVar()

E_check1 = StringVar()
E_check2 = StringVar()
E_check3 = StringVar()
E_check4 = StringVar()
E_check5 = StringVar()
E_check6 = StringVar()
E_check7 = StringVar()
E_check8 = StringVar()
E_check9 = StringVar()
E_check10 = StringVar()
E_check11 = StringVar()
E_check12 = StringVar()
E_check13 = StringVar()
E_check14 = StringVar()
E_check15 = StringVar()
E_check16 = StringVar()
E_check17 = StringVar()
E_check18 = StringVar()
E_check19 = StringVar()
E_check20 = StringVar()
E_check21 = StringVar()
E_check22 = StringVar()
E_check23 = StringVar()
E_check24 = StringVar()
E_check25 = StringVar()
E_check26 = StringVar()
E_check27 = StringVar()
E_check28 = StringVar()

E_checkk1 = StringVar()
E_checkk2 = StringVar()
E_checkk3 = StringVar()
E_checkk4 = StringVar()
E_checkk5 = StringVar()
E_checkk6 = StringVar()
E_checkk7 = StringVar()
E_checkk8 = StringVar()
E_checkk9 = StringVar()
E_checkk10 = StringVar()
E_checkk11 = StringVar()
E_checkk12 = StringVar()
E_checkk13 = StringVar()
E_checkk14 = StringVar()
E_checkk15 = StringVar()
E_checkk16 = StringVar()
E_checkk17 = StringVar()
E_checkk18 = StringVar()
E_checkk19 = StringVar()
E_checkk20 = StringVar()
E_checkk21 = StringVar()
E_checkk22 = StringVar()
E_checkk23 = StringVar()
E_checkk24 = StringVar()
E_checkk25 = StringVar()
E_checkk26 = StringVar()
E_checkk27 = StringVar()
E_checkk28 = StringVar()


E_check1.set("0")
E_check2.set("0")
E_check3.set("0")
E_check4.set("0")
E_check5.set("0")
E_check6.set("0")
E_check7.set("0")
E_check8.set("0")
E_check9.set("0")
E_check10.set("0")
E_check11.set("0")
E_check12.set("0")
E_check13.set("0")
E_check14.set("0")
E_check15.set("0")
E_check16.set("0")
E_check17.set("0")
E_check18.set("0")
E_check19.set("0")
E_check20.set("0")
E_check21.set("0")
E_check22.set("0")
E_check23.set("0")
E_check24.set("0")
E_check25.set("0")
E_check26.set("0")
E_check27.set("0")
E_check28.set("0")

E_checkk1.set("0")
E_checkk2.set("0")
E_checkk3.set("0")
E_checkk4.set("0")
E_checkk5.set("0")
E_checkk6.set("0")
E_checkk7.set("0")
E_checkk8.set("0")
E_checkk9.set("0")
E_checkk10.set("0")
E_checkk11.set("0")
E_checkk12.set("0")
E_checkk13.set("0")
E_checkk14.set("0")
E_checkk15.set("0")
E_checkk16.set("0")
E_checkk17.set("0")
E_checkk18.set("0")
E_checkk19.set("0")
E_checkk20.set("0")
E_checkk21.set("0")
E_checkk22.set("0")
E_checkk23.set("0")
E_checkk24.set("0")
E_checkk25.set("0")
E_checkk26.set("0")
E_checkk27.set("0")
E_checkk28.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))

# --------------------test butttons and frames---------------------------------
Button(f1aaa, text='INDIAN CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=indian).pack()
Button(f1aab, text='ITALIAN CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=italian).pack()
Button(f1aba, text='CHINESE CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=chinese).pack()
Button(f1abb, text='MEDITERRANEAN CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=mediterranean).pack()

# --------------------creating receipt(creating labels)-------------
lb1Receipt = Label(ft2, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="RECEIPT:", bd=2, anchor='w')
lb1Receipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=40, height=18, bg="white", bd=4, font=('Trebuchet MS', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

# -----------------------Price Information--------------------------
lb1COD1 = Label(f2aa, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="SUB TOTAL:", bd=8, anchor='w')
lb1COD1.grid(row=2, column=0, sticky=W)
txtCOD1 = Entry(f2aa, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=COD)
txtCOD1.grid(row=2, column=1)

lb1SC1 = Label(f2aa, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="CGST(2.5%):", bd=8, anchor='w')
lb1SC1.grid(row=3, column=0, sticky=W)
txtSC1 = Entry(f2aa, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=SC)
txtSC1.grid(row=3, column=1)

# ---------------------Payment Options---------------------------
lb1PT1 = Label(f2ab, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="SGST(2.5%):", bd=8, anchor='w')
lb1PT1.grid(row=2, column=0, sticky=W)
txtPT1 = Entry(f2ab, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=PT)
txtPT1.grid(row=2, column=1)

lb1T1 = Label(f2ab, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="TOTAL:", bd=8, anchor='w')
lb1T1.grid(row=4, column=0, sticky=W)
txtT1 = Entry(f2ab, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=T)
txtT1.grid(row=4, column=1)
#------------------------Execute-----------------------------------
def Execute():
    global r1
    l=[]
    gh=my.connect(host="localhost",user="root",password="gunsandroses007",database="Mp")
    ij=gh.cursor()
    if gh.is_connected()==True:
        print("Sure!")
    c="insert into recipt values (%s,%s,curdate())"
    print(c)
    ij.execute(c,(b,a))
    gh.commit()
    ij.execute("select * from recipt")
    x=ij.fetchall()
    n=len(x)
    print(type(str(x)))
    for i in x:
        l.append((i))
        print(i)
    print(i[2])  
    r1.writelines(str(l[n-1]))
    r1.close()
# -----------------------creating buttons--------------------------
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="TOTAL",
                  command=COI).grid(row=0, column=0)

btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="RECEIPT",
                    command=Rcpt).grid(row=0, column=1)

btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="RESET",
                  command=Reset).grid(row=0, column=2)

btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="EXIT",
                 command=qExit).grid(row=0, column=3)
btnReport = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue",font=('Trebuchet MS', 11, 'bold'), width=4, text="REPORT",
                 command=Report).grid(row=0, column=4)
btnExecute = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue",font=('Trebuchet MS', 11,'bold'), width=4,text="EXECUTE",
                 command=Execute).grid(row=0, column=5)   
root1.mainloop()
print(a,",",b)


