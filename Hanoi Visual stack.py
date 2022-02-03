from tkinter import Tk, Label, Entry, Canvas, Button, Scrollbar, Frame, mainloop, messagebox
from tkinter import*
from time import sleep
class app(Tk):
    def __init__(self):
        Tk.__init__(self)        
        self.geometry("940x630")
        self.config(bg="lightblue")
        self.lb=Label(self,text="Torres de Hanoi", font="Arial 15 underline", bg="lightblue")
        self.lb.place(x=390,y=5)
        self.b1=Button(self,text="Calcular", command=self.resolver)
        self.b1.place(x=550,y=32)
        self.l1=Label(self,text="Anillos", bg="lightblue")
        self.l1.place(x=350,y=40)
        self.c1=Entry(self)
        self.c1.place(x=400,y=40)
        self.c=Canvas(self, width=890, height=540)
        self.c.place(x=20,y=70)
        self.ta=stack(self,150)
        self.tb=stack(self,450)
        self.tc=stack(self,750)
    def resolver(self):
        try:
            n=int(self.c1.get())
            if(n>10 or 0>n ):
                messagebox.showerror("ERROR","DATO FUERA DE RANGO")
            else:
                while not self.tc.empty():
                    temp=self.tc.pop()
                    temp.destroy()
                for i in range(n):
                    color=["salmon","turquoise","violet","greenyellow","hotpink","sandybrown","cyan","lime","gold","tomato"]
                    temp=Button(width=30-i*2, bg=color[i], text=str(i+1))
                    self.ta.push(temp)
                self.hanoi(n,self.ta, self.tb, self.tc)
        except ValueError:
            messagebox.showerror("ERROR","DATO INVALIDO")
    def hanoi(self, n, a, b, d):
        if n==1:
            anillo=a.pop()
            self.horizontal(anillo,d.position-a.position, d.position,a.position)
            d.push(anillo)
        elif n>1:
            self.hanoi(n-1,a,d,b)
            self.hanoi(1,a,b,d)
            self.hanoi(n-1,b,a,d)

    def horizontal(self,a,d,xi,xf): #MOVIMIENTO SUPERIOR IZQUIERDO Y DERECHO
        paso=d//20
        po=xf
        pf=xi
        while po!=pf:            
            if d<0 or d>0 :
                po=po+paso
                a.place(x=po,y=70)
                self.update()
                sleep(0.01)  
class stack():
    def __init__(self,f,x):
        self.position=x 
        self.forma=f
        self.vector=[""]*10
        self.sp=0
        self.forma.c.create_line(x-120,500,x+120,500,width=5)
        self.forma.c.create_line(x,200,x,500,width=5)
    def push(self,e):
        e.place(x=self.position,y=100)
        self.forma.update_idletasks()
        px=self.position-e.winfo_width()//2+20
        py=530-self.sp*30
        y=100
        while y<py:
            e.place(x=px,y=y)
            self.forma.c.update()
            sleep(0.01)
            y+=10
        e.place(x=px,y=py)
        self.vector[self.sp]=e 
        self.sp+=1
    def pop(self):
        self.sp-=1
        e=self.vector[self.sp]
        y=e.winfo_y()
        px=e.winfo_x()
        while y>40:
            e.place(x=px,y=y)
            self.forma.c.update()
            sleep(0.01)
            y-=20
        e.place(x=px,y=30)
        return e
    def empty(self):
        return self.sp==0
app().mainloop()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Reforzar conocimientos de las torres de Hanoiy aplicacion de stacks
#Lenguaje: python
#Net Framewor: 4.5
#Recursos: visual studio
#Descripción: Desarrollar un programa que muestre los movimientos de discos como torre de hanoi VISUAL
#Ultima modificación 26/04/2021