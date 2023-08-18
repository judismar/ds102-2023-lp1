from random import randint
from tkinter import *

#A dinâmica do jogo:
def escolheuVermelho():
    res = randint(0, 1)
    if res == 0:
        resultado.set("Você venceu!")
        x = float(aposta.get())
        y = float(saldo.get())
        y += 2*x
        saldo.set(str(y))
    else:
        resultado.set("Você perdeu!")
        x = float(aposta.get())
        y = float(saldo.get())
        y -= x
        saldo.set(str(y))
        
def escolheuPreto():
    res = randint(0, 1)
    if res == 1:
        resultado.set("Você venceu!")
        x = float(aposta.get())
        y = float(saldo.get())
        y += 2*x
        saldo.set(str(y))
    else:
        resultado.set("Você perdeu!")
        x = float(aposta.get())
        y = float(saldo.get())
        y -= x
        saldo.set(str(y))

#A parte gráfica:
r = Tk()
saldo = StringVar()
saldo.set("5000.00")
resultado = StringVar()
aposta = StringVar()

strSaldo = Label(textvariable=saldo, font="Helvetica, 32")
perguntaLabel = Label(text="Escolha entre vermelho ou preto.", font="Helvetica, 32")
vermelho = Button(text="Vermelho", command=escolheuVermelho, font="Helvetica, 20")
preto = Button(text="Preto", command=escolheuPreto, font="Helvetica, 20")
apostaEntrada = Entry(textvariable=aposta, font="Helvetica, 20")
resultadoRotulo = Label(textvariable=resultado, font="Helvetica, 32")

strSaldo.pack()
perguntaLabel.pack()
vermelho.pack()
preto.pack()
apostaEntrada.pack()
resultadoRotulo.pack()
