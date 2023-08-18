

from random import randint
from tkinter import *

TAMANHOFONTE = 18

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

strSaldo = Label(textvariable=saldo, font="Helvetica, " + str(TAMANHOFONTE))
perguntaLabel = Label(text="Escolha entre vermelho ou preto.", font="Helvetica, " + str(TAMANHOFONTE))
vermelho = Button(text="Vermelho", command=escolheuVermelho, font="Helvetica, " + str(TAMANHOFONTE))
preto = Button(text="Preto", command=escolheuPreto, font="Helvetica, " + str(TAMANHOFONTE))
apostaEntrada = Entry(textvariable=aposta, font="Helvetica, " + str(TAMANHOFONTE))
resultadoRotulo = Label(textvariable=resultado, font="Helvetica, " + str(TAMANHOFONTE))

strSaldo.pack()
perguntaLabel.pack()
vermelho.pack()
preto.pack()
apostaEntrada.pack()
resultadoRotulo.pack()

r.mainloop()
