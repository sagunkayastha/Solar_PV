a11=TV_39in_active=142
a12=TV_39in_standby=3.5
a21=TV_25_27in_active=90
a22=TV_25_27in_standby=4.9
a31=Computer=125
a41=Laptop=20
a51=Lights=30
a61=Pump1=450
a71=Refrig14=1080
a81=Refrig19=1140
a91=Refrig22=1250
a21=Refrigdc=560
Pump2=100
xte='''All Loads in Watt
TV_39in_active=142
TV_39in_standby=3.5
TV_25_27in_active=90
TV_25_27in_standby=4.9\nComputer=125\nLaptop=20
Lights=30
Pump1=450
Refrig14=1080
Refrig19=1140
Refrig22=1250
Refrigdc=560
Pump2=100Whr/day'''
import numpy as np
from Tkinter import*
import tkMessageBox as ts
tk=Tk()
tk.geometry('425x250')
a1,a2,a3,a4,a5,a6,D,ans=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
b1,b2,b3,b4,b5,b6=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
a=np.array([a1,a2,a3,a4,a5,a6])
b=np.array([b1,b2,b3,b4,b5,b6])
c=np.array([a11,a21,a31,a41,a51,a61])
z=0

#######################function##########
def Numbers():
     global z
     na=[]
     nb=[]
     dd=D.get()
     for i in a:
          z=i
          na.append(z.get())
     for i in b:
          z=i
          nb.append(z.get())
     if dd==14:
          d=a71
     elif dd==19:
          d=a81
     elif dd==22:
          d=a91
     elif dd==12:
          d=a21
     else:
          d=0
     z= c*na*nb
     total= sum(z)+d
     z=str(total)
    
     ans.set(z)
     
def showLoads():
     ts.showinfo('Window', xte)
     return
##     na1=a1.get(); na2=a2.get();na3=a3.get();na4=a4.get();na5=a5.get();na6=a6.get()
##     nb1=b1.get(); nb2=b2.get();nb3=b3.get();nb4=b4.get();nb5=b5.get();nb6=b6.get()
def Next():
     tk.destroy()

#########################for numbers########
label1=Label(tk,text = 'No ').grid(row=0,column=1)
label2=Label(tk,text = 'Hours ').grid(row=0,column=2)
TV_39 =Label(tk,text = '39 in. TV ').grid(row=1,column=0,sticky=E)
TV_39no=Entry(tk,textvariable= a1).grid(row=1,column=1)
TV_39hr=Entry(tk,textvariable= b1).grid(row=1,column=2)

TV_25=Label(tk,text = '25-27 in. TV').grid(row=2,column=0,sticky=E)
TV_25no=Entry(tk,textvariable= a2).grid(row=2,column=1)
TV_25hr=Entry(tk,textvariable= b2).grid(row=2,column=2)

Computer=Label(tk,text = 'Computer').grid(row=3,column=0,sticky=E)
Computerno=Entry(tk,textvariable= a3).grid(row=3,column=1)
Computerehr=Entry(tk,textvariable= b3).grid(row=3,column=2)


Laptop=Label(tk,text = 'Laptop').grid(row=4,column=0,sticky=E)
Laptopent=Entry(tk,textvariable= a4).grid(row=4,column=1)
Laptophr=Entry(tk,textvariable= b4).grid(row=4,column=2)

Lights=Label(tk,text = 'Lights').grid(row=5,column=0,sticky=E)
Lightent=Entry(tk,textvariable= a5).grid(row=5,column=1)
Lighthr=Entry(tk,textvariable= b5).grid(row=5,column=2)

Pump1=Label(tk,text = 'Pump').grid(row=6,column=0,sticky=E)
Pumpent=Entry(tk,textvariable= a6).grid(row=6,column=1)
Pumphr=Entry(tk,textvariable= b6).grid(row=6,column=2)

Refrig=Label(tk,text = 'Refrigerator Size\n(14, 19, 22)').grid(row=7,column=0,sticky=E)
Refrig=Entry(tk,textvariable= D).grid(row=7,column=1)

Loads=Label(tk,text = 'Total Load',bg='White').grid(row=9,column=0,sticky=E)
Loads=Entry(tk,textvariable= ans).grid(row=9,column=1)

#ccc=Checkbutton(tk, text='check box').grid(row=8,columnspan=2)



mbutton = Button(tk, text= ' Ok ',command= Numbers).grid(row=4,column =4)
mbutton2 = Button(tk, text= 'Show loads ',command= showLoads).grid(row=5,column =4)
mbutton2 = Button(tk, text= 'Next ',command= Next).grid(row=9,column =4)

#mexit= Button(tk, text= ' Next ',command= tk.exit).grid(row=8,column =4)
tk.mainloop()

