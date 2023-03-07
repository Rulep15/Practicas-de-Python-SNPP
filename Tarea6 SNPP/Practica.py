from textwrap import fill
import tkinter 

ventana=tkinter.Tk()
ventana.geometry("400x300")

cajatexto=tkinter.Entry(ventana)
cajatexto.pack()

etiqueta=tkinter.Label(ventana)
etiqueta.pack()

def textoDelaCaja():
    text20=cajatexto.get()
    etiqueta["text"]=text20

boton1=tkinter.Button(ventana, text="click",command=textoDelaCaja)
boton1.pack()

ventana.mainloop()
