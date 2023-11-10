def salva(nomeArquivo, valor): #modo w
    arq = open(nomeArquivo, 'w')
    arq.write(valor)
    arq.close()

def carrega(nomeArquivo): #modo r
    arq = open(nomeArquivo, 'r')
    valor = arq.read()
    arq.close()
    return valor