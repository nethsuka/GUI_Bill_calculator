from tkinter import*

mywindow=Tk()
mywindow.title("House Electricity Bill")
mywindow.geometry('610x290')

frame1=Frame(mywindow,padx=5,bd=16)
frame1.grid()

frame2=Frame(frame1,width=300,height=300,padx=7,bd=16,relief=RIDGE)
frame2.grid(row=0,column=0)

label1=Label(frame2,text='Enter the previous reading',font=('areal',14,'bold'),bd=10)
label1.grid(row=0,column=0,padx=5,pady=10)

Preading=IntVar()
Creading=IntVar()

textbox1=Entry(frame2,textvariable=Preading,fg='green',font=('areal',14,'bold'),bd=10)
textbox1.grid(row=0,column=1)

label2=Label(frame2,text='Enter the current reading',font=('areal',14,'bold'),bd=10)
label2.grid(row=1,column=0,pady=10)

textbox2=Entry(frame2,textvariable=Creading,fg='green',font=('areal',14,'bold'),bd=10)
textbox2.grid(row=1,column=1)

def myfunction():
    units=Creading.get()-Preading.get()
    if units<=60:
        R=units*7.85+90
    elif (units-60)<=30:
        R=(units-60)*10+60*7.85+90
    elif (units-90)<=30:
        R=60*7.85+30*10+((units-90)*27.75)+90
    elif (units-120)<=56:
        R=60*7.85+30*10+30*27.75+((units-120)*32)+90
    else:
        R=60*7.85+30*10+30*27.75+62*32+((units-176)*45)+90
    emptylabel.config(text='Rs '+str(R))

button1=Button(frame2,command=myfunction,text='CALCULATE',fg='blue',bg='pink',font=('Arial',14,'bold'),bd=10)
button1.grid(row=2,column=1,sticky=W)

def myreset():
    Preading.set("")
    Creading.set("")

button2=Button(frame2,command=myreset,text='RESET',fg='blue',bg='pink',font=('Arial',14,'bold'),bd=10)
button2.grid(row=2,column=1,sticky=E)

label3=Label(frame2,text='Total Bill : ',font=('areal',14,'bold'))
label3.grid(row=3,column=0,sticky=E,pady=10)

emptylabel=Label(frame2,fg='green',font=('areal',14,'bold'))
emptylabel.grid(row=3,column=1,sticky=W,pady=10)

mywindow.mainloop()

