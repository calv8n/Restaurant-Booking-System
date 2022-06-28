import matplotlib.pyplot as pl
import mysql.connector as my
def Plot():
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
    pl.bar(z,y)
    pl.show()
    
Plot()
