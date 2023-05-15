from random import randint

print("--- Cara, Coroa ou Zai ---")
x = input("Escolha Cara, Coroa: ")
estiverErrado = True
while estiverErrado:
    if not (x == "Cara" or x == "Coroa" or x == "Zai"):
        x = input("Erro. Informe Cara, Coroa ou Zai: ")
    else:
        estiverErrado = False
y = randint(0, 2)
if y == 0:
    y = "Cara"
else:
    if y == 1:
        y = "Coroa"
    else:
        if y == 2:
            y = "Zai"
