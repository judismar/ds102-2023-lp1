from random import randint
from tkinter import *
from functools import partial

#Crédito aos alunos Pablo, Luiz Felipe e Serra pela ideia do jogo da roleta. :)
#Usem este código como base para desenvolver outros apps com tkinter (para quem gostou).

#A dinâmica do jogo:
def pretoOuVermelho(cor, aposta, saldo, resultado):
	res = randint(0, 1)
	valorAposta = float(aposta.get())
	valorSaldo = float(saldo.get())
	if valorAposta > valorSaldo:
		resultadoRotulo["foreground"] = "red"
		resultado.set("O valor da aposta não pode ser\nmaior do que o saldo atual.")
		return
	if not valorAposta >= 0:
		resultadoRotulo["foreground"] = "red"
		resultado.set("O valor da aposta não pode ser\nmenor que 0.")
		return
	resultadoRotulo["foreground"] = "black"
	if res == 0:
		s = "Caiu na casa preta.\n"
		if cor == "preta":
			resultado.set(s + "Você venceu!")
			strSaldo["foreground"] = "green"
			saldo.set(str(valorSaldo + 2*valorAposta))
		else:
			resultado.set(s + "Você perdeu!")
			strSaldo["foreground"] = "red"
			saldo.set(str(valorSaldo - valorAposta))
	else:
		s = "Caiu na casa vermelha.\n"
		if cor == "vermelha":
			resultado.set(s + "Você venceu!")
			strSaldo["foreground"] = "green"
			saldo.set(str(valorSaldo + 2*valorAposta))
		else:
			resultado.set(s + "Você perdeu!")
			strSaldo["foreground"] = "red"
			saldo.set(str(valorSaldo - valorAposta))

#A parte gráfica:
r = Tk()
saldo = StringVar()
saldo.set("5000.00")
resultado = StringVar()
aposta = StringVar()
aposta.set("0")

strSaldo = Label(textvariable=saldo, font="Helvetica, 32")
perguntaLabel = Label(text="Escolha entre vermelho ou preto.", font="Helvetica, 32")
vermelho = Button(text="Vermelho", command=partial(pretoOuVermelho, "vermelha", aposta, saldo, resultado), font="Helvetica, 20")
preto = Button(text="Preto", command=partial(pretoOuVermelho, "preta", aposta, saldo, resultado), font="Helvetica, 20")
apostaEntrada = Entry(textvariable=aposta, font="Helvetica, 20")
resultadoRotulo = Label(textvariable=resultado, font="Helvetica, 32")

strSaldo.pack()
perguntaLabel.pack()
vermelho.pack()
preto.pack()
apostaEntrada.pack()
resultadoRotulo.pack()

r.mainloop()
