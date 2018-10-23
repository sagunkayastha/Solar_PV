import p3_Nominal_final
from p3_Nominal_final import Nom
from other_data import battery_char
from tkinter import*
import sys
from p2_usable_storage import battery


series,parallel=0,0
tk4=Tk()
x=StringVar()
y=StringVar()
Voltage,Ah,parallel,series=0,0,0,0
photo1=PhotoImage(file='images/block_i1.gif')
photo2=PhotoImage(file='images/block_i2.gif')
photo3=PhotoImage(file='images/block_imiddle.gif')
photo4=PhotoImage(file='images/block_itop.gif')
photo5=PhotoImage(file='images/block_ibot.gif')

def one():
     global Voltage,Ah
     Voltage=battery_char['Conorde PVX 5040T'][0]
     Ah=battery_char['Conorde PVX 5040T'][2]
def two():
     global Voltage,Ah
     Voltage=battery_char['Trojan T-105'][0]
     Ah=battery_char['Trojan T-105'][2]
def three():
     global Voltage,Ah
     Voltage=battery_char['Trojan L16'][0]
     Ah=battery_char['Trojan L16'][2]
def four():
     global Voltage,Ah
     Voltage=battery_char['Conorde PVX 1080'][0]
     Ah=battery_char['Conorde PVX 1080'][2]
def five():
     global Voltage,Ah
     Voltage=battery_char['Surette 12CS11PS'][0]
     Ah=battery_char['Surette 12CS11PS'][2]
########################################################################3     
def Print():
     global Voltage,Ah,parallel,series
     print(Voltage,Ah)
     series=battery/Voltage
     print('Nom = ',Nom)
     parallel=int(Nom/Ah)
     if (Ah*parallel)<Nom:
          parallel=parallel+1
     x.set(series)
     y.set(parallel)
     #tk4.destroy()
     
def Final_w():
     global series,parallel
     import sys
     
     series=int(series)
     parallel=int(parallel)
     sizex=parallel*50+25
     sizey= series*50
     x,y=25,25
     canvas1= Canvas(tk4,height=500,width=500,bg='White')
     canvas1.grid(row=0,column=1)
     print(sizex,sizey)
     j=0
     for i in range(parallel):
          if i ==0 and j==0:
               photo=photo1
               
          canvas1.create_image(x,y,image=photo)
          for j in range(series):
               if i==0 and j==series-1:
                    photo=photo2
               elif i>=0 and i<parallel and j>0 and j<series-1 :
                    photo=photo3
               elif i>0 and j==0:
                    photo=photo4
               elif i>0 and j<series-1:
                    photo=photo4
               elif i>0 and j==series-1:
                    photo=photo5
               canvas1.create_image(x,y,image=photo)
               y=y+50
          x=x+50
          y=25

     tk4.mainloop()    
     return
def Next():
     tk4.destroy()
Concorde_5040T= Radiobutton(tk4, text= 'Conorde PVX 5040T',value=1,variable=2,command=one).grid(row=3,column=0,sticky=W)
Trojan_T_105= Radiobutton(tk4, text= 'Trojan T-105 ',value=2,variable=2,command=two).grid(row=4,column=0,sticky=W)
Trojan_L16= Radiobutton(tk4, text= 'Trojan L16',value=3,variable=2,command=three).grid(row=5,column=0,sticky=W)
Concorde_1080= Radiobutton(tk4, text= 'Conorde PVX 1080',value=4,variable=2,command=four).grid(row=6,column=0,sticky=W)
Surette_12CS= Radiobutton(tk4, text= 'Surette 12CS11PS',value=5,variable=2,command=five).grid(row=7,column=0,sticky=W)
canvas1= Canvas(tk4,height=500,width=500,bg='White')
canvas1.grid(row=0,column=1)
#######################################


series=Label(tk4,text = 'Series ').grid(row=1,column=0,sticky=W)
sers=Entry(tk4,textvariable= x).grid(row=1,column=1)
parallel=Label(tk4,text = 'parallel').grid(row=2,column=0,sticky=W)
pal=Entry(tk4,textvariable= y).grid(row=2,column=1)
button=Button(tk4,text='Okay',command=Print).grid(row=5,column=1)
button2=Button(tk4,text='Print Block Diagrawwm',command=Final_w).grid(row=6,column=1)
button3=Button(tk4,text='Next',command=Next).grid(row=7,column=1)
tk4.mainloop()
