# -*- coding: utf-8 -*-
import usable_storage
from Tkinter import*
from usable_storage import ans2,storage_days
from other_data import b,m
tk3=Tk()
y=ans2.get()
Nominal_battery=DoubleVar()
storage_days=5
sd=int(storage_days)+1
if sd>3:
   sd='C/72'
elif sd<=3:
     sd='C/48'

mdod=100
Tdr=100
i=0
##m={'30':39,'25':50,'20':62,'15':79,'10':97,'5':100}
##b={'C/72':[77,82,88,94,97,100],'C/48':[68,73,80,88,90,95],'C/20':[52,59,65,70,75,80],'C/10':[42,48,54,60,65,70]}
temp=[]
def one():
     global temp,i;temp='30';i=0
def two():
     global temp,i;temp='25';i=1
def three():
     global temp,i;temp='20';i=2
def four():
     global temp,i;temp='15';i=3
def five():
     global temp,i;temp='10';i=4
def six():
     global temp,i;temp='5';i=5
def one1():
     global mdod,m,temp,Tdr
     mdod=m[temp]
     if mdod>80:
          mdod=80
     
     Tdr=b[sd][i]
     
def two2():
     global mdod
     mdod=20
def final():
     global y,Tdr,Nom
     Nom=y*100*100/(Tdr*mdod)
     print Nom
     Nominal_battery.set(Nom)
     return
def Next():
     tk3.destroy()
     return
label1=Label(tk3,text='Minimum Temperature').grid(row=0,column=0)
Neg_30= Radiobutton(tk3, text= '-30◦C ',value=1,variable=2,command=one).grid(row=1,column=0)
Neg_25= Radiobutton(tk3, text= '-25◦C ',value=2,variable=2,command=two).grid(row=2,column=0)
Neg_20= Radiobutton(tk3, text= '-20◦C',value=3,variable=2,command=three).grid(row=3,column=0)
Neg_15= Radiobutton(tk3, text= '-15◦C',value=4,variable=2,command=four).grid(row=4,column=0)
Neg_10= Radiobutton(tk3, text= '-10◦C',value=5,variable=2,command=five).grid(row=5,column=0)
Neg_5= Radiobutton(tk3, text= '-5◦C',value=6,variable=2,command=six).grid(row=6,column=0)

label2=Label(tk3,text='Type of battery').grid(row=0,column=1)
Deep= Radiobutton(tk3, text= 'Deep Cycle',value=1,variable=1,command=one1).grid(row=1,column=1,sticky=W)
SLI= Radiobutton(tk3, text= 'SLI ',value=2,variable=1,command=two2).grid(row=2,column=1,sticky=W)
Nic_cad= Radiobutton(tk3, text= 'Nickel-cadmium',value=3,variable=1).grid(row=3,column=1,sticky=W)
Nic_metal= Radiobutton(tk3, text= 'Nickel-metal hydride',value=4,variable=1).grid(row=4,column=1,sticky=W)

Nom=Label(tk3,text = 'Nominal Storage in Ah ').grid(row=8,column=0,sticky=E)
Ues=Entry(tk3,textvariable= Nominal_battery).grid(row=8,column=1)
button=Button(tk3,text='Okay',command=final).grid(row=7)
mbutton2 = Button(tk3, text= 'Next ',command= Next).grid(row=9,column =1)
tk3.mainloop()
