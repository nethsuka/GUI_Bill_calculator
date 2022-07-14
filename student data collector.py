from tkinter import*

root=Tk()
root.title("Student Data Collector")
root.geometry('510x600')

mainframe=Frame(root,padx=5,bd=10)
mainframe.grid()

frame1=Frame(mainframe,width=100,height=100,bd=14,relief=RIDGE)
frame1.grid(row=0,column=0)

label1=Label(frame1,text='Student Data Collector',font=('Helvetica',31,'bold'),justify=CENTER,bg="#c0ded9")
label1.grid()

frame2=LabelFrame(mainframe,bd=14,relief=RIDGE,padx=5,font=('Helvetica',13,'bold'),text='Enter Data To Collect')
frame2.grid(row=1,column=0)

name=StringVar()
grade=StringVar()
M=IntVar()
N=IntVar()
E=IntVar()

label2=Label(frame2,text='Student Name ',font=('Helvetica',14,'bold'))
label2.grid(row=0,column=0,padx=16,pady=9)             

textbox1=Entry(frame2,textvariable=name,font=('areal',14,'bold'),bd=10)
textbox1.grid(row=0,column=1,padx=16,pady=9)

label3=Label(frame2,text='Enter Class',font=('Helvetica',14,'bold'))
label3.grid(row=1,column=0,padx=16,pady=9)

textbox2=Entry(frame2,textvariable=grade,font=('areal',14,'bold'),bd=10)
textbox2.grid(row=1,column=1,padx=16,pady=9)

label4=Label(frame2,text='Maths Marks',font=('Helvetica',14,'bold'))
label4.grid(row=2,column=0,padx=16,pady=9)

textbox3=Entry(frame2,textvariable=M,font=('areal',14,'bold'),bd=10)
textbox3.grid(row=2,column=1,padx=16,pady=9)

label5=Label(frame2,text='Science Marks',font=('Helvetica',14,'bold'))
label5.grid(row=3,column=0,padx=16,pady=9)

textbox4=Entry(frame2,textvariable=N,font=('areal',14,'bold'),bd=10)
textbox4.grid(row=3,column=1,padx=16,pady=9)

label6=Label(frame2,text='English Marks',font=('Helvetica',14,'bold'))
label6.grid(row=4,column=0,padx=16,pady=9)

textbox5=Entry(frame2,textvariable=E,font=('areal',14,'bold'),bd=10)
textbox5.grid(row=4,column=1,padx=16,pady=9)

label7=Label(frame2,text='click on add to file and it will create',font=('Helvetica',8))
label7.grid(row=5)

label8=Label(frame2,text='stdata.txt file on the same folder',font=('Helvetica',8))
label8.grid(row=6)

frame3=LabelFrame(mainframe,bd=14,relief=RIDGE,padx=5,font=('Helvetica',13,'bold'),text='Click To Add')
frame3.grid(row=2,column=0)

def add():
    f=open("add.txt","a")
    total=M.get()+N.get()+E.get()
    avg=(M.get()+N.get()+E.get())/3
    data="Student Name :"+str(name.get())+"\n"+"Class              :"+str(grade.get())+"\n"+"Maths Marks  :"+str(M.get())+"\n"+"Science Marks:"+str(N.get())+"\n"+"English Marks:"+str(E.get())+"\n"+"Total Marks    :"+str(total)+"\n"+"Average         :"+  str(avg)+"%"+"\n"+"     "+"\n"+"================================="+"\n"
    f.write(data)
    f.close()

    textbox1.delete(0,END)
    textbox2.delete(0,END)
    textbox3.delete(0,END)
    textbox4.delete(0,END)
    textbox5.delete(0,END)

button1=Button(frame3,text='ADD DATA TO FILE',bg='#c0ded9',font=('Arial',14,'bold'),bd=10,width=22,command=add)
button1.grid(row=0,column=0)
    
def myreset():
    name.set("")
    grade.set("")
    M.set("")
    N.set("")
    E.set("")

button2=Button(frame3,text='RESET',bg='#c0ded9',font=('Arial',14,'bold'),bd=10,width=11,command=myreset)
button2.grid(row=0,column=1)

root.mainloop()
