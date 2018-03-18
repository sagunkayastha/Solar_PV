
from Tkinter import*
from Block_battery import series,parallel
import sys
tk5=Tk()
series=int(series)
parallel=int(parallel)
sizex=parallel*50+25
sizey= series*50
x,y=25,25
photo1=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\block_i1.gif')
photo2=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\block_i2.gif')
photo3=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\block_imiddle.gif')
photo4=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\block_itop.gif')
photo5=PhotoImage(file='C:\\Users\\Sagun\\Desktop\\Sem Break\\Solar PV\\images\\block_ibot.gif')
canvas1= Canvas(tk5,height=sizey,width=sizex,bg='White')
canvas1.pack()
print sizex,sizey
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


     
tk5.mainloop()

