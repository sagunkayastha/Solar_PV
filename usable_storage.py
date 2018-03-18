import Loads
from Tkinter import*
from Loads import z
#z=3000
tk2=Tk()
e=DoubleVar()
a={'Jan': [2.9, 3.2, 3.4], 'Feb': [4.0, 4.3, 4.4],'Mar': [5.0, 5.2, 5.1], 'Apr': [5.9, 5.8, 5.4], 'May': [6.6, 6.2, 5.5],'Jun': [7.2, 6.6, 5.6],'July': [7.3, 6.7, 6.1],'Aug': [7.0, 6.7, 6.1], 'Sept': [6.3, 6.4, 6.1], 'Oct': [5.0, 5.4, 5.5], 'Nov': [3.3, 3.7, 3.9],  'Dec': [2.5, 2.9, 3.1], }
storage_days=[]
peak_sun=[]
battery=[]
ans2=DoubleVar()
x=IntVar()
Ah_load=0
def calculate():
     global battery,storage_days,Ah_load
     Dc_load= float(z)*100/e.get()
     Ah_load=Dc_load/battery
     Usable_storage=Ah_load*storage_days
##     print Dc_load
##     print battery
##     print Ah_load
####     print peak_sun
####     print 'storage_days',storage_days
##     print Usable_storage
     ans2.set(Usable_storage)
def one():
     global peak_sun
     peak_sun=a['Dec'][0]
     
     
def two():
     global peak_sun
     peak_sun=a['Dec'][1]
     return
     
def three():
     global peak_sun
     peak_sun=a['Dec'][2]
     
def one1():
     global battery
     battery = 12
def two2():
     global battery
     battery = 24
     
def one3():
     global storage_days,peak_sun     
     storage_days=9.43-1.9*(peak_sun)+0.11*(peak_sun)**2
     
     
def two3():
     global storage_days,peak_sun
     storage_days=24.0-4.73*(peak_sun)+0.3*(peak_sun)**2
     
     
def Next():
     tk2.destroy()
     
Efficiency =Label(tk2,text = 'Inverter Efficiency').grid(row=0,column=0,sticky=E)
Eff=Entry(tk2,textvariable= e).grid(row=0,column=1)

Radio_1= Radiobutton(tk2, text= 'Lat -15',value=1,variable=1,command=one).grid(row=2)
Radio_2= Radiobutton(tk2, text= 'Lat ',value=2,variable=1,command=two).grid(row=3)
Radio_3= Radiobutton(tk2, text= 'Lat +15',value=3,variable=1,command=three).grid(row=4)

V_12= Radiobutton(tk2, text= '12 V',value=4,variable=2,command=one1).grid(row=2,column=2)
V_24= Radiobutton(tk2, text= '24 V ',value=5,variable=2,command=two2).grid(row=3,column=2)

for_95= Radiobutton(tk2, text= '95% Availability',value=6,variable=3,command=one3).grid(row=2,column=1)
for_99= Radiobutton(tk2, text= '99% Availability ',value=7,variable=3,command=two3).grid(row=3,column=1)
button=Button(tk2,text='Okay',command=calculate).grid(row=5,column=1)

Usable_storage=Label(tk2,text = 'Total Usable Storage').grid(row=6,column=0,sticky=E)
Us=Entry(tk2,textvariable= ans2).grid(row=6,column=1)
button2=Button(tk2,text='Next',command=Next).grid(row=7,column=2)

tk2.mainloop()
