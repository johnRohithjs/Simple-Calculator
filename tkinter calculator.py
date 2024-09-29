from tkinter import *

window = Tk()
window.title('Simple Calculator')
window.iconbitmap("C:/Users/johnr/Downloads/Calculator_30001.ico")


def ButtonClick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(1,str(current)+str(num))

def ButtonClear():
    e.delete(0,END)

def Add():
    global fnum,code
    code=1
    num1=e.get()
    fnum=int(num1)
    e.delete(0,END)

def Sub():
    global fnum,code
    code=2
    num1=e.get()
    fnum=int(num1)
    e.delete(0,END)

def Mul():
    global fnum,code
    code=3
    num1=e.get()
    fnum=int(num1)
    e.delete(0,END)

def Div():
    global fnum,code
    code=4
    num1=e.get()
    fnum=int(num1)
    e.delete(0,END)

def Equal():
    num2=e.get()
    snum=int(num2)
    e.delete(0,END)
    if code==1:
        e.insert(1,fnum+snum)
    elif code==2:
        e.insert(1,fnum-snum)
    elif code==3:
        e.insert(1,fnum*snum)
    else:
        try:
            e.insert(1,fnum/snum)
        except:
            e.insert("ERROR")

e=Entry(width=90,borderwidth=5)
e.grid(row=0,column=0,columnspan=5)

button1=Button(text='1',padx=40,pady=20,command=lambda: ButtonClick(1),fg='Black',bg='Orange').grid(row=1,column=0)
button2=Button(text='2',padx=40,pady=20,command=lambda: ButtonClick(2),fg='Black',bg='Orange').grid(row=1,column=1)
button3=Button(text='3',padx=40,pady=20,command=lambda: ButtonClick(3),fg='Black',bg='Orange').grid(row=1,column=2)
buttonadd=Button(text='+',padx=39,pady=20,command=Add,fg='Black',bg='Orange').grid(row=1,column=3)
buttonsub=Button(text='-',padx=40,pady=20,command=Sub,fg='Black',bg='Orange').grid(row=1,column=4)


button4=Button(text='4',padx=40,pady=20,command=lambda: ButtonClick(4),fg='Black',bg='Orange').grid(row=2,column=0)
button5=Button(text='5',padx=40,pady=20,command=lambda: ButtonClick(5),fg='Black',bg='Orange').grid(row=2,column=1)
button6=Button(text='6',padx=40,pady=20,command=lambda: ButtonClick(6),fg='Black',bg='Orange').grid(row=2,column=2)
buttonmul=Button(text='*',padx=40,pady=19,command=Mul,fg='Black',bg='Orange').grid(row=2,column=3)
buttonequal=Button(text='=',padx=40,pady=83,command=Equal,fg='Black',bg='Orange').grid(row=2,column=4,rowspan=3)

button7=Button(text='7',padx=40,pady=20,command=lambda: ButtonClick(7),fg='Black',bg='Orange').grid(row=3,column=0)
button8=Button(text='8',padx=40,pady=20,command=lambda: ButtonClick(8),fg='Black',bg='Orange').grid(row=3,column=1)
button9=Button(text='9',padx=40,pady=20,command=lambda: ButtonClick(9),fg='Black',bg='Orange').grid(row=3,column=2)
buttondiv=Button(text='/',padx=40,pady=52,command=Div,fg='Black',bg='Orange').grid(row=3,column=3,rowspan=2)

buttonClear=Button(text='Clear',padx=29,pady=21,command= ButtonClear,fg='Black',bg='Orange').grid(row=4,column=0)
button0=Button(text='0',padx=95,pady=18,command=lambda: ButtonClick(0),fg='Black',bg='Orange').grid(row=4,column=1,columnspan=2)



lable1=Label()

window.mainloop()
