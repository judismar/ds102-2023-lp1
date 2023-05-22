#Tudo que está depois de # é desconsiderado por Python. Chamamos isso de 'comentário' no código. É para ajudar a própria programadora ou programador a ler o código, ou então ajudar outra pessoa a compreender melhor o código. É o que estarei fazendo aqui!
from random import randint #Da biblioteca 'random' (from random) estamos importando o sub-programa 'randint'. Lembrando que randint leva dois argumentos a e b, a menor que b. Por exemplo, se eu quiser simular um jogo de dados, faço randint(1, 6): isso retorna 1, 2, 3, 4, 5 ou 6.

print("--- Cara, Coroa ou Zai ---")
estaErrado = True #Variável booleana (i.e. que assume apenas dois valores: True ou False) para controlar a repetição do while. Lembrando que, tudo que estiver dentro do bloco while será ignorado se a condição for falsa logo de cara, por isso iniciamos com True. Se for verdadeira, que é o nosso caso, tudo será executado, e repetirá enquanto for verdadeiro (while it is True).

while estaErrado:
    escolha = input("Escolha Cara, Coroa ou Zai: ") #A variável 'escolha' vai armazenar o que for digitado pelo jogador, retornado pelo sub-programa input.
    if not (escolha == "Cara" or escolha == "Coroa" or escolha == "Zai"): #Se o que está na variável 'escolha' não for o que esperamos, então
        print("Erro. Valor inválido.") #o valor será informado novamente, pois estaErrado continua True.
    else: #senão:
        estaErrado = False #depois desta linha, o valor dentro de 'estaErrado' é testado. Como é False, saímos do bloco while e continuamos o jogo.
numeroSorteado = randint(1, 3) #randint(1, 3) retorna um número entre 1 e 3, que é, em seguida, atribuido à variável numeroSorteado. Lembramdo que neste ponto, por termos voltado o código para a esquerda, saímos do bloco 'while'

#Agora precisamos comparar as variáveis 'escolha' e 'numeroSorteado' para ver se o jogador ou a jogadora ganharam. Como a primeira é uma string (texto, ou cadeia de caracteres/símbolos) e a segunda é uma variável do tipo inteiro, temos que associar 1, 2 e 3 à Cara, Coroa ou Zai. Isso pode ser feito assim:

if (escolha == "Cara" and numeroSorteado == 1) or (escolha == "Coroa" and numeroSorteado == 2) or (escolha == "Zai" and numeroSorteado == 3):
	print("O valor sorteado foi " + escolha + ". Você venceu!")
#Se escolhemos Cara e o número sorteado foi 1, ganhamos. Se escolhemos Coroa e o número sorteado foi 2, ganhamos. Se escolhemos Zai e o número sorteado foi 3, ganhamos. Senão (else), perdemos.
else:
	print("Você perdeu, pois o número sorteado foi " + str(numeroSorteado) + ".")
