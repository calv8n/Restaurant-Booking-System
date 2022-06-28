import mysql.connector as my
def Sqlish(a,b):
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
    for i in x:
        print(i)
    print(i[2])  
