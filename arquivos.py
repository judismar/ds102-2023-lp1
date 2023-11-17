def salva(nomeArquivo, valor): #modo w
    arq = open(nomeArquivo, 'w')
    arq.write(valor)
    arq.close()

def carrega(nomeArquivo): #modo r
    arq = open(nomeArquivo, 'r')
    valor = arq.read()
    arq.close()
    return valor

def carregaLinhaALinha(nomeArquivo):
    lista = []
    arq = open(nomeArquivo, 'r')
    while True:
        linha = arq.readline()
        if linha == "":
            break
        lista.append(linha)
    arq.close()
    return lista

def listaVazia(lista):
    return len(lista) == 0