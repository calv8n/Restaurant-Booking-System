import tkinter as tk
from tkinter import messagebox
import mysql.connector as my
import matplotlib.pyplot as pl
root = tk.Tk()
def Plot1():
    z=[]
    y=[]
    g=[]
    a=my.connect(host="localhost",user="root",password="gunsandroses007",database="mp")
    b=a.cursor()
    b.execute("select sum(total) from recipt")
    x=b.fetchall()
    print(type(x))
    print(type(x[0]))
    print(int(x[0][0]))
    b.execute("select date,sum(total) from recipt group by date")
    x=b.fetchall()
    n=len(x)
    for i in range(n):
        z.append(str(x[i][0]))
        y.append(int(x[i][1]))
    print(z)
    print(y)
    pl.bar(z,y,width=0.5)
    pl.xlabel('Dates')
    pl.ylabel('Grand Total for each day')
    pl.show()
def Plot2():
    z=[]
    y=[]
    g=[]
    a=my.connect(host="localhost",user="root",password="gunsandroses007",database="mp")
    b=a.cursor()
    b.execute("select sum(total) from recipt")
    x=b.fetchall()
    print(type(x))
    print(type(x[0]))
    print(int(x[0][0]))
    b.execute("select date,sum(total) from recipt group by date")
    x=b.fetchall()
    n=len(x)
    for i in range(n):
        z.append(str(x[i][0]))
        y.append(int(x[i][1]))
    print(z)
    print(y)
    pl.plot(z,y)
    pl.xlabel('Dates')
    pl.ylabel('Grand Total for each day')
    pl.show()
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

root = tk.Tk()

root.geometry("1350x750")
root.title("Muffada Allah Halal Kitchen")
root.configure(background="dark slate blue")


v = tk.IntVar()

tk.Label(root, 
        text="""Choose to plot or quit""",
        justify = tk.LEFT,
        padx = 20,pady=12).pack()
tk.Radiobutton(root, 
              text="Bar Graph",
              padx = 20,pady=12, 
              variable=v,command=Plot1, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="Line Graph",
              padx = 20,pady=12, 
              variable=v,command=Plot2, 
              value=2).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="Quit",
              padx = 20, pady=12,
              variable=v,command=qExit, 
              value=3).pack(anchor=tk.W)

    

root.mainloop()
