from random import randint

def roleta():
    x = input("Insira um valor:")
    y = 2

    pergunta = input('vermelho ou  preto?')
    sorteio = randint(0, 1)
    estiverErrado = True
    while estiverErrado :
        if(not(pergunta == "vermelho" or pergunta == 'preto')):
            pergunta = input("Ou é vermelho ou é preto:")
        else:
            estiverErrado = False
    sorteio = randint(0, 1)
    if pergunta == 'vermelho' and sorteio == 0 or pergunta == 'preto' and sorteio == 1:
        print(int(x) * int(y), "O seu valor foi dobrado.")
    else:
        print('Você perdeu tudo!')

dinheiro = 5000.00
opcao = ""
while opcao != "3":
    print("---Jogos e Apps---\nSaldo atual: " + str(dinheiro) + "\n1- Roleta\n2- Calculadora\n3- Sair") #menu
    opcao = input("Escolha sua opção: ")
    if opcao == "1":
       roleta()
