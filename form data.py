from tkinter import *
from tkinter import messagebox
import sqlite3

sc=Tk()
sc.title('فرم ارزیابی')
sc.geometry('1450x800')
i=Label(sc,background='gray')
i.pack(fill=BOTH,expand=True)

def register1():
    sc.geometry("100x100")  
    messagebox.askquestion("تایید","اطلاعات شما ذخیره شود؟")
     
    name1=firstname.get()
    name2=lastname.get()
    code1=codemeli.get()
    sen1=sen.get()
    gender1=jensiatt.get()
    edu1=tahsilatt.get()
    address2=address1.get("1.0","end-1c")
    if takhasos1.get()==1:
        spec1="شبکه"
    else:
        spec1=""
    if takhasos2.get()==1:
        spec2="برنامه نویس"
    else:
        spec2=""
    if takhasos3.get()==1:
        spec3="الکترونیک"
    else:
        spec3=""
    tel1=tel.get()
    
    conn=sqlite3.connect('mft.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS student (Codemeli INT PRIMARY KEY,Name TEXT,Surname TEXT,Age INT,gender TEXT,tahsilat TEXT,takhasos1 TEXT,takhasos2 TEXT,takhasos3 TEXT,Address TEXT,Phone INT)''')
    cursor.execute('''INSERT INTO student(Codemeli,Name,Surname,Age,gender,tahsilat,takhasos1,takhasos2,takhasos3,Address,Phone) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(code1,name1,name2,sen1,gender1,edu1,spec1,spec2,spec3,address2,tel1))
    conn.commit()
     
def clear1():
    firstname.set("")
    lastname.set("")
    codemeli.set("")
    sen.set("")
    jensiatt.set("")  
    tahsilatt.set("") 
    takhasos1.set("")
    takhasos2.set("")
    takhasos3.set("")
    address.set("")
    tel.set("")


#=====================firstname=========================
firstnamet=Label(sc,text='نام ',font=20,bg='gray')
firstnamet.place(x=1350,y=90)
firstname=StringVar()
firstnamee=Entry(sc,textvariable=firstname,width='42',border='3',bg='#1f2421',fg='#ffd8c2',font=('tohoma',12),justify='right')
firstnamee.place(x=930,y=90)

#=====================lastname=========================
lastnamet=Label(sc,text='نام خانوادگی',font=20,bg='gray')
lastnamet.place(x=1320,y=140)
lastname=StringVar()
lastnamee=Entry(sc,textvariable=lastname,width='42',border='3',bg='#1f2421',fg='#ffd8c2',font=('tohoma',12),justify='right')
lastnamee.place(x=930,y=140)

#=====================code melli=======================
codemelli=Label(sc,text='کد ملی',font=20,bg='gray')
codemelli.place(x=650,y=90)
codemeli=StringVar()
codemellii=Entry(sc,textvariable=codemeli,width='32',border='3',bg='#1f2421',fg='#ffd8c2',font=('tohoma',12),justify='right')
codemellii.place(x=330,y=90)

#=====================age=============================
senn=Label(sc,text='سن',font=20,bg='gray')
senn.place(x=650,y=140)
sen=IntVar()
sen.set('')
sennn=Entry(sc,textvariable=sen,width='3',border='3',bg='#1f2421',fg='#ffd8c2',font=('tohoma',12),justify='right')
sennn.place(x=590,y=140)

#===================================jensiat=================================

jensiat=Label(text=':جنسیت',font=20,bg='gray')
jensiat.place(x=1320,y=220)
jensiatt=StringVar()  
jensiat1=Radiobutton(sc,text='آقا',variable=jensiatt,value='danesh amooz',bg='gray',activebackground='gray', font=5) 
jensiat1.place(x=1250,y=260)  
jensiat2=Radiobutton(sc,text= 'خانم', variable = jensiatt,value='diplom',bg='gray',activebackground='gray', font=10)
jensiat2.place(x=1120,y=260)

#======================tahsilat========================
tahsilat=Label(text=':تحصیلات',font=20,bg='gray')
tahsilat.place(x=1320,y=340)

tahsilatt=StringVar()  
tahsilat1=Radiobutton(sc,text='دانش آموز',variable=tahsilatt,value='danesh amooz',bg='gray',activebackground='gray',font=5) 
tahsilat1.place(x=1250,y=380)  
tahsilat2=Radiobutton(sc,text= 'دیپلم', variable = tahsilatt,value='diplom',bg='gray',activebackground='gray', font=10)
tahsilat2.place(x=1140,y=380) 
tahsilat3=Radiobutton(sc,text= 'کاردانی', variable = tahsilatt,value='kardani',bg='gray',activebackground='gray', font=10)
tahsilat3.place(x=1000,y=380)
tahsilat4=Radiobutton(sc,text= 'کارشناسی', variable = tahsilatt,value='karshenasi',bg='gray',activebackground='gray', font=10)
tahsilat4.place(x=850,y=380)
tahsilat5=Radiobutton(sc,text= 'کارشناسی ارشد', variable = tahsilatt,value='arshad',bg='gray',activebackground='gray', font=10)
tahsilat5.place(x=660,y=380)
tahsilat6=Radiobutton(sc,text= 'دکتری', variable = tahsilatt,value='doctora',bg='gray',activebackground='gray', font=10)
tahsilat6.place(x=550,y=380) 


#===================================takhasos=================================

takhasoss=Label(text=':تخصص',font=20,bg='gray')
takhasoss.place(x=1320,y=430)
takhasos1=IntVar()
takhasos2=IntVar()
takhasos3=IntVar()
takhasoss1=Checkbutton(sc,text='برنامه نویس' ,variable = takhasos1, height = 1, width = 7,bg='gray',activebackground='gray', font=6)
takhasoss1.place(x=1200,y=470)  
takhasoss2=Checkbutton(sc,text='شبکه', variable = takhasos2, height = 1, width = 7,bg='gray',activebackground='gray', font=6)
takhasoss2.place(x=1000,y=470)
takhasoss3=Checkbutton(sc,text='الکترونیک', variable = takhasos3, height = 1, width = 7,bg='gray',activebackground='gray', font=6)
takhasoss3.place(x=800,y=470)

#================================adrress====================================

addresss=Label(sc,text='آدرس',font=20,bg='gray')
addresss.place(x=1350,y=550)
address=StringVar()
address1=Text(sc,width='42',height='7', border='3',bg='#1f2421',fg='#ffd8c2',font=('tohoma',12)) 
address1.tag_configure('tag-right',justify='right') 
address1.place(x=930,y=550)
#===============================tel===========================================
tel=Label(sc,text='تلفن',font=20,bg='gray')
tel.place(x=1350,y=690)
tel=StringVar()
tel1=Entry(sc,textvariable=tel,width='42',border='3',bg='#1f2421',fg='#ffd8c2',font=('tohoma',12),justify='right')
tel1.place(x=930,y=690)

#===============================sabt clear====================================
btnclear=Button(sc,text="پاک کردن",width=7,height=2,bg='dark gray',activebackground='#8b523e' ,font=("Tohoma",12 ),command=clear1)
btnclear.place(x=420,y=700)
btnreg=Button(sc,text="ثبت",width=7,height=2,bg='dark gray',activebackground='#8b523e', font=("Tohoma",12 ),command=register1)
btnreg.place(x=710,y=700)

mainloop()

