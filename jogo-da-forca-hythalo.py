import random

def abertura():
    print("*********************************");
    print("***Bem vindo ao jogo da Forca!***");
    print("*********************************");

def pede_chute():
    chute = input("Qual letra?\n");
    chute = chute.strip().upper();
    return chute;

def marca_chute(chute, letras_acertadas, palavra_secreta):
    index = 0;
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra;
        index += 1;

def carrega_palavra():
    arquivo = open("palavras.txt", "r");
    palavras = [];
    for linha in arquivo:
        linha = linha.strip();
        palavras.append(linha);
    arquivo.close();
    numero = random.randrange(0, len(palavras));
    palavra_secreta = palavras[numero].upper();
    return palavra_secreta;

def desenha_forca(erros):
    print("  _______     ");
    print(" |/      |    ");
    if(erros == 1):
        print (" |      (_)   ");
        print (" |            ");
        print (" |            ");
        print (" |            ");
    if(erros == 2):
        print (" |      (_)   ");
        print (" |      \     ");
        print (" |            ");
        print (" |            ");
    if(erros == 3):
        print (" |      (_)   ");
        print (" |      \|    ");
        print (" |            ");
        print (" |            ");
    if(erros == 4):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |            ");
        print (" |            ");
    if(erros == 5):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |            ");
    if(erros == 6):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |      /     ");
    if (erros == 7):
        print (" |      (_)   ");
        print (" |      \|/   ");
        print (" |       |    ");
        print (" |      / \   ");
    print(" |            ");
    print("_|___         ");
    print();

def vencedor():
    print("Parabéns, você ganhou!");

def perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!");
    print("A palavra era {}".format(palavra_secreta));

abertura()
palavra_secreta = carrega_palavra();
letras_acertadas = ["_" for letra in palavra_secreta];
print(letras_acertadas);
enforcou = False;
acertou = False;
erros = 0;
while(not enforcou and not acertou):
    chute = pede_chute();
    if(chute in palavra_secreta):
        marca_chute(chute, letras_acertadas, palavra_secreta);1
    else:
        erros += 1;
        desenha_forca(erros);
    enforcou = erros == 7;
    acertou = "_" not in letras_acertadas;
    print(letras_acertadas);
if(acertou):
    vencedor();
else:
    perdedor(palavra_secreta);
