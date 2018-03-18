import Block_battery
from usable_storage import peak_sun,Ah_load,battery
from Tkinter import*
from other_data import Pv_char
import tkMessageBox as ts
#Ah_load=147
#peak_sun=3.1
print battery
tk6=Tk()
ce,df=DoubleVar(),DoubleVar()
pvmod=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_modules.gif')
photo1=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_1st.gif')
photo2=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_1.gif')
photo3=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_2stup.gif')
photo4=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_2stdown.gif')
photo5=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_midup.gif')
photo6=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\Pv_middown.gif')
Ir,Pb,Ah_inverter=0,0,0
series,paraller=0,0
xx,yy=IntVar(),IntVar()
def one():
     global Ir,Pb
     Ir=Pv_char['Kyocera'][0]
     Pb=12
    
def two():
     global Ir,Pb
     Ir=Pv_char['Sharp'][0]
     Pb=24
def three():
     global Ir,Pb
     Ir=Pv_char['BP'][0]
     Pb=24
def four():
     global Ir,Pb
     Ir=Pv_char['Uni-Solar'][0]
     Pb=12
def five():
     global Ir,Pb
     Ir=Pv_char['Shell'][0]
     Pb=12
def Calc():
     global Ah_inverter,Ir,Pb,parallel,Ah_load
     Ah_inverter=(Ir*peak_sun*ce.get()*df.get())/(100*100)
     parallel=int(Ah_load/Ah_inverter)
     series=battery/Pb
     print series,parallel
     i,j=0,0
     x=40;y=40
     canvas1= Canvas(tk6,height=200,width=700,bg='White')
     canvas1.grid(row=9,column=1)
     xx.set(series)
     yy.set(parallel)
     if series==1:
          for i in range(parallel):
               if i==0:
                    canvas1.create_image(x,y,image=photo1)
               else:
                    canvas1.create_image(x,y,image=photo2)
          
               x=x+50
     x=40;y=40
     if series!=1:
          for i in range(parallel):
               if i==0 and j==0:
                    photo=photo3
                    canvas1.create_image(x,y,image=photo)
               for j in range(series):
                    if i==0 and j==1:
                         photo=photo4
                    if i>0 and j==0:
                         photo=photo5
                    if i>0 and j==1:
                         photo=photo6

                    
                    canvas1.create_image(x,y,image=photo)
                    y=y+70
               y=40
               x=x+50
    
###########################
Column_Effeciency =Label(tk6,text = 'Columng Efficiency').grid(row=0,column=0,sticky=W)
Eff1=Entry(tk6,textvariable= ce).grid(row=0,column=1,sticky=W)
Derating_Factor =Label(tk6,text = 'Derating Factor').grid(row=1,column=0,sticky=W)
Eff2=Entry(tk6,textvariable= df).grid(row=1,column=1,sticky=W)
#############
canvas1= Canvas(tk6,height=200,width=800,bg='White')
canvas1.grid(row=9,column=1)
Concorde_5040T= Radiobutton(tk6, text= 'Kyocera',value=1,variable=2,command=one).grid(row=3,column=0,sticky=W)
Trojan_T_105= Radiobutton(tk6, text= 'Sharp',value=2,variable=2,command=two).grid(row=4,column=0,sticky=W)
Trojan_L16= Radiobutton(tk6, text= 'BP',value=3,variable=2,command=three).grid(row=5,column=0,sticky=W)
Concorde_1080= Radiobutton(tk6, text= 'Uni-Solar',value=4,variable=2,command=four).grid(row=6,column=0,sticky=W)
Surette_12CS= Radiobutton(tk6, text= 'Shell',value=5,variable=2,command=five).grid(row=7,column=0,sticky=W)
button=Button(tk6,text='Okay',command=Calc).grid(row=7,column=1)
series=Label(tk6,text = 'Series ').grid(row=10,column=0,sticky=W)
sers=Entry(tk6,textvariable= xx).grid(row=10,column=1)
parallel=Label(tk6,text = 'parallel').grid(row=11,column=0,sticky=W)
pal=Entry(tk6,textvariable= yy).grid(row=11,column=1)
#mbutton2 = Button(tk6, text= 'Show Info ',command= showLoads).grid(row=7,column =2)
tk6.mainloop()
