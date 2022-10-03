
from cgitb import text
from email import message
from enum import auto
import json
from tkinter import *
from tkinter import messagebox



Usuario= "20547537-0"
password="mati"


def validar():
    if txt1.get() == Usuario:
        if txt2.get() == password:
            abrirventana2()
        else:
            messagebox.showwarning("ERROR", "usuario o contraseña incorrectos")

    else:
        messagebox.showwarning("cuidado", "Usuario o contraseña incorrectos incorrecto")

def abrirventana2():
    vent.withdraw()
    vent2=Tk()
    vent2.geometry("1900x1050")
    vent2.config(bg= "#B6F7CC")
    lbl2vent=Label(vent2, text="bienvenido a MedicApp")
    lbl2vent.config(bg="#B6F7CC", fg="black")
    
   










vent = Tk()
vent.title("MedicApp")
vent.geometry("600x400")
vent.config(bg="#B6F7CC")

#####################################################
lblTittle= Label(vent, text="""Para acceder 
ingrese 
los siguientes datos:""")
lblTittle.place(relx=00.40, rely=0.05 )
lblTittle.config(bg="#B6F7CC", fg="black")
lbl= Label(vent, text="""Rut sin punto
con guion:""", bg= "White")
lbl.place(relx=0.40, rely=0.18, width=100,height=30)

txt1= Entry(vent, bg= "white")
txt1.place(relx=0.40, rely=0.28, width=100,height=30)

lblslash= Label(vent, text="................................")
lblslash.place(relx=0.40, rely=0.38)
lblslash.config(bg="#B6F7CC")


lbl2= Label(vent, text="Contraseña :", bg= "White")
lbl2.place(relx=0.40, rely=0.48, width=100,height=30)

txt2= Entry(vent, bg= "white")
txt2.place(relx=0.40, rely=0.58, width=100,height=30)

btn=Button(vent, text= "INGRESAR", command=validar)
btn.place(relx=0.41,rely=0.68, width= 80, height=30)
btn.config(bg="green",fg="white")



vent.mainloop()

 